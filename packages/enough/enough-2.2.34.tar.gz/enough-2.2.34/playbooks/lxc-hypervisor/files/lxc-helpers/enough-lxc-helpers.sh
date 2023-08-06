#!/bin/bash

LXC_SELF_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
LXC_BIN=/usr/local/bin

: ${LXC_SUDO:=}
: ${LXC_CONTAINER_RELEASE:=bookworm}
: ${LXC_HOME:=/home}

source /etc/os-release

function lxc_release() {
    echo $VERSION_CODENAME
}

function lxc_template_release() {
    echo enough-$LXC_CONTAINER_RELEASE
}

function lxc_root() {
    local name="$1"

    echo /var/lib/lxc/$name/rootfs
}

function lxc_container_run() {
    local name="$1"
    shift

    $LXC_SUDO lxc-attach --clear-env --name $name -- "$@"
}

function lxc_container_run_script_as() {
    local name="$1"
    local user="$2"
    local script="$3"

    $LXC_SUDO chmod +x $(lxc_root $name)$script
    $LXC_SUDO lxc-attach --name $name -- sudo --user $user $script
}

function lxc_container_run_script() {
    local name="$1"
    local script="$2"

    $LXC_SUDO chmod +x $(lxc_root $name)$script
    lxc_container_run $name $script
}

function lxc_container_inside() {
    local name="$1"
    shift

    lxc_container_run $name $LXC_BIN/enough-lxc.sh "$@"
}

function lxc_container_user_install() {
    local name="$1"
    local user_id="$2"
    local user="$3"

    if test "$user" = root ; then
	return
    fi

    local root=$(lxc_root $name)

    if ! $LXC_SUDO grep --quiet "^$user " $root/etc/sudoers ; then
	$LXC_SUDO tee $root/usr/local/bin/enough-create-user.sh > /dev/null <<EOF
#!/bin/bash
set -ex

mkdir -p $LXC_HOME
useradd --base-dir $LXC_HOME --create-home --shell /bin/bash --uid $user_id $user
for group in docker kvm libvirt ; do
    if grep --quiet \$group /etc/group ; then adduser $user \$group ; fi
done
echo "$user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
sudo --user $user ssh-keygen -b 2048 -N '' -f $LXC_HOME/$user/.ssh/id_rsa
EOF
	lxc_container_run_script $name /usr/local/bin/enough-create-user.sh
    fi
}

function lxc_prepare_environment() {
    if test $(id -u) != 0 ; then
        LXC_SUDO=sudo
    fi
    if ! $(which lxc-create > /dev/null) ; then
	$LXC_SUDO apt-get install -y -qq make git libvirt0 libpam-cgfs bridge-utils uidmap dnsmasq-base dnsmasq dnsmasq-utils qemu-user-static
    fi
}

function lxc_container_configure() {
    local name="$1"
    
    $LXC_SUDO tee -a /var/lib/lxc/$name/config > /dev/null <<'EOF'
security.nesting = true
lxc.cap.drop =
lxc.apparmor.profile = unconfined
#
# /dev/net (docker won't work without /dev/net/tun)
#
lxc.cgroup2.devices.allow = c 10:200 rwm
lxc.mount.entry = /dev/net dev/net none bind,create=dir 0 0
#
# /dev/kvm (libvirt / kvm won't work without /dev/kvm)
#
lxc.cgroup2.devices.allow = c 10:232 rwm
lxc.mount.entry = /dev/kvm dev/kvm none bind,create=file 0 0
#
# /dev/loop
#
lxc.cgroup2.devices.allow = c 10:237 rwm
lxc.cgroup2.devices.allow = b 7:* rwm
lxc.mount.entry = /dev/loop-control dev/loop-control none bind,create=file 0 0
#
# /dev/mapper
#
lxc.cgroup2.devices.allow = c 10:236 rwm
lxc.mount.entry = /dev/mapper dev/mapper none bind,create=dir 0 0
#
# /dev/fuse
#
lxc.cgroup2.devices.allow = b 10:229 rwm
lxc.mount.entry = /dev/fuse dev/fuse none bind,create=file 0 0
EOF


    #
    # Wait for the network to come up
    #
    local wait_networking=$(lxc_root $name)/usr/local/bin/enough-wait-networking.sh
    $LXC_SUDO tee $wait_networking > /dev/null <<'EOF'
#!/bin/sh -e
for d in $(seq 60); do
  getent hosts wikipedia.org > /dev/null && break
  sleep 1
done
getent hosts wikipedia.org > /dev/null || getent hosts wikipedia.org
EOF
    $LXC_SUDO chmod +x $wait_networking
}

function lxc_container_start() {
    local name="$1"
    local root="$2"

    if lxc_running $name ; then
	return
    fi

    if test "$root" ; then
	$LXC_SUDO mkdir -p /var/lib/lxc/$name/rootfs/$root
	$LXC_SUDO mount --bind $root /var/lib/lxc/$name/rootfs/$root
    fi

    $LXC_SUDO lxc-start $name
    $LXC_SUDO lxc-wait --name $name --state RUNNING
    lxc_container_run $name /usr/local/bin/enough-wait-networking.sh
}

function lxc_container_stop() {
    local name="$1"
    local root="$2"

    $LXC_SUDO lxc-ls -1 --running --filter="^$name" | while read container ; do
	$LXC_SUDO lxc-stop --kill --name="$container"
    done

    if test "$root" ; then
	$LXC_SUDO lxc-ls -1 --filter="^$name" | while read container ; do
	    local mountpoint=/var/lib/lxc/$container/rootfs/$root
	    if $LXC_SUDO test -e $mountpoint ; then
		$LXC_SUDO umount $mountpoint
	    fi
	done
    fi
}

function lxc_container_destroy() {
    local name="$1"
    local root="$2"

    if lxc_exists "$name" ; then
	lxc_container_stop $name $root
	$LXC_SUDO lxc-destroy --force --name="$name"
    fi
}

function lxc_exists() {
    local name="$1"

    test "$($LXC_SUDO lxc-ls --filter=^$name)"
}
    
function lxc_running() {
    local name="$1"

    test "$($LXC_SUDO lxc-ls --running --filter=^$name)"
}

function lxc_build_template_release() {
    local name="$(lxc_template_release)"
    
    if lxc_exists $name ; then
	return
    fi

    local root=$(lxc_root $name)
    local packages="sudo,git,python3"
    $LXC_SUDO lxc-create --name $name --template debian -- --release=$LXC_CONTAINER_RELEASE --packages="$packages"
    $LXC_SUDO cp -a $LXC_SELF_DIR/enough-lxc*.sh $root/$LXC_BIN
    lxc_container_configure $name
}

function lxc_build_template() {
    local name="$1"
    local newname="$2"

    if lxc_exists $newname ; then
	return
    fi

    if test "$name" = "$(lxc_template_release)" ; then
	lxc_build_template_release
    fi
    
    $LXC_SUDO lxc-copy --name=$name --newname=$newname
}

function lxc_apt_install() {
    local name="$1"
    shift

    lxc_container_inside $name lxc_apt_install_inside "$@"
}

function lxc_apt_install_inside() {
    DEBIAN_FRONTEND=noninteractive apt-get install -y -qq "$@"
}

function lxc_install_lxc() {
    local name="$1"
    local prefix="$2"

    lxc_container_inside $name lxc_install_lxc_inside $prefix
}

function lxc_install_lxc_inside() {
    local prefix="$1"
    
    local packages="make git libvirt0 libpam-cgfs bridge-utils uidmap dnsmasq-base dnsmasq dnsmasq-utils qemu-user-static"
    if test "$(lxc_release)" = bookworm ; then
	packages="$packages lxc-templates debootstrap distro-info"
    fi

    lxc_apt_install_inside $packages

    if ! systemctl is-active --quiet lxc-net; then
	systemctl disable --now dnsmasq
	apt-get install -y -qq lxc
	systemctl stop lxc-net
	sed -i -e '/ConditionVirtualization/d' $root/usr/lib/systemd/system/lxc-net.service
	systemctl daemon-reload
	cat >> /etc/default/lxc-net <<EOF
LXC_ADDR="$prefix.1"
LXC_NETMASK="255.255.255.0"
LXC_NETWORK="$prefix.0/24"
LXC_DHCP_RANGE="$prefix.2,$prefix.254"
LXC_DHCP_MAX="253"
EOF
	systemctl start lxc-net
    fi
}

function lxc_install_docker() {
    local name="$1"

    lxc_container_inside $name lxc_install_docker_inside
}

function lxc_install_docker_inside() {
    lxc_apt_install_inside docker.io docker-compose
}

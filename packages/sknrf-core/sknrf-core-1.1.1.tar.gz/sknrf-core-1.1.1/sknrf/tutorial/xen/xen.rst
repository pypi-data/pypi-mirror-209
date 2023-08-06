Citrix (Xen) Hypervisor
=======================

Objective
---------

Install a Type I Hypervisor so that you can install multiple operating systems for SMP or AMP.

Requirements
------------

1. A processor that support hypervisor virtualization.
2. A BIOS with virtualization enabled.
3. Debian as the Dom0 Linux Distribution.

This procedure uses Debian rather than the default Citrix Hypervisor (based on CentOS) because the
"xen-tools" package simplifies Virtual Machine (VM) creating for beginners.

API
---

.. code-block:: bash

    xl info  # Dom0 status
    xl list  # DomN list
    xl top   # List resources used by each DomN

    xl create -c <domU-name>.cfg  # Create/Boot new VM
    xl shutdown <domU-name>  # Shutdown VM
    xl destroy <domU-name>  # Remove VM


Procedure
---------

0. Configure BIOS
~~~~~~~~~~~~~~~~~

Press F2 to enter the BIOS and enable virtualization.

    - System BIOS > Processor Settings > Virtualization Technology Enabled

Press F11 to Enter Boot Manager

    - One-shot UEFI Boot Menu > Disk connected to back USB1: USB Flash Drive.
 
1. Install Dom0 (Debian)
~~~~~~~~~~~~~~~~~~~~~~~

Download the `Debian Net-Install<http://cdimage.debian.org/debian-cd/current/amd64/iso-cd/>`_
and validate the checksum

.. code-block:: bash

    wget http://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.0.0-amd64-netinst.iso
    wget http://cdimage.debian.org/debian-cd/current/amd64/iso-cd/SHA256SUMS -O debian-11.0.0-amd64-netinst_shasum256
    shasum -a 256 debian-11.0.0-amd64-netinst.iso ; cat debian-11.0.0-amd64-netinst_shasum256

Burn to USB key with boot flag.

.. code-block:: bash

    sudo umount /dev/sd<a-z>[<1-9>]
    sudo dd bs=4M if=debian-11.0.0-amd64-netinst.iso of=/dev/sd<a-z>[<1-9]>
    sudo sync


Insert USB key into server and boot from USB.

    #. Select Graphical Install  (images store in /var/log/)
    #. Select a Language: **English   - English**
    #. Select your Location: **United States**
    #. Configure the keyboard: **American English**
    #. Configure the network: **eno1: Broadcom Inc. ...**
        #. Please Enter the hostname of the system: **NSFW1-DOM0**
        #. Please Enter the domain name of the system: **Cisco**
    #. Set up users and passwords:
        #. Enter root password: **#######**
        #. Add user account:
            #. User Full Name: **Dylan Bespalko**
            #. Username: **dylan**
            #. User password: **########**
    #. Configure the clock:
        #. Time-Zone: **Pacific**
    #. Partition disks
        #. Partitioning method: **Manual**
            #. sda1    /boot 536.9 MB    B f    ESP    boot              # Set Boot flag: on
            #. sda2    /     16 GB         f    ext4   rootfs      /
            #. sda3          128 GB        f    swap   swap        swap  # swap size should be 1x the amount of RAM
            #. sda4    (reserved for LVM)              llvmm             # LVM disk should not be formatted
        #. Write Changes to Disks? **Yes**
    #. Configure the package manager
        #. Debian archive mirror country: **United States**
        #. Debian archive mirror: **deb.debian.org**
        #. HTTP proxy information: **Leave blank**
    #. Configuring popularity-contest
        #. Participate in the package usage survey: **No**
    #. Software selection
        #. Choose software to install: ** SSH server, standard system utilities**
    #. Finish the installation: **Press Continue**

Update Debian firmware and software:

.. code-block:: bash

    apt-get update
    apt-get upgrade
    apt-get install vim

    vim /etc/apt/sources.list # append "contrib non-free" to deb/deb-src repos as follows:
    # deb http://some.debian.server.org/debian bullseye main contrib non-free
    # deb http://some.debian.server.org/debian bullseye main contrib non-free

    apt-get update
    apt-get upgrade
    apt-get install firmware-linux-nonfree

2. Install Citrix (Xen) Hypervisor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install the Citrix Hypervisor and xen-tools

.. code-block:: bash

    apt-get install xen-system-amd64
    apt-get install xen-tools

Configure the Grub Bootloader to default to Debian with Xen Hypervisor boot option.

.. code-block:: bash

    sed -i 's/GRUB_DEFAULT=0/GRUB_DEFAULT=2/g' /etc/default/grub
    update-grub

Restart the server. 

Conifgure SSH server of DOM0:

.. code-block:: bash

    sed -i 's/#Port 22/Port 2222/g' /etc/ssh/sshd_config
    systemctl restart ssh.service


Connect to DOM0 from a remote machine:

.. code-block:: bash

    ssh -p 2222 dylan@<ip-addr>
    su -

2. a) Configure the Linux Logical Volume (LVM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install lvm2

.. code-block:: bash

    apt-get install lvm2

A group of disks can be virtualized as follows:

    - Physical Volume (PV)
        - Volume Group (VG)
            - Logical Volume (LV)

Configure the LV for your VM

.. code-block:: bash

    pvcreate /dev/sda4
    vgcreate vg0 /dev/sda4
    # lvcreate -n TILE0-data -L 350G vg0  # Performed by xen-tools
    # lvcreate -n TILE0-swap -L 64G vg0  # Performed by xen-tools

2. b) Configure the Linux Network Bridge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Install lvm2

.. code-block:: bash

    apt-get install bridge-utils

Create a Linux Network Bridge (a software ethernet switch) that shares a physical network port as follows:

    - Physical Port (Network Protocol Layer 1 and Layer 2)
        - Bridge (Network Protocol Layer 3)

Replace the existing Network Config File (/etc/network/interfaces):

.. code-block:: bash

    auto lo
    iface lo inet loopback

    allow-hotplug eno1
    iface eno1 inet dhcp

With the following Linux Bridge:

.. code-block:: bash

    auto lo
    iface lo inet loopback

    allow-hotplug eno1
    iface eno1 inet manual

    auto xenbr0
    iface xenbr0 inet dhcp
         bridge_ports eno1


    allow-hotplug eno2
    iface eno2 inet manual

    auto xenbr1
    iface xenbr1 inet dhcp
         bridge_ports eno2

Restart the network service and list the bridge configurations

.. code-block:: bash

    service networking restart

2. c) Validate the Dom0 Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Verify that Xen Hypervisor loads during boot:

.. code-block:: bash

    egrep '(vmx|svm|hypervisor)' /proc/cpuinfo  # Verify that the CPU supports hypervisor virtualization
    xl dmesg  # Filter dmesg system log to only show Xen messages

Verify that Linux logical volumes exist:

.. code-block:: bash

    lvdisplay

Verify that Linux Network Bridge exists:

.. code-block:: bash

    brctl show

Check IP Address of DOM0:

.. code-block:: bash

    ip addr

3. a) Assign Hardware to DomU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify the pci backend as follows:

.. code-block:: bash
    modprobe xen-pciback          # Should not generate error
    lspci | grep 03:00.3           # Filter by pci address
    xl pci-assignable-add 03:00.3  # assign device to DomU
    xl pci-assignable-list         # check DomU devices                                # Check the pci devices available for assignment.

3. a) Create a Paravirtualized Guest using Xen-Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

xen-tools does the following in one command:

    #. Create logical volume for rootfs
    #. Create logical volume for swap
    #. Create filesystem for rootfs
    #. Mount rootfs
    #. Install operating system using debootstrap (or rinse etc, only debootstrap covered here)
    #. Run a series of scripts to generate guest config files like fstab/inittab/menu.lst
    #. Create a VM config file for the guest
    #. Generate a root password for the guest system
    #. Unmount the guest filesystem

.. code-block:: bash

    xen-create-image --hostname=TILE0 \
      --memory=64GB \
      --vcpus=22 \
      --lvm=vg0 \
      --size=380GB \
      --swap=64GB \
      --bridge=xenbr0 \
      --dhcp \
      --pygrub \
      --dist=bionic


To delete a vm image:

.. code-block:: bash
    xen-delete-image --lvm=vg0 --hostname=TILE0
    # todo: xt-customize-image
    #    default hook scripts in /usr/share/xen-tools/bionic.d
    #    custom hook scripts in /etc/xen-tools/hooks.d

Verify the VM Log and Configuration File. Record the root password:

.. code-block:: bash
    vim /var/log/xen-tools/TILE0.log
    vim /etc/xen/TILE0.cfg  # Add xenbr1 ethernet bridge

The final cfg file should be as follows:

.. code-block:: bash

    #
    # Configuration file for the Xen instance TILE0, created
    # by xen-tools 4.9 on Sun Oct 10 13:51:36 2021.
    #

    #
    #  Kernel + memory size
    #


    bootloader = 'pygrub'

    vcpus       = '22'
    memory      = '65536'

    #
    #  Disk device(s).
    #
    root        = '/dev/xvda2 ro'
    disk        = [
                      'phy:/dev/vg0/TILE0-disk,xvda2,w',
                      'phy:/dev/vg0/TILE0-swap,xvda1,w',
                  ]


    #
    #  Physical volumes
    #


    #
    #  Hostname
    #
    name        = 'TILE0'

    #
    #  Networking
    #
    dhcp        = 'dhcp'
    vif         = [
                    'mac=00:16:3E:FB:E5:B6,bridge=xenbr0',
                    'mac=00:16:3E:FB:E5:B7,bridge=xenbr1',
                  ]

    #
    # PCI Forwarding
    #
    iommu = "soft"
    pci = [ '03:00.3,permissive=1' ]

    #
    #  Behaviour
    #
    on_poweroff = 'destroy'
    on_reboot   = 'restart'
    on_crash    = 'restart'

Create the VM and boot to console

.. code-block:: bash

    xl create -c /etc/xen/TILE0.cfg

Configure SSH/VNC Server

.. code-block:: bash

    apt update
    apt upgrade
    passwd
    ip addr
    adduser dylan
    passwd dylan
    apt install vim
    apt install pciutils
    sed -i 's/#Port 22/Port 2222/g' /etc/ssh/sshd_config
    systemctl restart sshd.service
    systemctl status sshd.service


Connect from a SSH Client

.. code-block bash

    ping <ip-address>
    ssh -p 2222 -L 5900:localhost:5903 dylan@<ip-address>

Configure the Server

.. code-block bash

    su -
    adduser tilemasters
    passwd tilemasters
    usermod -a -G adm,tty,dialout,cdrom,sudo,dip,plugdev tilemasters

    apt install terminator
    apt install tigervnc-standalone-server tigervnc-xorg-extension tigervnc-viewer
    apt install ubuntu-gnome-desktop
    systemctl enable gdm
    systemctl start gdm
    vncpasswd
    vncserver :3

Connect from a VNC Client

.. code-block bash

    vncviewer :3


3. b) Create a Paravirtualized Guest Manually
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create the LV:

.. code-block:: bash

    lvcreate -n TILE0-data -L 350G vg0
    lvcreate -n TILE0-swap -L 64G vg0
    lvdisplay

Verify the Network Bridge:

.. code-block:: bash

    brctl show

Create the VM Configuration File:

.. code-block:: bash

    # DomU settings
    memory = 4000
    name = 'TILE0'
    vcpus = 4
    maxvcpus = 4

    kernel = "/media/cdrom/boot/vmlinuz-virt"
    ramdisk = "/media/cdrom/boot/initramfs-virt"
    extra="modules=loop,squashfs console=hvc0"


    #
    #  Disk device(s).
    #
    root        = '/dev/xvda2 ro'
    disk        = [
                      'phy:/dev/vg0/NSFW1-DOM1-disk,xvda2,w',
                      'phy:/dev/vg0/NSFW1-DOM1-swap,xvda1,w',
                      'format=raw, vdev=xvdc, access=r, devtype=cdrom, target=/root/iso/alpine-virt-3.14.2-x86_64.iso'
                  ]


    #
    #  Physical volumes
    #

    #
    #  Networking
    #
    dhcp        = 'dhcp'
    vif         = [ 'bridge=xenbr1' ]

    #
    #  Behaviour
    #
    on_poweroff = 'destroy'
    on_reboot   = 'restart'
    on_crash    = 'restart'

Go to "Create the VM and boot to console"

References
----------

https://askubuntu.com/questions/1336194/how-to-connect-openvpn-automatically-on-boot-using-openvpn3-autoload
https://openvpn.net/blog/openvpn-3-linux-and-auth-user-pass/
https://wiki.xenproject.org/wiki/Xen_PCI_Passthrough
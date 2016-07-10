#!/bin/bash 

#———————————————————
# ——Virtual——
#———————————————————
#By Marisol_Martinez_Madrigal



sudo virt-install 
--connect qemu:///system 
-n KVM-fedora 
-r 1024 
--disk path=/home/user/vms/fedora.img,size=20 
-c /home/user/os/Fedora-Live-LXDE-i686-21-5.iso 
-network network:default 
--os -variant fedora 
--os-type linux 
--hvm 





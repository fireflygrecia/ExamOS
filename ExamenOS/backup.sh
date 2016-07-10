#!/bin/bash 

#———————————————————
# —— Backup_script——
#———————————————————
#By Marisol_Martinez_Madrigal


echo ” Initializing Backup ”
 
  account =$ user
  day =$ (date + %d)
  month =$ (date + %m)
  year =$ (date + %y)
  hour =$ (date + %h) 
  minutes =$ (date + %m)

    backup = "Backup_"$account”_”$day”_”$month”_”$year”_”$hour$minutes”.tar.xz"

echo “Packing files”

  tar zcvf "$backup” /home/$account









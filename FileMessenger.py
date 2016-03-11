#!/usr/bin/env python

'''
v0.4 2016 Mar. 13
	- project name was typo (FieMessenger)
v0.3 2016 Feb. 27
    - add while True and usb insert check
v0.2 2016 Feb. 27
    - add msgr_filecopy()
v0.1 2016 Feb. 27
    - just hello
'''

import os.path
import shutil
import time
import subprocess

pizeropath="/home/pi/BYOP"
usbpath="/media/BYOP"

def msgr_filecopy(srcdir, dstdir, filename):
    if os.path.isdir(srcdir)==False:
        print "no file"
        return
    srcpath = srcdir + "/" + filename
    dstpath = dstdir + "/" + filename
    shutil.copyfile(srcpath, dstpath)    

chk1=False
chk2=False
chk3=False
while True:
    chk1 = chk2
    chk2 = chk3
    chk3 = os.path.isdir(usbpath)
    if os.path.isdir(pizeropath) and os.path.isdir(usbpath):
        if chk1==False and chk2==False and chk3==True:    
            msgr_filecopy(usbpath, pizeropath, "name.txt")
            msgr_filecopy(usbpath, pizeropath, "send.txt")
            msgr_filecopy(pizeropath, usbpath, "rcvd.txt")    
            #umount
            cmd=["umount", usbpath]
	    print cmd
	    subprocess.Popen(cmd, bufsize=0)
	    print "Copied"

    time.sleep(0.5) #second
    

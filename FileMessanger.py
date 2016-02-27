#!/usr/bin/env python

'''
v0.2 2016 Feb. 27
    - add msgr_filecopy()
v0.1 2016 Feb. 27
    - just hello
'''

import os.path
import shutil

pizeropath="/home/pi/BYOP"
usbpath="/media/BYOP"

def msgr_filecopy(srcpath, dstpath):
    print "myUpdate"
    if os.path.isdir(usbpath)==False:
        print "no file"
        return
    shutil.copyfile(srcpath, dstpath)    

srcname=usbpath + "/" + "name.txt"
dstname=pizeropath + "/" + "name.txt"
print srcname

msgr_filecopy(srcname, dstname)

    

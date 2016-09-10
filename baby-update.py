#!/usr/bin/env python
#
# BABY Framework update module
# Created By D@nt3 (Ritik Dubey)
# Email : blackdeath8765@Gmail.Com


import subprocess
import os
from core import wcolors

def update_websploit():
	print wcolors.color.GREEN + "[*]Updating Baby framework, Please Wait ..." + wcolors.color.ENDC
	try:
		subprocess.Popen("cd /tmp;git clone https://github.com/dblackmorris/baby.git;cp -R websploit/ /usr/share;rm -rf /tmp/baby/", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	except Exception, e:
		print wcolors.color.RED + "[!] Update Failed."+ wcolors.color.ENDC
		pass

	print wcolors.color.GREEN + "[*]Update was completed successfully." + wcolors.color.ENDC
if __name__ == "__main__":
	update_websploit()

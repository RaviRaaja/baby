#!/usr/bin/env python
#
# BABY Framework Help module
# Created By D@nt3 (Ritik Dubey)
# Email : blackdeath8765@Gmail.Com

from core import wcolors
from time import sleep
def help():
    print "\n"
    print (wcolors.color.BLUE + "Commands\t\tDescription" + wcolors.color.ENDC)
    print (wcolors.color.GREEN + "---------------\t\t----------------" + wcolors.color.ENDC)
    print "set \t\t\tSet Value Of Options To Modules"
    print "scan\t\t\tScan Wifi (Wireless Modules)"
    print "stop\t\t\tStop Attack & Scan (Wireless Modules)"
    print "run \t\t\tExecute Module"
    print "use \t\t\tSelect Module For Use"
    print "os \t\t\tRun Linux Commands(ex : os ifconfig)"
    print "back\t\t\tExit Current Module"
    print "show modules\t\tShow Modules of Current Database"
    print "show options\t\tShow Current Options Of Selected Module"
    print "upgrade\t\t\tGet New Version"
    print "update\t\t\tUpdate Baby Framework "
    print "about\t\t\tAbout US"
    print ""

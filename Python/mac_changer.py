#!usr/bin/env python
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args() #Values and arguments entered by the user
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
        #code to handle an error, error being they haven't inputted any info
    elif not options.new_mac:
         parser.error("[-] Please specify an interface, use --help for more info")
        #code to handle an error, error being they haven't inputted any info
    return options


def change_mac(interface, new_mac):
     print('[+] Changing MAC address for ' + interface + " to " + new_mac)
     subprocess.call(["ifconfig", interface, "down"])
     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
     subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
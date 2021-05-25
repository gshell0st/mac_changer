#python3

import subprocess
import optparse
import re

def perfumaria():
	print('''
			
								
		@@@@@@@@@@    @@@@@@    @@@@@@@              @@@@@@@  @@@  @@@   @@@@@@   @@@  @@@   @@@@@@@@  @@@@@@@@  @@@@@@@   
		@@@@@@@@@@@  @@@@@@@@  @@@@@@@@             @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@ @@@  @@@@@@@@@  @@@@@@@@  @@@@@@@@  
		@@! @@! @@!  @@!  @@@  !@@                  !@@       @@!  @@@  @@!  @@@  @@!@!@@@  !@@        @@!       @@!  @@@  
		!@! !@! !@!  !@!  @!@  !@!                  !@!       !@!  @!@  !@!  @!@  !@!!@!@!  !@!        !@!       !@!  @!@  
		@!! !!@ @!@  @!@!@!@!  !@!       @!@!@!@!@  !@!       @!@!@!@!  @!@!@!@!  @!@ !!@!  !@! @!@!@  @!!!:!    @!@!!@!   
		!@!   ! !@!  !!!@!!!!  !!!       !!!@!@!!!  !!!       !!!@!!!!  !!!@!!!!  !@!  !!!  !!! !!@!!  !!!!!:    !!@!@!    
		!!:     !!:  !!:  !!!  :!!                  :!!       !!:  !!!  !!:  !!!  !!:  !!!  :!!   !!:  !!:       !!: :!!   
		:!:     :!:  :!:  !:!  :!:                  :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:   !::  :!:       :!:  !:!  
		:::     ::   ::   :::   ::: :::              ::: :::  ::   :::  ::   :::   ::   ::   ::: ::::   :: ::::  ::   :::  
		:      :     :   : :   :: :: :              :: :: :   :   : :   :   : :  ::    :    :: :: :   : :: ::    :   : :  
																														
			
	''')

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC add")
	parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
	(options, arguments) = parser.parse_args()

	if not options.interface:
		parser.error("[-] Please specify an interface, use --help for more info")

	elif not options.new_mac:
		parser.error("[-] Please specify a new MAC address, use --help for more info")
	
	return options

def change_mac(interface, new_mac):
	print(f'[+] Changing MAC address for {interface} to {new_mac}')
	subprocess.call(["sudo", "ifconfig", interface, "down"])
	subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["sudo", "ifconfig", interface, "up"])

options = get_arguments()
#change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["sudo", "ifconfig", options.interface])
mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
print(mac_address_search_result.group(0))

perfumaria()
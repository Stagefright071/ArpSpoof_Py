# ArpSpoof_Py
ARP (Address Resolution Protocol), used to translate between MAC (Media Access Control) addresses and IP (Internet Protocol) addresses. ARP resolves IPs to MAC addresses by asking, “Who has IP address 192.168.1.43.” An example of an ARP reply is “192.168.1.43 is at 02:0c:29:69:19:65."

What this script allows you to do is to **spoof** (fake) ARP, putting you in the middle of the connection which could be useful for packet sniffing, modifying packets, etc.

```
╭─compromyse@Aspire ~/Projects/ArpSpoof_Py ‹main› 
╰─$ sudo python3 ArpSpoof.py

░█████╗░██████╗░██████╗░░██████╗██████╗░░█████╗░░█████╗░███████╗██████╗░██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚██╗░██╔╝
███████║██████╔╝██████╔╝╚█████╗░██████╔╝██║░░██║██║░░██║█████╗░░██████╔╝░╚████╔╝░
██╔══██║██╔══██╗██╔═══╝░░╚═══██╗██╔═══╝░██║░░██║██║░░██║██╔══╝░░██╔═══╝░░░╚██╔╝░░
██║░░██║██║░░██║██║░░░░░██████╔╝██║░░░░░╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═════╝░╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░░░░╚═╝░░░

User is root, the script can continue...

1. virbr0
2. vmnet1
3. virbr0-nic
4. vmnet8
5. wlp0s20f3
6. docker0
7. enp2s0

Pick your network card (The number beside it) > 5

You have picked wlp0s20f3

Enter the IP address of target > 192.168.1.12

IP is valid, script can continue...


Enter the IP address of router > 192.168.1.254

IP is valid, script can continue...


Spoofing...

[+] Packets sent: 8^C

Restoring ARP tables and exiting...

```

# Running

> Install python and git
```
Debian / Ubuntu based: $ sudo apt install python3 python3-pip git

Arch based: $ sudo pacman -S python python-pip
```

> Clone git repository
```
git clone https://github.com/compromyse/ArpSpoof_Py
```

> Install script requirements
```
python3 -m pip install -r requirements.txt
```

> Run the script as **root**
```
sudo python3 ArpSpoof.py
```

# Thanks!
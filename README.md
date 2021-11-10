# ArpSpoof_Py
An ARP spoofer written in python. 

<!-- ![image](https://user-images.githubusercontent.com/71056504/119310996-28c04800-bc8e-11eb-89b6-75cf4d89300e.png) -->

```
╭─stagefright@Aspire ~/Projects/ArpSpoof_Py ‹main› 
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
git clone https://github.com/Stagefright071/ArpSpoof_Py
```

> Install script requirements
```
python3 -m pip install -r requirements.txt
```

> Run the script as **root**
```
sudo python3 ArpSpoof.py
```
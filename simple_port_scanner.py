import socket
import sys
import argparse
from termcolor import *
import re
from datetime import datetime


openports = []


def singleportscanner(host,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host,port))
        if result == 0:
            openports.append(port)
    except:
        cprint("Could not connect to " + host + "!","red",attrs=["bold"])
        sys.exit()

def allportscanner(host):
    try:
        for port in range(1,65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host,port))
            if result == 0:
                openports.append(port)
    except:
        cprint("Could not connect to " + host + "!","red",attrs=["bold"])
        sys.exit()

def rangescanner(host,ports):
    try:
        temp = re.findall(r'\d+', ports)
        portz = list(map(int, temp))
        for port in range(portz[0],portz[1]):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host,port))
            if result == 0:
                openports.append(port)
    except:
        cprint("Could not connect to " + host + "!","red",attrs=["bold"])
        sys.exit()

def printascii():
    asciiart = """
 _________________________________________
< Simple_Port_Scanner.py MOOOOO! by @_dr1veby >
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\

                ||     ||
                """
    cprint(asciiart,"blue",attrs=["bold"])


printascii()
parser = argparse.ArgumentParser("Simple Python Port Scanner\n\nExample Syntax: simple_port_scanner.py 192.168.1.1 --allports\n")
group = parser.add_mutually_exclusive_group()
parser.add_argument('host', help="Target")
group.add_argument('--port', help="Scan a single port")
group.add_argument('--range', help="Scan a range of ports. Eg. 0-1024")
group.add_argument('--allports', help="Scan all 65535 ports", action="store_true")
args = parser.parse_args()

host = args.host


ip_validation = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",host)

t1 = datetime.now()

if ip_validation:
    cprint("Please Wait, Scanning Remote Host: " + host, "white",attrs=["bold"])
    if args.allports == True:
        cprint("Scanning for all ports!","yellow",attrs=["bold"])
        allportscanner(host)

    elif args.range is not None:
        ports = args.range
        rangescanner(host,ports)
        cprint("Scanning Target Ports: " + ports,"yellow",attrs=["bold"])

    elif args.port is not None:
        port = args.port
        port_validation = re.match(r"^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$",port)
        port = int(port)
        if port_validation:
            singleportscanner(host,port)
        else:
            cprint("\nPort " + str(port) + " is not a valid network port. Try again using ports between 0-65535\n","red",attrs=["bold"])
            sys.exit()
    else:
        cprint("Could Not Scan Ports!\nPlease Check The Help and Re-Run!","red",attrs=["bold"])
        sys.exit()
else:
    cprint(host + " Appears To Be Invalid! Re-run with a valid IP Address!","red",attrs=["bold"])
    sys.exit()

t2 = datetime.now()
print("\n")
cprint("*" * 30,"yellow",attrs=["bold"])        
cprint("Scanning Summary:","green",attrs=["bold"])        
cprint("*" * 30, "yellow", attrs=["bold"])
total = str(t2 - t1)

if len(openports) != 0:
    for port in openports:
        cprint("Port: " + str(port) + " is open","green",attrs=["bold"])
    cprint("\nScanning time elapsed: " + total + ";\n","cyan",attrs=["bold"])    
else:
    cprint("No open ports found!","red",attrs=["bold"])
    print("\n")


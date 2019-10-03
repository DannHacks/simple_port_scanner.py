# simple_portscanner.py

## Simple Python Portscanner (with colours!)

### Args
```
 _________________________________________
< Simple_Port_Scanner.py MOOOOO! by @_dr1veby >
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/
                ||     ||
                
usage: Simple Python Port Scanner

Example Syntax: simple_port_scanner.py 192.168.1.1 --allports

       [-h] [--port PORT | --range RANGE | --allports] host

positional arguments:
  host           Target

optional arguments:
  -h, --help     show this help message and exit
  --port PORT    Scan a single port
  --range RANGE  Scan a range of ports. Eg. 0-1024
  --allports     Scan all 65535 ports
  ```
### Examples
```
python simple_port_scanner.py --allports 192.168.1.1
python simple_port_scanner.py --range 0-1024 192.168.1.1  
```
### Requirements
  
- termcolor

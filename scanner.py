#!usr/bin/env python

from socket import *
import sys,time
from datetime import datetime

host = ''
min_port = 1
max_port = 6553

port_dict = {
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    115: "SFTP",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    194: "IRC",
    443: "SSL",
    445: "SMB",
    1433: "MSSQL",
    3306: "MySQL",
    3389: "Remote Desktop" ,
    5632: "PCAnywhere",
    5900: "VNC",
    6112: "Warcraft III"
}
try:
    host = raw_input("[*] Enter target host address: ")
except KeyboardInterrupt:
    print("\n\n[*] User interrrupted process")
    print("[*] Shutting down application")
    system.exit(1)

host_ip = gethostbyname(host);

print("\n[*] Host: %s IP: %s" % (host, host_ip))
print("\n[*] Scanning started at: %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

def scan_host(host, port, r_code = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)

        code = s.connect_ex(host, port)

        if code == 0:
            r_code = code
        
        s.close()
    except Exception, e:
        pass
    
    return r_code


for port in range(min_port, max_port):
    try:
        response = scan_host(host, port)
        
        if response == 0:
            print("[*] Port %d [%s] Open" % (port, port_dict[port]))
    except Exception, e:
        pass

stop_time = datetime.now()
print("\n[*] Scanning Finished at %s..." % (time.strftime("%H:%M:%S")))
print("[*] Scanning duration: %s..." % (stop_time - start_time))
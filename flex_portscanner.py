import socket
import threading
import ipaddress
import time
target = ""  
# add default case 
start_port = 1
end_port = 1024


def validate_ip(ip_str):
    try:
        return ipaddress.ip_address(ip_str)
    except ValueError:
        return None
    
if len(sys.argv) < 2:
    print("Usage 1: " + sys.argv[0] + "[1]Target [2]Start Port [3]End Port, if you only provide an IP, this script will default to 1-1024)
    print("Usage 2: " + sys.argv[0] + "[1]Target\n If usiing the default port range is your intention please wait 4 seconds, if not cancel execution now.")
    time.sleep(4)
    
    if len(sys.argv) == 2:
        target = validate_ip(sys.argv[1])
        # add default
        if target_ip is None: 
            print("Invalid IP:",sys.argv[1])
            sys.exit(1)
        else:
            print("Invalid Arguments.")
            sys.exit(1)
    
open_ports = []

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((sys.argv[1], port))
    if result == 0:
        open_ports.append(port)
    sock.close()

def main():
    threads = []
# Grouping the threads into a list
    for port in range(sys.argv[2], sys.argv[3] + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Open ports:", open_ports)

if __name__ == "__main__":
    main()

import socket
import threading

target = ""  
# add default case 
start_port = 1
end_port = 100

if len(sys.argv) < 4:
    print("Usage: " + sys.argv[0] + "[1]Target [2]Start Port [3]End Port)
    sys.exit(1)
#else .. default to first 1028

# ide testing 
#
#
#
#
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

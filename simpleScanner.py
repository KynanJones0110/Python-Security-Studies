import socket

targetIP = input("Enter target IP: ")
targetPort = input("Enter target Port Range (format 1-1024 for example): ")

lowport = int(targetPort.split("-")[0])
highport = int(targetPort.split("-")[1])

print("Scanning Host ", targetIP, "from port ", lowport, "to port", highport)


for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print("*** Port ", targetPort," OPEN ***")
    else:
        print("*** Port ", targetport, " CLOSED ***")
    s.close()
    

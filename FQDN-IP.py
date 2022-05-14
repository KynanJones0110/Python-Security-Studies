import socket
import sys
from csv import reader
from csv import reader

#Name of the output file ( list of IP's etc)
f = open('output.txt','w')

#defining the csv you are reading from, put it in your workspace

fileToRead = input("Enter the name of the file ( including .csv )")
with open(fileToRead, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        #reads from the row 0 only
        hostname = (row[0])

        try:
            ip = socket.gethostbyname(hostname)

            print(ip,",",hostname,",","Successful", file = f)
            #May need to null this ?
        except:
             print(" ",",",hostname,",","Failed", file =f)
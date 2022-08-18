#this is a python file
#SERVER CODE
import os
import socket

host = socket.gethostbyname(socket.gethostname())
# host = your IP address
# provide the above IP address to the client
print("Your IP:",host)
port = 80 
#You may use any port, generally firewalls don't block port 80 as it is the https port

addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind(addr) 

print("Waiting to receive messages...") 

(data, addr) = sock.recvfrom(2048)
data = data.decode('utf-8')
print("USER:",data)
time.sleep(10)
sock.close()

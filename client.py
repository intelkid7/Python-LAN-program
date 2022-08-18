#CLIENT CODE
import os 
import socket 
import time

def program():

    host = getpass.getpass("IP:") 
    # set to IP address of target computer 
    port = 80
    addr = (host, port) 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    data = mys
    data = bytes(data,'utf-8')
    sock.sendto(data, addr)
    print('This window and message will get destroyed in 3 seconds...')
    time.sleep(3)
    sock.close() 
    os._exit(0)

program()
time.sleep(10)

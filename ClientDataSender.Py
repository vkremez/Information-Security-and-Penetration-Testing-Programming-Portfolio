#!/usr/bin/env python

def connector():
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM) #s = socket object
    s.connect(('127.0.0.1',13337)) #connect
    received_string = s.recv(1024) #get what server sends
    s.close() #close the socket
    return received_string

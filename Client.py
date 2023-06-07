# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 23:17:06 2023

@author: ADMIN
"""

import socket
import sys
if __name__=='__main__':
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as e:
        print('Create socket fails')
        print(str(e))
        sys.exit()
    print('Socket create')
    host=input('Enter host: ') #localhost
    port=input('Enter port: ') #9050
    try:
        sk.connect((host,int(port)))
        print('socket connect to %s port %s'%(host,port))
        # sk.shutdown(1)
    except socket.error as e:
        print('Fail to connect to %s port %s'%(host,port))
        print(str(e))
        sys.exit()
    while True:
        # Nhan 1
        data = sk.recv(4096)
        if not data:
            break
        print(data.decode('utf-8'))
        # Gui 2
        sk.send('hello server'.encode('utf-8'))
    sk.close()
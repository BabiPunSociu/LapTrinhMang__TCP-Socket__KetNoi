# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 22:35:43 2023

@author: ADMIN
"""

import socket
import sys
if __name__=='__main__':
    host = 'localhost'
    port=9050
    try:
        sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as e:
        print('Create socket fails')
        print(str(e))
        sys.exit()
    print('Socket create')
    sk.bind((host, port))
    print('socket bind to %s port %s'%(host, port))
    sk.listen(5)
    print('waiting...')
    while True:
        client_sk, client_add=sk.accept()
        print('client address: ', client_add)
        # Gui 1
        client_sk.send('Hello client '.encode('utf-8'))
        # Nhan 2
        data=client_sk.recv(4096)
        if not data:
            break
        print(data.decode('utf-8'))
        client_sk.close()
        break

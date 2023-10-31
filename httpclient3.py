#!/usr/bin/env python3
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 80))
    s.sendall(b'GET / HTTP/1.0\r\n\r\n')
    print(b''.join(iter(lambda: s.recv(1024), b'')).decode('ASCII'))

if __name__ == '__main__':
    main()


import socket
import tqdm
import os
from requests import get


class server:
    def __init__(self):
        self.HOST = "0.0.0.0"
        self.PORT = 25565
        self.BS = 4096
        self.STATUS = False
        self.SEPARATOR = "<SEPARATOR>"
        
    def getip(self):
        ip = get('https://api.ipify.org').text
        return ip
    
    def listen(self):
        
        print("Listening on {}:{}".format(self.getip(), self.PORT))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()
            
            conn, addr = s.accept()
   
            
            
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    
                    if not data:
                        break
                    print("Client Echo: {}".format(data))
                    conn.sendall(data)
            



if __name__ == '__main__':
    host = server()
    host.STATUS = True
    while host.STATUS:
        host.listen()

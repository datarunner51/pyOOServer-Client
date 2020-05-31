import socket

class client:
    def __init__(self, IP = "", PORT = ""):
        self.ip = IP
        self.port = PORT
        self.socket = socket.socket()
    
    def bind(self,IP, PORT):
        self.ip = IP
        self.port = IP
        
    def sendmessage(self,message):
        conn = self.connect()
        with conn:            
            #conn.sendall(b'{}'.format(message))
            conn.sendall(str.encode(message))
            data = conn.recv(1024)
        print("Received: {}".format(str(repr(data))))
        
        
        
        
    def connect(self):
        print("Connecting")
        try:
            socketInstance = socket.create_connection((self.ip,self.port), 5)
        except BaseException as e:
            print("Exception: {}".format(str(e)))
            return
        finally:
            pass
        print("Connection Successful")
        return socketInstance

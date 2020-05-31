class client:
    def __init__(self, IP = "", PORT = ""):
        self.ip = IP
        self.port = PORT
        self.BS = 4096
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
        

        
    def sendfile(self, filename):
        conn = self.connect()
        filesize = os.path.getsize(filename)
        SEPARATOR = "<SEPARATOR>"
        
        #Send information for the file
        conn.send(f"{filename}{SEPARATOR}{filesize}".encode())
        
        
        progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        
        #Openfile in binary
        with open(filename, "rb") as f:
            for _ in progress:
                # read the bytes from the file
                bytes_read = f.read(self.BS)
                if not bytes_read:
                    # file to bytes is done
                    break
                # we use sendall to assure transimission in 
                # busy networks
                conn.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
        # close the socket when complete
        conn.close()
        print("Complete")
        
        
        
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
        

        
        
        
    

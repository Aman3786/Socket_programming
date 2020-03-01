import socket

def Main():
	host= "127.0.0.1"
	port =5000

	s = socket.socket()
	s.bind((host,port))
	
	s.listen(2)
	
	c,add = s.accept()
	print("connection from: "+str(add))
	while True:
		data =c.recv(1024).decode("utf-8")
		if not data:
			break
		print("Received data: ",data)
		data =str(hash(data))
		print("sending: ",data)
		c.send(data.encode('utf-8'))
	c.close()

if __name__ == "__main__":
	Main()

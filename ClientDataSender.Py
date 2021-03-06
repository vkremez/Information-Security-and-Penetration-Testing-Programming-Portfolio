import socket
PORT = 50001
files = {
        "File1": "====================" ,
        "File2": "====================" ,
        "File3": "====================" ,
        }
        
for i in files:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', PORT))
    s.send("SAVE")
    s.send(i)
    s.send(files[i])
    s.close()

for i in files:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', PORT))
    s.send("LOAD")
    s.send(i)
    data = s.recv(1024)
    if files[i] != data:
        print("Failed: %s != %s" % (data, files[i]))
    s.close()
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', PORT))
s.send("LOAD")
s.send("File4")
data = s.recv(1024)
if data != "File Not Found":
    print("Error check failed")
else:
    print("SUCCESS!")
s.close()

import sys, time, socket
from MachineMotion import *
sys.path.append("../..")

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('192.168.127.120', 1234))

homed = False

while true:
	try:
	        time.sleep(0.25)

	        print("Socket is listening...")       
        	server.listen(1)
        	client, addr = server.accept()
	        msg = client.recv(1024)
 		print("Recieved command:", msg.decode('utf-8'))
        
      		if msg.decode('utf-8') == "Home":
            		if not homed:
                		print ("Axis "+ str(axis) +" is going home")
                		homed = mm.emitHome(axis)
                		print("Axis "+ str(axis) +" is at home")
        
            		print("Sending HomeDone")
            		client.send("HomeDone".encode("utf-8"))
    
	except:
    		print("Closing socket due to error")
    		client.close()
    		server.close()

	finally:    
    		print("Finally closing socket due to error")
    		client.close()
    		server.close()
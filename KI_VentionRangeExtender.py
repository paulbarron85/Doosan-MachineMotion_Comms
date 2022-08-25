import sys, time, socket
from MachineMotion import *
sys.path.append("../..")

###### CONFIGURING MACHINEMOTION ######
mm = MachineMotionV2OneDrive()

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('192.168.127.120', 1234))

# Configure actuator
axis = 1

homed = False

while True:
    try:
        time.sleep(0.5)
    
        print("Socket is listening...")       
        server.listen(1)
        client, addr = server.accept()
        msg = client.recv(1024)
        print("Recieved command:", msg.decode('utf-8'))
        
        if msg.decode('utf-8') == "Home":
            
            if not homed:
                # Home the actuator
                print ("Axis "+ str(axis) +" is going home")
                homed = mm.moveToHome(axis)
                mm.waitForMotionCompletion()
                print("Axis "+ str(axis) +" homing routine complete")
        
            print("Sending HomeDone")
            client.send("HomeDone".encode("utf-8"))
        
    except:
        print("Closing socket due to error")
        client.close()
        server.close()

import time
from socket import *

elapsedList = [] # Create an empty list
packetLossCount = 0
pings = 0 # Sequence number of the ping message

# Ping for 10 times
while pings < 10:
    pings += 1
    clientSocket = socket(AF_INET, SOCK_DGRAM) # Creates UDP Client Socket
    clientSocket.settimeout(1) # Wait up to 1 second for reply
    message = 'Ping'
    address = ("127.0.0.1", 20000)

    start = time.time() # Sent time (ms)
    clientSocket.sendto("{:.6f}".format(start), address) # Send ping message
    try:
        data, server = clientSocket.recvfrom(1024) # Takes  buffer size of 1024
        end = time.time() # Received time
        elapsed = end - start # RTT: Time takes from sending to receiving the packet.
        elapsedList.append(elapsed) # Add elapsed (RTT) to the list
        print ('%s %d %f' % (data, pings, elapsed))
    except timeout:
        packetLossCount = packetLossCount + 1
        print ('Request timed out')

print ("minimum:", min(elapsedList))
print ("maximum:", max(elapsedList))
print ("average RTTs:", sum(elapsedList)/len(elapsedList))
print ("Packet loss rate", (packetLossCount * 1.0/10 * 1.0)* 100.0, "%")




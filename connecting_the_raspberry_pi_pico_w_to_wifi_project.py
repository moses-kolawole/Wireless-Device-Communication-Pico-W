import socket
import time
import network

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('mosesphone', '22222223')

while wifi.isconnected() == False:
    print('Waiting for connection . . . ')
    time.sleep(1)

wifiInfo = wifi.ifconfig()
print(wifiInfo)

ServerIP = wifiInfo[0]
ServerPort = 2222
bufferSize = 1024
UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServer.bind((ServerIP, ServerPort))
print('UDP Server Up and Waiting . . .')
while True:
    message,address = UDPServer.recvfrom(bufferSize)
    messageDecoded = message.decode('utf-8')
    print('Message Received: ',messageDecoded, 'FROM: ', address[0])
    dataString = 'Received Your Command: '+messageDecoded
    dataStringEncoded = dataString.encode('utf-8')
    UDPServer.sendto(dataStringEncoded, address)

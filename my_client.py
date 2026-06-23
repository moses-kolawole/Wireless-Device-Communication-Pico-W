import socket
serverAddress = ('10.130.70.111', 2222)
bufferSize = 1024
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    cmd = input('What is your command? ')
    cmdEncoded = cmd.encode('utf-8')
    UDPClient.sendto(cmdEncoded, serverAddress)
    data,address = UDPClient.recvfrom(bufferSize)
    dataDecoded = data.decode('utf-8')
    print('MESSAGE FROM SERVER: ', dataDecoded)
    





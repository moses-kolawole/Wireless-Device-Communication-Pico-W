# Wireless Communication Between Devices Using Raspberry Pi Pico W

## Description

This project demonstrates wireless communication between two devices using a Raspberry Pi Pico W and Wi-Fi networking.

The system consists of a server and a client. The client sends commands wirelessly to the server, and the server receives the commands and sends a response back to the client.

This project introduces important networking concepts used in IoT and embedded systems, including wireless communication, message transmission, and socket programming.

## Components Used

* Raspberry Pi Pico W
* MicroPython
* Wi-Fi Network
* Socket Programming

## project code files

[click here to download the server code](connecting_the_raspberry_pi_pico_w_to_wifi_project.py)


[click here to download the client code](my_client.py)

## Server Code

```python
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
    message, address = UDPServer.recvfrom(bufferSize)
    messageDecoded = message.decode('utf-8')

    print('Message Received: ', messageDecoded, 'FROM: ', address[0])

    dataString = 'Received Your Command: ' + messageDecoded
    dataStringEncoded = dataString.encode('utf-8')

    UDPServer.sendto(dataStringEncoded, address)
```

## Client Code

```python
import socket

serverAddress = ('10.130.70.111', 2222)
bufferSize = 1024

UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    cmd = input('What is your command? ')

    cmdEncoded = cmd.encode('utf-8')

    UDPClient.sendto(cmdEncoded, serverAddress)

    data, address = UDPClient.recvfrom(bufferSize)

    dataDecoded = data.decode('utf-8')

    print('MESSAGE FROM SERVER: ', dataDecoded)
```

## How It Works

1. The Raspberry Pi Pico W connects to a Wi-Fi network.
2. The server starts and waits for incoming messages.
3. The client sends a command to the server.
4. The server receives and processes the command.
5. The server sends a response back to the client.
6. The client receives and displays the response.

## Skills Learned

* Wi-Fi networking with Raspberry Pi Pico W
* Wireless device communication
* Socket programming
* Sending and receiving data
* Data encoding and decoding
* Client-server communication
* IoT networking fundamentals

## Future Improvements

* Control LEDs wirelessly
* Add support for multiple devices
* Send sensor data between devices
* Create a wireless monitoring system
* Add security and authentication features

## Author

Moses Olorunfemi Kolawole

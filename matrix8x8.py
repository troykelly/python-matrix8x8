#!/usr/bin/env python3

import socket
import os
import time

HOST = '10.7.3.220'  # Standard loopback interface address (localhost)
PORT = 8000        # Port to listen on (non-privileged ports are > 1023)
MESSAGESIZE = 12    # How many bytes in a message
TEMPLATE = bytearray([165, 91, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# keep track of connection status
connected = True
print("connected to server")


def calc_checksum(s):
    """
    Calculates checksum for sending commands to the Matrix.
    Sums the ASCII character values mod256 and returns
    the lower byte of the two's complement of that value.
    """
    return '%2X' % (-(sum(ord(c) for c in "".join(map(chr, s))) % 256) & 0xFF)


def send(data):
    data.append(int(calc_checksum(data), 16))
    print('Sending', repr(data))
    try:
        s.sendall(data)
        time.sleep(0.5)
        return
    except socket.error:
        connected = False
        print('Connection lost. Reconnecting...')
        while not connected:
            try:
                s.connect((HOST, PORT))
                connected = True
                print('Reconnected')
            except socket.error:
                time.sleep(2)


def reboot():
    cmd = TEMPLATE[:]
    cmd[2] = 8
    cmd[3] = 13
    return send(cmd)


def factoryReset():
    cmd = TEMPLATE[:]
    cmd[2] = 8
    cmd[3] = 10
    return send(cmd)


def powerOff():
    cmd = TEMPLATE[:]
    cmd[2] = 8
    cmd[3] = 11
    cmd[4] = 240
    cmd[6] = 240
    return send(cmd)


def powerOn():
    cmd = TEMPLATE[:]
    cmd[2] = 8
    cmd[3] = 11
    cmd[4] = 15
    cmd[6] = 15
    return send(cmd)


def reqInput(output):
    cmd = TEMPLATE[:]
    cmd[2] = 2
    cmd[3] = 1
    cmd[4] = output
    return send(cmd)


def setInput(outDevice, inDevice):
    cmd = TEMPLATE[:]
    cmd[2] = 2
    cmd[3] = 3
    cmd[4] = inDevice
    cmd[6] = outDevice
    return send(cmd)


def setEdid(inDevice, edid):
    #	1080p,Stereo Audio 2.0 = 1
    #	1080p,Dolby/DTS 5.1 = 2
    #	1080p,HD Audio 7.1 = 3
    #	1080i,Stereo Audio 2.0 = 4
    #	1080i,Dolby/DTS 5.1 = 5
    #	1080i,HD Audio 7.1 = 6
    #	3D,Stereo Audio 2.0 = 7
    #	3D,Dolby/DTS 5.1 = 8
    #	3D,HD Audio 7.1 = 9
    #	4K2K30,Stereo Audio 2.0 = 10
    #	4K2K30,Dolby/DTS 5.1 = 11
    #	4K2K30,HD Audio 7.1 = 12
    #	4K2K60,Stereo Audio 2.0 = 13
    #	4K2K60,Dolby/DTS 5.1 = 14
    #	4K2K60,HD Audio 7.1 = 15
    cmd = TEMPLATE[:]
    cmd[2] = 3
    cmd[3] = 2
    cmd[4] = edid
    cmd[6] = inDevice
    return send(cmd)


pid = os.fork()

if pid > 0:
    while True:
        buf = s.recv(1024)
        print('Received', repr(buf))

reqInput(8)
setInput(8, 8)
reqInput(1)
reqInput(2)
exit()

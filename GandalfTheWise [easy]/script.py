from pwn import xor
import base64

b64_text1 = "xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p"
b64_text2 = "h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU"

# Decoding from base64
text1 = base64.b64decode(b64_text1)
text2 = base64.b64decode(b64_text2)

# xor
output = xor(text1, text2)
flag = output.decode() # get the strings from bytes
print(flag)

with open('flag.txt', 'w') as f:
	f.write(flag)

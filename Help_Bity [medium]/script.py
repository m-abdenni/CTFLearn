from pwn import xor

s = b"BUGMd`sozc0o`sx^0r^`vdr1ld|"
key = bytes.fromhex('01')

flag = ""

for i in s:
	flag += xor(key, i).decode()

print(flag) 
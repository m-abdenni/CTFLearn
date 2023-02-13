# Help Bity

## Description

* Bity had the flag for his problem. Unfortunately, his negative friend Noty corrupted it. Help Bity retrieve his flag. He only remembers the first 4 characters of the flag: `CTFL`. 
* Flag: BUGMd\`sozc0o\`sx^0r^\`vdr1ld|

> Note: the original encoded flag is missing some '\`', so i added them to make the decryption more easier

## Solution

1. Researching around, we get the idea that the flag is `xor`ed by some key, so first thing first let's find the key
2. Since we know that the flag is starting with 'C', we'll `xor` the first letter of the encoded flag 'B' along with 'C' to get the key

```py
from pwn import xor

print(xor(b'C', b'B'))

# b'\x01'
```

3. Now that we have the key, we can use a script to do the rest for us

* Flag:

```
CTFLearn{b1nary_1s_awes0me}
```
# Simple Steganography

## Description

* Think the flag is somewhere in there. Would you help me find it? hint-" Steghide Might be Helpfull"
* [Attachement](https://ctflearn.com/challenge/download/894)

## Solution

1. Using `exiftool`, we find what it seems like a password in the _keyword_ section

![password.png](password.png)

2. Using `steghide` with the password that we found using `exiftool`, we get a new file extracted from the image

```bash
# Extract file from the image
steghide extract -sf Minions1.jpeg
# Read the content of the extracted file
cat raw.txt
```

3. Using `base64` to decode the content of `raw.txt`, and get the flag

```bash
cat raw.txt | base64 -d
```

* Flag:

```
CTFlearn{this_is_fun}
```
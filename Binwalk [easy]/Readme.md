# Binwalk

## Description

* Here is a file with another file hidden inside it. Can you extract it?
* [Attachement](https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY)

## Solution

1. As the name suggested, we use `binwalk` to extract what is inside the image

```bash
binwalk --dd=".*" PurpleThing.jpeg
```

2. Inside the directory output of the `binwalk` command, we have 2 images, one of them has the flag written on it
3. We can use `tessaract` command to get the text inside the image

```bash
# Syntax: tesseract <input file> <output file>
tessaract 25795 flag

# Read the flag
cat flag.txt
```

* Flag

```
ABCTF{b1nw4lk_is_us3ful}
```
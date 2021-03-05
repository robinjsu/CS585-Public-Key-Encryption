import os
import constant as c

def readFile(file):
    plainText = b''
    with open(file, 'rb') as f:
        block = f.read(c.BLOCK_SIZE_BYTES)
        while block != b'':
            plainText += block
            block = f.read(c.BLOCK_SIZE_BYTES)
    return plainText 

if __name__ == "__main__":
    print(readFile("ptext.txt"))
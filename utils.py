import os
import constant as c
import math

def make_x_bits(num, x):
    if num // pow(2, (x-1)) <= 0:
        return num + pow(2,(x-1))
    return num


def read_file(file):
    plainText = b''
    with open(file, 'rb') as f:
        block = f.read(c.BLOCK_SIZE_BYTES)
        while block != b'':
            plainText += block
            block = f.read(c.BLOCK_SIZE_BYTES)
    print(plainText)
    return plainText 

def get_blocks(filebytes):
    index = 0
    end = len(filebytes)
    blocks = []
    while index < end:
        if end - index < c.BLOCK_SIZE_BYTES:
            blk = filebytes[index::]
            blocks.append(int(blk.hex(), 16))
        else:
            blk = filebytes[index:index+c.BLOCK_SIZE_BYTES]
            blocks.append(int(blk.hex(), 16))
        index += c.BLOCK_SIZE_BYTES      
    print(f"message blocks: {blocks}")
    return blocks

# if __name__ == "__main__":
#     get_blocks(b'Hello there!')
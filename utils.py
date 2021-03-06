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
    return plainText 

def read_cipher_text(filename):
    blocks = []
    with open(filename) as f:
        block = f.readline()
        while block != '':
            ctexts = block[:-1].split(' ')
            blocks.append(ctexts)
            block = f.readline()
    return blocks

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
    return blocks

def check_key_file(filename):
    with open(filename) as f:
        contents = f.readline()
        if contents == '':
            return None
        return contents.split(' ')

def write_ciphertxt_to_file(cipher_tuples, filename):
    with open(filename, 'w') as f:
        for ctuple in cipher_tuples:
            f.write(f"{ctuple[0]} {ctuple[1]}\n")
        f.close()

def write_plaintxt_to_file(plaintext, filename):
    with open(filename, 'w') as f:
        f.write(plaintext)
        f.close()

def int_to_ascii(blocks):
    hex_string = ""
    hex_encoding = []
    for b in blocks:
        hex_encoding.append(hex(b))
    for h in hex_encoding:
        hex_string += h[2::]
    plainBytes = bytes.fromhex(hex_string)
    plain_ascii = plainBytes.decode()
    return plain_ascii



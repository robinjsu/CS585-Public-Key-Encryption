## CS585 CRYPTOGRAPHY Project 2
### Robin Su
### robisu@pdx.edu

## Description
This code implements a public key cryptosystem. It uses a 33-bit key to encrypt 32-bit blocks of text.

There are three modes to this program: key generation, encryption and decryption. It must be run in key generation mode first before any files can be encrypted or decrypted.

**For key generation mode**: using '--keygen' as a command line flag, it outputs
the public key (p,g,e_2) and private key (p, g, d) into two separate files, named 'pubkey.txt' and 'prikey.txt', 
respectively.

**For encryption mode**: input is a plaintext file ('ptext.txt'), encoded as ASCII/Unicode (UTF-8), and the public key file ('pubkey.txt'); output of encrypted message blocks are written to a file named 'ctext.txt'.

**For decryption mode**: input is the ciphertext file, 'ctext.txt', where each pair of ciphertext, (C1,C2), is written to a separate line; output of plaintext is written to a file named 'ptext-out.txt'.

## Running the Program

Key Generation:
```
python3 public_key.py --keygen
```

Encryption Mode:
```
python3 public_key.py -f ptext.txt -k pubkey.txt --encrypt
```

Decryption Mode:
```
python3 public_key.py -f ctext.txt -k prikey.txt --decrypt

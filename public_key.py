import argparse as ap
import keygen as kg
import constant as c
import utils
import secrets
 
CIPHER_TEXT_FILE = "ctext.txt"
PLAIN_TEXT_FILE = "ptext.txt"

def parse_args():
    parser = ap.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="Name of file to encrypt/decrypt")
    parser.add_argument("-p", "--pubkey", type=str,\
        help="Name of file containing public key elements (default filename: 'pubkey.txt')")
    parser.add_argument("--keygen", action='store_true', help="Run program in key generation mode")
    parser.add_argument("-e", "--encrypt", action='store_true', help="(optional) run program in encryption mode")
    parser.add_argument("-d", "--decrypt", action='store_true', help="(optional) run program in decryption mode")
    args = parser.parse_args()
    return args.file, args.pubkey, args.keygen, args.encrypt, args.decrypt

def check_key_file(filename):
    with open(filename) as f:
        contents = f.readline()
        if contents == '':
            return None
        return contents.split(' ')

def write_to_file(cipher_tuples):
    with open(CIPHER_TEXT_FILE, 'w') as f:
        for ctuple in cipher_tuples:
            f.write(f"{ctuple[0]} {ctuple[1]}\n")
        f.close()

def read_cipher_text(filename):
    blocks = []
    with open(filename) as f:
        block = f.readline()
        while block != '':
            ctexts = block[:-1].split(' ')
            blocks.append(ctexts)
            block = f.readline()
    return blocks

# C1 = g^k mod p
# C2 = e2^k∙m mod p
def encrypt_text(file, pub_keys):
    filebytes = utils.read_file(file)
    blocks = utils.get_blocks(filebytes)
    cipher_text = []
    p = int(pub_keys[0], 10)
    print(f"p: {p}")
    g = int(pub_keys[1], 10)
    print(f"g: {g}")
    e2 = int(pub_keys[2], 10)
    print(f"e2: {e2}")
    c1 = 0
    c2 = 0
    for b in blocks:
        k = secrets.randbelow(p-1)
        c1 = pow(g, k, p)
        c2 = pow(e2, k, p)
        c2 = (c2 * b) % p
        cipher_text.append(tuple([c1, c2]))
    print(f"cipher text blocks: {cipher_text}")
    return cipher_text

# ((C1^{p-1-d} mod p)(C2 mod p)) mod p = m
def decrypt_text(file, privkeys):
    plain_text = []
    ctext_pairs = read_cipher_text(file)
    p = int(privkeys[0])
    print(f"p: {p}")
    d = int(privkeys[2])
    print(f"d: {d}")
    exp = p - 1 - d
    for c in ctext_pairs:
        print(f"c1, c2: {c[0]}, {c[1]}")
        c1 = int(c[0])
        c2 = int(c[1]) % p
        c1 = pow(c1, exp, p)
        m = (c1 * c2) % p
        plain_text.append(m)
    print(f"plaintext: {plain_text}")
    return plain_text

def main():
    file, pubkey, keygen, encrypt, decrypt = parse_args()
    if keygen == True:
        kg.generate_key_files()
    elif encrypt == True:
        pub_keys = check_key_file(pubkey)
        if pub_keys == None:
            raise Exception(c.PUB_KEY_ERROR)
        cipher_text = encrypt_text(file, pub_keys)
        write_to_file(cipher_text)
    elif decrypt == True:
        pri_key = check_key_file("prikey.txt")
        if pri_key == None:
            raise Exception(c.PRI_KEY_ERROR)
        plain_text = decrypt_text(CIPHER_TEXT_FILE, pri_key)

if __name__ == "__main__":
    main()
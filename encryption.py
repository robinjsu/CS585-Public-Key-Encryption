import utils
import secrets
import constant as c

# C1 = g^k mod p
# C2 = e2^k∙m mod p
def encrypt_text(file, pub_keys):
    filebytes = utils.read_file(file)
    blocks = utils.get_blocks(filebytes)
    cipher_text = []
    p = int(pub_keys[0], 10)
    # print(f"p: {p}")
    g = int(pub_keys[1], 10)
    # print(f"g: {g}")
    e2 = int(pub_keys[2], 10)
    # print(f"e2: {e2}")
    c1 = 0
    c2 = 0
    for b in blocks:
        k = secrets.randbelow(p-1)
        c1 = pow(g, k, p)
        c2 = pow(e2, k, p)
        c2 = (c2 * b) % p
        cipher_text.append(tuple([c1, c2]))
    # print(f"cipher text blocks: {cipher_text}")
    return cipher_text

    # ((C1^{p-1-d} mod p)(C2 mod p)) mod p = m
def decrypt_text(file, privkeys):
    plain_text = []
    ctext_pairs = utils.read_cipher_text(file)
    p = int(privkeys[0])
    d = int(privkeys[2])
    exp = p - 1 - d
    for c in ctext_pairs:
        c1 = int(c[0])
        c2 = int(c[1]) % p
        c1 = pow(c1, exp, p)
        m = (c1 * c2) % p
        plain_text.append(m)
    return plain_text
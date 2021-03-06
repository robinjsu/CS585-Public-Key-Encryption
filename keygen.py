import utils
import constant as c
import prime_test as prime
import secrets

def find_q_val(q):
    while True:
        if prime.miller_rabin(q) == True and (q % 12 == 5):
            return q
        q = utils.make_x_bits(secrets.randbits(c.Q_SIZE_BITS), c.Q_SIZE_BITS)


def keygen():
    q, p, d, e2 = 0, 0, 0, 0
    e1 = 2
    while True:
        q = utils.make_x_bits(secrets.randbits(c.Q_SIZE_BITS), c.Q_SIZE_BITS)
        # find k-1 bit prime
        q = find_q_val(q)  
        p = (2 * q) + 1
        if prime.miller_rabin(p) == True:
            d = secrets.randbelow(p-2) + 1
            e2 = pow(2, d, p)
            return tuple([p,e1,e2]), tuple([p,e1,d])

def generate_key_files():
    pubkey, privkey = keygen()

    with open("pubkey.txt", "w") as file:
        file.write(f"{pubkey[0]} {pubkey[1]} {pubkey[2]}")
        file.close()

    with open("prikey.txt", "w") as file:
        file.write(f"{privkey[0]} {privkey[1]} {privkey[2]}")
        file.close()


if __name__ == "__main__":
    generate_key_files()
    
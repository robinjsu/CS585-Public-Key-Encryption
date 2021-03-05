import constant as c
import prime_test as prime
import secrets

def find_q_val(q):
    print(f"checking q ({q})...")
    while True:
        if prime.miller_rabin(q) == True and (q % 12 == 5):
            return q
        q = secrets.randbits(c.Q_SIZE_BITS)

        
def keygen():
    q, p, d, e2 = 0, 0, 0, 0
    e1 = 2
    # print("generating p...")
    while True:
        q = secrets.randbits(c.Q_SIZE_BITS)
        # find a k-1 bit prime
        q = find_q_val(q)  
        p = (2 * q) + 1
        if prime.miller_rabin(p) == True:
            print(f"found valid p: {p}")
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
    
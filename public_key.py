import argparse as ap
import keygen as kg
import constant as c
import utils
import encryption as enc


def parse_args():
    parser = ap.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="Name of file to encrypt/decrypt")
    parser.add_argument("-k", "--key", type=str,\
        help="Name of file containing public key (for encryption) or private key (for decryption) elements") 
    parser.add_argument("--keygen", action='store_true', help="run program in key generation mode")
    parser.add_argument("-e", "--encrypt", action='store_true', help="(optional) run program in encryption mode")
    parser.add_argument("-d", "--decrypt", action='store_true', help="(optional) run program in decryption mode")
    args = parser.parse_args()
    return args.file, args.key, args.keygen, args.encrypt, args.decrypt

def main():
    file, key, keygen, encrypt, decrypt = parse_args()
    if keygen == True:
        kg.generate_key_files()

    elif encrypt == True:
        pub_keys = utils.check_key_file(key)
        if pub_keys == None:
            raise Exception(c.PUB_KEY_ERROR)
        cipher_text = enc.encrypt_text(file, pub_keys)
        utils.write_ciphertxt_to_file(cipher_text, c.CIPHER_TEXT_FILE)

    elif decrypt == True:
        pri_key = utils.check_key_file(key)
        if pri_key == None:
            raise Exception(c.PRI_KEY_ERROR)
        plain_ints = enc.decrypt_text(c.CIPHER_TEXT_FILE, pri_key)
        final_plaintext = utils.int_to_ascii(plain_ints)
        print(f"Decryption Output: {final_plaintext}")
        utils.write_plaintxt_to_file(final_plaintext, c.DECRYPTION_OUTPUT_FILE)

    return 0

if __name__ == "__main__":
    main()
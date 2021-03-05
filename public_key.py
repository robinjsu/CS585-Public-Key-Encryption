import argparse as ap

def parseArgs():
    parser = ap.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, help="Name of file to encrypt/decrypt")
    parser.add_argument("-p", "--pubkey", type=str,\
        help="Name of file containing public key elements (default filename: 'pubkey.txt')")
    parser.add_argument("--keygen", action='store_true', help="Run program in key generation mode")
    parser.add_argument("-d", "--decrypt", action='store_true', help="(optional) run program in decryption mode")
    args = parser.parse_args()
    return args.file, args.pubkey, args.keygen, args.decrypt

def main():
    f, p, k, d = parseArgs()

if __name__ == "__main__":
    main()
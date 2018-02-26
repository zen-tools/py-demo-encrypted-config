#!/usr/bin/env python

import os
import argparse

from Crypto.PublicKey import RSA


def generate_rsa_key(key_password):
    key = RSA.generate(2048)
    return key.exportKey('PEM', key_password)


if __name__ == '__main__':
    def parse_args():
        parser = argparse.ArgumentParser(
            formatter_class=lambda prog: argparse.HelpFormatter(
                prog, max_help_position=40))
        parser.add_argument(
            "-k", "--key-file", help="path to new mykey.pem", required=True,
            type=str, metavar="mykey.pem")
        parser.add_argument(
            "-p", "--password", help="password for mykey.pem", required=False,
            type=str, metavar="12345", default="")
        return parser, parser.parse_args()

    try:
        parser, args = parse_args()
        if os.path.exists(args.key_file):
            raise IOError("%s already exists" % args.key_file)
        rsa_key = generate_rsa_key(args.password)
        with open(args.key_file, 'w') as f:
            f.write(rsa_key)
    except KeyboardInterrupt:
        pass

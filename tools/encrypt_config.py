#!/usr/bin/env python

import os
import argparse

from ConfigParser import ConfigParser

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def main(args):
    if not os.path.exists(args.source):
        raise IOError("%s file is not exist" % args.source)

    if os.path.exists(args.output):
        raise IOError("%s file is exist" % args.output)

    p_key = None
    with open(args.key_file) as f:
        p_key = PKCS1_OAEP.new(RSA.importKey(f.read(), args.password))

    enc_config = ConfigParser()
    enc_config.add_section('main')
    enc_config.set('main', 'private_key', args.key_file)

    config = ConfigParser()
    config.read(args.source)
    for section in config.sections():
        if section != 'main':
            enc_config.add_section(section)
        for (key, val) in config.items(section):
            enc_config.set(section, key, p_key.encrypt(val).encode('base64'))

    with open(args.output, 'w') as f:
        enc_config.write(f)


if __name__ == '__main__':
    def parse_args():
        parser = argparse.ArgumentParser(
            formatter_class=lambda prog: argparse.HelpFormatter(
                prog, max_help_position=40))
        parser.add_argument(
            "-s", "--source", help="source file", required=True,
            type=str, metavar="config.ini")
        parser.add_argument(
            "-o", "--output", help="output file", required=True,
            type=str, metavar="config-protected.ini")
        parser.add_argument(
            "-k", "--key-file", help="path to new mykey.pem", required=True,
            type=str, metavar="mykey.pem")
        parser.add_argument(
            "-p", "--password", help="password for mykey.pem", required=False,
            type=str, metavar="12345", default="")
        return parser, parser.parse_args()

    try:
        parser, args = parse_args()
        main(args)
    except KeyboardInterrupt:
        pass

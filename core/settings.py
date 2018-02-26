import sys
from getpass import getpass
from ConfigParser import (
    ConfigParser,
    Error as ConfigParserError
)
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

_p_key = None
_config_instance = None


class settings:
    @staticmethod
    def init(config_file):
        config = ConfigParser()
        config.read(config_file)

        global _config_instance, _p_key
        _config_instance = config

        key = ''
        try:
            key = _config_instance.get('main', 'private_key')
        except ConfigParserError:
            pass

        if key and 'ENCRYPTED' in key:
            if sys.stdin.isatty():
                password = getpass("Enter password: ")
                _p_key = PKCS1_OAEP.new(RSA.importKey(key, password))
            else:
                raise Exception("Can't open stdin to read cert password.")
        elif key:
            _p_key = PKCS1_OAEP.new(RSA.importKey(key))

    @staticmethod
    def get(section, key):
        global _p_key
        if not _config_instance:
            raise Exception("Must call settings.init('/path/to/config.ini')")

        value = _config_instance.get(section, key)

        if (section, key) == ('main', 'private_key'):
            return value

        if _p_key:
            return _p_key.decrypt(value.decode('base64'))

        return value

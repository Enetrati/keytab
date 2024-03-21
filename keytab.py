#!/usr/bin/env python

import sys
from pathlib import Path
from os.path import isfile, join
from cryptography.fernet import Fernet
#from cryptography.hazmat.primitives import hashes

class KeyTabException(Exception):
    def __init__(self, message):
        super(). __init__(message)

class KeyTab:
    def __init(
            self,
            keytab_dir=None,
            keytab_key = None,
            keytab_file = None,
            text = None
        ):
        self.keytab_dir = Path(keytab_dir)
        self.keytab_key = join(self.keytab_dir, "key")
        self.keytab_file = join(self.keytab_dir, "keytab")
        self.keytab_key_hash = None
        self.text = text

    def initialize(self):
        try:
            if not self.keytab_dir.is_dir()
                os.mkdir(self.keytab_dir)

            if not isfile(self.keytab_key_file):
                self.keytab_key_hash = Fernet.generate_key()

            with open(keytab_key_file, "wb") as key_file:
                key_file.write(keytab_key_hash)
            return True
        except OSError as ose:
            print("Cannot create: ", ose)
            return False

    def get_key(self):
        with open(keytab_key_file, "rb") as key_file:
            self.keytab_key_hash = key_file.read()

    def decrypt(self):
        if not self.keytab_dir.is_dir() and not isfile(self.keytab_key_file):
            print("There is nothing set. Initialize first")
            return None

        self.get_key(self.keytab_key_file)
        cipher_suite = Fernet(self.keytab_key_hash)

        with open(self.keytab_file, "rb") as keytab:
            self.text = keytab.read()

        return cipher_suite.decrypt(self.text)


    def encrypt(self):
        if not isfile(self.keytab_key_file):
            print("There is nothing set. Initializing")
            self.initialize()


        cipher_suite = Fernet(self.keytab_key_hash)
        data = bytes(password, 'ascii')
        cipher_text = cipher_suite.encrypt(data)

        with open(fernet_key_tab, "wb") as key_tab:
            key_tab.write(cipher_text)
        return True


if __name__ == '__main__':
    main()

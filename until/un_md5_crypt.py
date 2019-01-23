#encoding=utf-8
import hashlib
import crypt

import sys

class un_md5_crypt:
    def run_ep(self, password, salt):
        pw = crypt.crypt(password,salt)
        print(pw)


if __name__ == '__main__':
    pass
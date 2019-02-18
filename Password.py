import random
import string
import hashlib


class Password:

    @staticmethod
    def asd(pb_hash):
        while True:
            key = ''.join([random.choice(string.ascii_letters + string.digits + "@" + "_" + "!" + "#" + "$" + "%" + "^" + "&" + "*" + "(" + ")" + "<" + ">" + "?" + "/" + '|' + '}' + '{' + '~' + ':')for n in range(2, 6, 2)])
            print(key)
            hash_key = hashlib.sha1(key.encode('utf-8'))
            pb_hash_key = hash_key.hexdigest()
            print(pb_hash_key)
            if pb_hash_key == pb_hash:
                return key


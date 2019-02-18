import hashlib
from Password import Password


def main():
    password = input("Password: ")
    hash_object = hashlib.sha1(password.encode('utf-8'))
    pb_hash = hash_object.hexdigest()
    print(pb_hash)
    a1 = Password()
    print(a1.asd(pb_hash))


if __name__ == '__main__':
    main()

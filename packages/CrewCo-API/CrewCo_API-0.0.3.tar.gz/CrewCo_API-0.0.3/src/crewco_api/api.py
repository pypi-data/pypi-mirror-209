import base64
from base64 import b64encode
from Crypto.Cipher import AES
import json


def to_b64_padded(plaintext, block_size):
    plaintext_bytes = plaintext.encode('utf-8')
    plaintext_b64 = b64encode(plaintext_bytes).decode('utf-8')
    padding = (block_size - len(plaintext_b64) % block_size) * chr(block_size - len(plaintext_b64) % block_size)
    return plaintext_b64 + padding


def un_pad(data):
    pad = data[-1]
    if data[-pad:] == bytes([pad]) * pad:
        return data[:-pad]
    return data


class API:
    def __init__(self):
        self.filename = "NodeList.json"
        self.data = {}
        self.load()
        self.key = key = "867e685b3ffd0b70".encode('utf-8')
        if len(self.key) != 16:
            print("Key must be 16 charters long")
            exit()
        else:
            self.key = key
            self.iv = key

    def encrypt(self, message):
        plaintext = message
        padded_plaintext = to_b64_padded(plaintext, AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ciphertext_bytes = cipher.encrypt(padded_plaintext.encode('utf-8'))
        ciphertext_b64 = b64encode(ciphertext_bytes).decode('utf-8')
        return ciphertext_b64.encode('utf-8')

    # Decryption
    def decrypt(self, message):
        # Decryption
        decipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        ciphertext = base64.b64decode(message)
        plaintext_b64padded = decipher.decrypt(ciphertext)
        plaintext_b64 = un_pad(plaintext_b64padded)
        plaintext = base64.b64decode(plaintext_b64).decode("utf-8")
        return plaintext

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def lookup(self, name):
        return self.data.get(name)

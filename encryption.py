import random
import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

class Encryption:
    def __init__(self):
        self.PASS_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    
    def get_salt(self, len=8) -> bytearray:
        salt = bytearray()
        for _ in range(len):
            salt.append(random.randint(0, 255))
        return salt

    def gen_password(self, len=9) -> bytearray:
        pw = bytearray()
        for _ in range(len):
            pw.append(ord(random.choice(self.PASS_CHARS)))
        return pw

    def SSLKey(self, pw_bytes: bytearray, salt: bytearray) -> dict:
        pw = pw_bytes + salt
        res = hashlib.md5(pw).digest()
        temp_hash = res
        for _ in range(2):
            temp_hash = hashlib.md5(temp_hash + pw).digest()
            res += temp_hash
        return {'key': res[0:4*8],
        'iv': res[4*8:4*8+16]}

    def encrypt(self, text: str, password: bytearray) -> bytes:
        salt = self.get_salt()
        s_block = b'Salted__' + salt
        gen_ssl = self.SSLKey(password, salt)
        key, iv = gen_ssl['key'], gen_ssl['iv']
        cipher = AES.new(key, AES.MODE_CBC, iv, use_aesni=True)
        cipher_bl = cipher.encrypt(pad(text.encode(), cipher.block_size))
        cipher_bl = s_block + cipher_bl
        return base64.b64encode(cipher_bl)       
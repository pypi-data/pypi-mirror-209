from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_v1_5
from nacl.public import PublicKey, SealedBox
from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from typing import Union
from uuid import UUID
import base64
import datetime
import struct
import io
import time
import datetime
import random
import string
import binascii


class A():
    def __init__(self):
        self.defkey1 = ''
        self.pkey1 = ''
        self.defkey2 = ''
        self.pkey2 = ''

    def _encpw(self, id: str, key: str, password: str) -> str:
        rand_key = get_random_bytes(32)
        iv = get_random_bytes(12)
        pubkey_bytes = base64.b64decode(key)
        pubkey = RSA.import_key(pubkey_bytes)
        cipher_rsa = PKCS1_v1_5.new(pubkey)
        encrypted_rand_key = cipher_rsa.encrypt(rand_key)
        cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
        current_time = int(time.time())
        cipher_aes.update(str(current_time).encode("utf-8"))
        encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(
            password.encode("utf-8"))
        buf = io.BytesIO()
        buf.write(bytes([1, int(id)]))
        buf.write(iv)
        buf.write(struct.pack("<h", len(encrypted_rand_key)))
        buf.write(encrypted_rand_key)
        buf.write(auth_tag)
        buf.write(encrypted_passwd)
        encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
        return f"#PWD_INSTAGRAM:4:{current_time}:{encoded}"

    def _encpwd(self, key_id, pub_key, password, version=10):
        key = Random.get_random_bytes(32)
        iv = bytes([0] * 12)
        time = int(datetime.datetime.now().timestamp())
        aes = AES.new(key, AES.MODE_GCM, nonce=iv, mac_len=16)
        aes.update(str(time).encode('utf-8'))
        encrypted_password, cipher_tag = aes.encrypt_and_digest(
            password.encode('utf-8'))
        pub_key_bytes = binascii.unhexlify(pub_key)
        seal_box = SealedBox(PublicKey(pub_key_bytes))
        encrypted_key = seal_box.encrypt(key)
        encrypted = bytes([1,
                           key_id,
                           *list(struct.pack('<h', len(encrypted_key))),
                           *list(encrypted_key),
                           *list(cipher_tag),
                           *list(encrypted_password)])
        encrypted = base64.b64encode(encrypted).decode('utf-8')
        return f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}'

    def _encbsc(self,  pw) -> None:
        time = int(datetime.datetime.now().timestamp())
        return f'#PWD_INSTAGRAM:0:{time}:{[pw]}'

    def _generate(self, seed: Union[str, bytes]) -> None:
        rand = random.Random(seed + str(datetime.date.today()))
        phone_id = str(UUID(int=rand.getrandbits(128), version=4))
        adid = str(UUID(int=rand.getrandbits(128), version=4))
        id = f"android-{''.join(rand.choices(string.hexdigits, k=16))}".lower()
        _uuid = str(UUID(int=rand.getrandbits(128), version=4))
        fdid = str(UUID(int=rand.getrandbits(128), version=4))
        jazoest = self._jazoest(phone_id)
        _sessid = f'UFS-{UUID(int=rand.getrandbits(128))}-0'
        _time = str(round(time.time(), 3))
        return _sessid, _time, id, phone_id, adid, _uuid, fdid, jazoest

    def _jazoest(self, phone_id) -> str:
        return f"2{sum(ord(i) for i in phone_id)}"

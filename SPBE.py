# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 13:31:26 2020

@author: jaspe
"""

#Password Based Symetrical Encryptor/Decryptor

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def key_gen(password, salt):
    pass_bits = password.encode()
    salt_bits = salt.encode()
    kdf = PBKDF2HMAC(
            algorithm=hashes.MD5(),
            length = 32,
            salt = salt_bits,
            iterations = 100,
            backend = default_backend()
            )
    key = base64.urlsafe_b64encode(kdf.derive(pass_bits))
    return key
    
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def MD5_HashEncryption(data):
    return hashlib.md5(data.encode()).hexdigest()

def SHA256_HashEncryption(data):
    return hashlib.sha256(data.encode()).hexdigest()

def AES_Encrypt(data, key):
    cipher = AES.new(bytes.fromhex(key), AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(bytes.fromhex(data), AES.block_size))
    return encrypted.hex()

PASS = 'Your PASSWORD' # Enter your password
VV1 = 'VV1 Output' # Taking from Restful API
VV2 = 'VV2 Output' # Taking from Restful API

password_md5 = MD5_HashEncryption(PASS) # Convert your password to MD5
first_sha256 = SHA256_HashEncryption(password_md5 + VV1) # MD5 and VV1 String Together Encrypting with Sha256.
password_key = SHA256_HashEncryption(first_sha256 + VV2) # MD5 and VV2 String Together Encrypting with Sha256.

encrypted_password = AES_Encrypt(password_md5, password_key) # Using AES-ECB-NoPadding Method And Encrypting.

print(encrypted_password[:32]) # Taking first 32 characters of the encrypted password. (16 Bytes Output.)

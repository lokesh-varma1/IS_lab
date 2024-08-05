from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
import binascii
import time

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    # Pad the plaintext to be a multiple of DES block size
    padded_data = pad(plaintext, DES.block_size)
    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    # Decrypt the ciphertext
    decrypted_padded_data = cipher.decrypt(ciphertext)
    # Unpad the decrypted data
    decrypted_data = unpad(decrypted_padded_data, DES.block_size)
    return decrypted_data

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
 
    padded_data = pad(plaintext, AES.block_size)
  
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def aes_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
   
    decrypted_padded_data = cipher.decrypt(ciphertext)
    
    decrypted_data = unpad(decrypted_padded_data, AES.block_size)
    return decrypted_data

def measure_time(cipher_func, key, plaintext):
    if (cipher_func == "DES"):
        start_time = time.time()
        encrypted_data = des_encrypt(key, plaintext)
        end_time = time.time()
        encryption_time = end_time - start_time

        start_time = time.time()
        decrypted_data = des_decrypt(key, encrypted_data)
        end_time = time.time()
        decryption_time = end_time - start_time

        return encryption_time, decryption_time
    elif (cipher_func == "AES"):
        start_time = time.time()
        encrypted_data = aes_encrypt(key, plaintext)
        end_time = time.time()
        encryption_time = end_time - start_time

        start_time = time.time()
        decrypted_data = aes_decrypt(key, encrypted_data)
        end_time = time.time()
        decryption_time = end_time - start_time

        return encryption_time, decryption_time



key_des = b"A1B2C3D4" 
key_aes = bytes.fromhex("0123456789ABCDEF0123456789ABCDEF")
plaintext = b"Performance Testing of Encryption Algorithms"

aestime_e,aestime_d = measure_time('AES',key_aes,plaintext)
destime_e,destime_d = measure_time('AES',key_aes,plaintext)

print(f"aes time=> encryption:{aestime_e}decryption{aestime_d}")
print(f"des time=> encryption:{destime_e}decryption{destime_d}")
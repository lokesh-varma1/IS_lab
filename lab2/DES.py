
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii


  

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


key = b"A1B2C3D4" 
n= input("e or d:")
if(n == 'e'):   
    plaintext = input("Enter the plaintext message: ").encode()
    encrypted_data = des_encrypt(key, plaintext)
    print(f"cipher text in hex: {binascii.hexlify(encrypted_data).decode()}")
  

elif(n =='d'):
    ciphertext_hex = input("Enter the ciphertext in hex format : ").strip()
    ciphertext_bytes = bytes.fromhex(ciphertext_hex)
    decrypted_data = des_decrypt(key, ciphertext_bytes)
    print(f"plain text: {decrypted_data.decode()}")






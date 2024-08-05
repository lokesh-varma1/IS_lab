
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii


  

def des_encrypt(key, plaintext):
    if len(key) != 24:
        raise ValueError("Key must be 24 bytes long")
    key1 = key[:8]
    key2 = key[8:16]
    key3 = key[16:]
    
    # Perform Triple DES encryption
    cipher1 = DES.new(key1, DES.MODE_ECB)
    cipher2 = DES.new(key2, DES.MODE_ECB)
    cipher3 = DES.new(key3, DES.MODE_ECB)
   
   
    # Pad the plaintext to be a multiple of DES block size
    padded_data = pad(plaintext, DES.block_size)
    # Encrypt the padded data
    inter1 = cipher1.encrypt(padded_data)
    inter2 = cipher2.decrypt(inter1)
    encrypted_data=cipher3.encrypt(inter2)
    return encrypted_data

def des_decrypt(key, ciphertext):
    if len(key) != 24:
        raise ValueError("Key must be 24 bytes long")
    

    key1 = key[:8]
    key2 = key[8:16]
    key3 = key[16:]
    cipher1 = DES.new(key1, DES.MODE_ECB)
    cipher2 = DES.new(key2, DES.MODE_ECB)
    cipher3 = DES.new(key3, DES.MODE_ECB)

    inter1 = cipher1.decrypt(ciphertext)
    inter2 = cipher2.encrypt(inter1)
    decrypted_padded_data = cipher3.decrypt(inter2)
    # Unpad the decrypted data
    decrypted_data = unpad(decrypted_padded_data, DES.block_size)
    return decrypted_data


key = bytes.fromhex("1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF")
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






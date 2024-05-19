from cryptography.fernet import Fernet
import base64
def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(message.encode())
    return encrypted_text

# Function to decrypt the message
def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_message)
    return decrypted_text.decode()
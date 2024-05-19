from cryptography.fernet import Fernet
import base64

# Function to encrypt the message
def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(message.encode())
    return encrypted_text

# Function to decrypt the message
def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_message)
    return decrypted_text.decode()

def main():
    key = input("Enter the shared key: ").encode()
    
    while True:
        action = input("Do you want to (s)end or (r)eceive a message? (s/r): ").strip().lower()
        
        if action == 's':
            message = input("Enter the message to send: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Encrypted Message: {base64.urlsafe_b64encode(encrypted_message).decode()}")
        
        elif action == 'r':
            encrypted_message = input("Enter the received encrypted message: ").encode()
            encrypted_message = base64.urlsafe_b64decode(encrypted_message)
            decrypted_message = decrypt_message(encrypted_message, key)
            print(f"Decrypted Message: {decrypted_message}")
        
        else:
            print("Invalid action. Please enter 's' to send or 'r' to receive a message.")

if __name__ == "__main__":
    main()

from cryptography.fernet import Fernet

# Generate a symmetric key and print it
key = Fernet.generate_key()
print(f"Shared Key: {key.decode()}")

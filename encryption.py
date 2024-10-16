from cryptography.fernet import Fernet

# Load the secret key from the key file
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Encrypt message
def encrypt_message(message):
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message.decode('utf-8')  # Return as base64-encoded string

# Decrypt message
def decrypt_message(encrypted_message):
    encrypted_message_bytes = encrypted_message.encode('utf-8')  # Ensure it's in bytes
    decrypted_message = fernet.decrypt(encrypted_message_bytes).decode('utf-8')
    return decrypted_message

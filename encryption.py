from cryptography.fernet import Fernet
import logging

# Setup logging
logging.basicConfig(filename='encryption.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Load the secret key from the key file
try:
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()
        logging.info('Secret key loaded successfully')
except Exception as e:
    logging.error(f'Error loading secret key: {str(e)}')
    raise

fernet = Fernet(key)

# Encrypt message
def encrypt_message(message):
    try:
        encrypted_message = fernet.encrypt(message.encode())
        logging.info('Message encrypted successfully')
        return encrypted_message.decode('utf-8')  # Return as base64-encoded string
    except Exception as e:
        logging.error(f'Error encrypting message: {str(e)}')
        raise

# Decrypt message
def decrypt_message(encrypted_message):
    try:
        encrypted_message_bytes = encrypted_message.encode('utf-8')  # Ensure it's in bytes
        decrypted_message = fernet.decrypt(encrypted_message_bytes).decode('utf-8')
        logging.info('Message decrypted successfully')
        return decrypted_message
    except Exception as e:
        logging.error(f'Error decrypting message: {str(e)}')
        raise

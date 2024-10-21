from cryptography.fernet import Fernet
import os
import logging

# Configure logging
logging.basicConfig(
    filename='key_management.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Generate a new key and save it into a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    logging.info("Secret key generated and saved as 'secret.key'.")
    print("Secret key generated and saved as 'secret.key'.")

# Load the existing key from the file
def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
        logging.info("Secret key loaded from 'secret.key'.")
        print("Secret key loaded from 'secret.key'.")
        return key
    else:
        logging.warning("No key found. Generating a new key.")
        print("No key found. Generating a new key.")
        generate_key()
        return load_key()  # Load the newly generated key

if __name__ == '__main__':
    key = load_key()

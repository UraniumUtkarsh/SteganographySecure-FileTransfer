from cryptography.fernet import Fernet

# Generate a key and save it into a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

if __name__ == '__main__':
    generate_key()
    print("Secret key generated and saved as 'secret.key'.")

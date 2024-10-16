from stegano import lsb
from PIL import Image

# Function to encode the encrypted message into an image
def encode_image(input_image_path, encrypted_message, output_image_path):
    image = Image.open(input_image_path)
    encoded_image = lsb.hide(image, encrypted_message.decode('utf-8'))
    encoded_image.save(output_image_path)
    return output_image_path

# Function to decode the encrypted message from an image
def decode_image(input_image_path):
    image = Image.open(input_image_path)
    encoded_message = lsb.reveal(image)
    return encoded_message.encode('utf-8')  # Return it as bytes for decryption

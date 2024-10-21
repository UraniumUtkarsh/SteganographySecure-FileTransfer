from stegano import lsb
from PIL import Image
import logging

# Configure logging
logging.basicConfig(
    filename='Image_Encoder.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Function to encode the encrypted message into an image
def encode_image(input_image_path, encrypted_message, output_image_path):
    try:
        image = Image.open(input_image_path)
        encoded_image = lsb.hide(image, encrypted_message.decode('utf-8'))
        encoded_image.save(output_image_path)
        logging.info(f"Message successfully encoded into '{input_image_path}' and saved as '{output_image_path}'.")
        #print(f"Message successfully encoded into '{output_image_path}'.")
        return output_image_path
    except Exception as e:
        logging.error(f"Failed to encode the message into '{input_image_path}'. Error: {str(e)}")
        #print(f"Error: {str(e)}")

# Function to decode the encrypted message from an image
def decode_image(input_image_path):
    try:
        image = Image.open(input_image_path)
        encoded_message = lsb.reveal(image)
        if encoded_message:
            logging.info(f"Message successfully decoded from '{input_image_path}'.")
            #print(f"Message decoded from '{input_image_path}': {encoded_message}")
            return encoded_message.encode('utf-8')  # Return it as bytes for decryption
        else:
            logging.warning(f"No message found in '{input_image_path}'.")
            #print(f"No message found in '{input_image_path}'.")
            return None
    except Exception as e:
        logging.error(f"Failed to decode the message from '{input_image_path}'. Error: {str(e)}")
        #print(f"Error: {str(e)}")

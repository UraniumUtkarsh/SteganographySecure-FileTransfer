from PIL import Image
import numpy as np

# Convert the binary data to pixels
def binary_to_pixels(binary_data):
    pixels = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        pixels.append(int(byte, 2))
    return pixels

# Function to encode secret data into an image
def encode_image(input_image_path, secret_data, output_image_path):
    # Open the image
    image = Image.open(input_image_path)
    image = image.convert('RGB')  # Ensure the image is in RGB mode

    # Convert the encrypted message from bytes to a string
    if isinstance(secret_data, bytes):
        secret_data = secret_data.decode('utf-8')

    # Convert the secret data into binary
    binary_secret = ''.join(format(ord(i), '08b') for i in secret_data)
    
    # Get the image data
    data = np.array(image)

    # Flatten the image data
    flat_data = data.flatten()

    # Make sure the image has enough pixels to store the secret data
    if len(binary_secret) > len(flat_data):
        raise ValueError("Image is too small to encode the secret data.")

    # Modify the least significant bit of each pixel to store the binary secret data
    for i in range(len(binary_secret)):
        flat_data[i] = (flat_data[i] & ~1) | int(binary_secret[i])

    # Reshape the flat data back to the original image shape
    new_data = flat_data.reshape(data.shape)

    # Create a new image from the modified data
    new_image = Image.fromarray(new_data.astype(np.uint8))

    # Save the encoded image
    new_image.save(output_image_path)
    return output_image_path

# Function to decode secret data from an image
def decode_image(input_image_path):
    # Open the image
    image = Image.open(input_image_path)
    image = image.convert('RGB')  # Ensure the image is in RGB mode

    # Get the image data
    data = np.array(image)

    # Flatten the image data
    flat_data = data.flatten()

    # Extract the least significant bit of each pixel to reconstruct the binary secret data
    binary_secret = [str(pixel & 1) for pixel in flat_data]

    # Group the binary data into bytes and convert them to characters
    secret_data = ''.join(chr(int(''.join(binary_secret[i:i+8]), 2)) for i in range(0, len(binary_secret), 8))

    # Remove trailing null characters (if any)
    return secret_data.rstrip('\x00')

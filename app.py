from flask import Flask, request, render_template, send_file, jsonify
from encryption import encrypt_message, decrypt_message
from steganography import encode_image, decode_image
import os
from werkzeug.utils import secure_filename
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# Ensure the 'uploads' folder exists
os.makedirs('uploads', exist_ok=True)

# Home route
@app.route('/')
def index():
    app.logger.info('Home page accessed')
    return render_template('index.html')

# Route to encode message into an image
@app.route('/encode', methods=['POST'])
def encode():
    if 'file' not in request.files:
        app.logger.error('No file part in encode request')
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        app.logger.error('No selected file in encode request')
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        filename = secure_filename(file.filename)
        input_image_path = os.path.join('uploads', filename)
        file.save(input_image_path)
        
        message = request.form['message']
        encrypted_message = encrypt_message(message)
        app.logger.info(f'File {filename} uploaded and message encrypted')
        
        # Create a unique output filename
        output_image_name = 'encoded_' + filename
        output_image_path = os.path.join('uploads', output_image_name)
        
        # Encode image with the secret message
        try:
            encode_image(input_image_path, encrypted_message, output_image_path)
            app.logger.info(f'Image {filename} encoded successfully')
        except Exception as e:
            app.logger.error(f'Error encoding image {filename}: {str(e)}')
            return jsonify({"error": f"Error encoding image: {str(e)}"}), 500

        return send_file(output_image_path, as_attachment=True)

# Route to decode message from an image
@app.route('/decode', methods=['POST'])
def decode():
    if 'file' not in request.files:
        app.logger.error('No file part in decode request')
        return jsonify({"success": False, "message": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        app.logger.error('No selected file in decode request')
        return jsonify({"success": False, "message": "No selected file"}), 400

    try:
        # Save the uploaded file to a temporary location
        filename = secure_filename(file.filename)
        input_image_path = os.path.join('uploads', filename)
        file.save(input_image_path)
        
        # Decode the message from the image
        encoded_message = decode_image(input_image_path)
        app.logger.info(f'Message decoded from image {filename}')
        
        # Decrypt the message
        decrypted_message = decrypt_message(encoded_message)
        app.logger.info(f'Message decrypted from image {filename}')
        
        # Return the decrypted message as a JSON response
        return jsonify({"success": True, "message": decrypted_message})
    
    except Exception as e:
        app.logger.error(f'Error decoding image {filename}: {str(e)}')
        return jsonify({"success": False, "message": f"Error decoding image: {str(e)}"}), 500

if __name__ == '__main__':
    app.logger.info('Starting Flask application')
    app.run(debug=True)

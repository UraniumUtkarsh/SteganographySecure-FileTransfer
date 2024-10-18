from flask import Flask, request, render_template, send_file, jsonify
from encryption import encrypt_message, decrypt_message
from steganography import encode_image, decode_image
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Ensure the 'uploads' folder exists
os.makedirs('uploads', exist_ok=True)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to encode message into an image
@app.route('/encode', methods=['POST'])
def encode():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        input_image_path = os.path.join('uploads', filename)
        file.save(input_image_path)
        
        message = request.form['message']
        encrypted_message = encrypt_message(message)
        
        # Create a unique output filename
        output_image_name = 'encoded_' + filename
        output_image_path = os.path.join('uploads', output_image_name)
        
        # Encode image with the secret message
        try:
            encode_image(input_image_path, encrypted_message, output_image_path)
        except Exception as e:
            return jsonify({"error": f"Error encoding image: {str(e)}"}), 500

        return send_file(output_image_path, as_attachment=True)


# Route to decode message from an image
@app.route('/decode', methods=['POST'])
def decode():
    if 'file' not in request.files:
        return jsonify({"success": False, "message": "No file part"}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({"success": False, "message": "No selected file"}), 400

    try:
        # Save the uploaded file to a temporary location
        filename = secure_filename(file.filename)
        input_image_path = os.path.join('uploads', filename)
        file.save(input_image_path)
        
        # Decode the message from the image
        encoded_message = decode_image(input_image_path)
        
        # Decrypt the message
        decrypted_message = decrypt_message(encoded_message)
        
        # Return the decrypted message as a JSON response
        return jsonify({"success": True, "message": decrypted_message})
    
    except Exception as e:
        return jsonify({"success": False, "message": f"Error decoding image: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)

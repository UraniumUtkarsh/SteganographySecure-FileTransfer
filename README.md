```markdown
# Steganography Secure File Transfer 🖼️🔐

## Description
The Steganography Secure File Transfer project is a web application that allows users to encode and decode messages within images. It utilizes steganography techniques to securely hide messages within image files, ensuring privacy and confidentiality during file transfers. 🤫

## Features 🌟
- Encode Message into Image: Upload an image and input a message to be encrypted and embedded within the image. 📩
- Decode Message from Image: Upload an encoded image to extract and display the hidden message. 📤
- User-Friendly Interface: Designed with simplicity in mind, providing a seamless experience for users. 🎨

## Technologies Used 🛠️
- Flask: A lightweight WSGI web application framework for Python.
- HTML/CSS: For the front-end user interface.
- JavaScript: To handle form submissions and display dynamic content.
- Pillow (PIL): For image processing and manipulation.

## Getting Started 🚀

### Prerequisites
- Python 3.x
- Flask
- Pillow

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/UraniumUtkarsh/steganography-secure-file-transfer.git
   cd steganography-secure-file-transfer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate the secret.key (Required only once, during setting up the app):
   ```bash
   python generate_key.py
   ```

### Running the Application
1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`. 🌐

## Usage 📘
- To Encode: Navigate to the "Encode Message into Image" section, enter your message, select an image, and click "Encode". ✏️
- To Decode: Navigate to the "Decode Message from Image" section, upload the encoded image, and click "Decode". 📖

## File Structure 🗂️
```
/steganography-secure-file-transfer
│
├── app.py                # Main application file
├── static                # Directory for static files (CSS, images)
│   └── images            # Directory for image assets
├── templates             # Directory for HTML templates
│   └── index.html        # Main HTML file for the application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Contributing 🤝
Contributions are welcome! Please feel free to submit a pull request or report any issues you encounter.

## Acknowledgments 🙏
- Special thanks to the contributors and resources that helped in the development of this project.
```

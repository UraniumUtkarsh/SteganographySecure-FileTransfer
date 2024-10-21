function displayFilename(inputId, filenameId) {
    var input = document.getElementById(inputId);
    var filename = input.files[0]?.name;
    document.getElementById(filenameId).textContent = filename ? "File attached: " + filename : "";
}

function submitDecodeForm() {
    var formData = new FormData(document.getElementById('decodeForm'));

    // Display loading message and spinner
    document.getElementById('decodedText').textContent = "Decoding... please wait.";
    document.getElementById('loadingSpinner').style.display = 'block';  // Show spinner
    document.getElementById('decodedMessage').style.display = 'block';

    fetch('/decode', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('loadingSpinner').style.display = 'none';  // Hide spinner
        if (data.success) {
            document.getElementById('decodedText').textContent = data.message;
        } else {
            document.getElementById('decodedText').textContent = "Failed to decode message.";
        }
    })
    .catch(error => {
        document.getElementById('loadingSpinner').style.display = 'none';  // Hide spinner
        console.error('Error:', error);
        document.getElementById('decodedText').textContent = "An error occurred during decoding.";
    });
}

function clearDecodedMessage() {
    document.getElementById('decoded-message').innerHTML = "";
}

document.getElementById('decode-file-input').addEventListener('change', function() {
    clearDecodedMessage();
});

function displayFilename(inputId, filenameId) {
    var input = document.getElementById(inputId);
    var filename = input.files[0]?.name;
    document.getElementById(filenameId).textContent = filename ? "File attached: " + filename : "";
}

function submitDecodeForm() {
    var formData = new FormData(document.getElementById('decodeForm'));

    fetch('/decode', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('decodedText').textContent = data.message;
            document.getElementById('decodedMessage').style.display = 'block';
        } else {
            alert('Failed to decode message.');
        }
    })
    .catch(error => console.error('Error:', error));
}
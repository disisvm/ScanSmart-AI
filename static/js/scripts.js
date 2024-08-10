// Ensure the DOM is fully loaded before running the script
document.addEventListener("DOMContentLoaded", function() {

    // Get the file input element
    const fileInput = document.getElementById('formFile');

    // Get the form element
    const form = document.getElementById('uploadForm');

    // Event listener to display a preview of the uploaded image
    fileInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        const previewContainer = document.createElement('div');
        const imgPreview = document.createElement('img');

        if (file) {
            const reader = new FileReader();

            reader.onload = function(e) {
                imgPreview.src = e.target.result;
                imgPreview.style.maxWidth = '100%';
                imgPreview.style.maxHeight = '300px';
                imgPreview.style.marginTop = '20px';

                // Remove previous preview if exists
                const existingPreview = document.querySelector('#imgPreview');
                if (existingPreview) {
                    existingPreview.remove();
                }

                // Append the new preview
                previewContainer.id = 'imgPreview';
                previewContainer.appendChild(imgPreview);
                form.appendChild(previewContainer);
            };

            reader.readAsDataURL(file);
        }
    });

    // Optional: Form submission event handler (can add custom behavior here)
    form.addEventListener('submit', function(event) {
        // Optionally, you can add custom logic here before the form is submitted
        console.log("Form submitted with file:", fileInput.files[0].name);
    });
});

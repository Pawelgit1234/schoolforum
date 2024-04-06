document.addEventListener('DOMContentLoaded', function () {
    const copyableTexts = document.querySelectorAll('.copyable');
    copyableTexts.forEach(function (element) {
        element.addEventListener('click', function () {
            const textToCopy = this.getAttribute('data-text');
            const tempInput = document.createElement('input');
            tempInput.value = textToCopy;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand('copy');
            document.body.removeChild(tempInput);
            const copiedAlert = document.createElement('div');
            copiedAlert.className = 'copied-alert';
            copiedAlert.textContent = 'Copied to clipboard: ' + textToCopy;
            document.body.appendChild(copiedAlert);
            copiedAlert.style.position = 'fixed';
            copiedAlert.style.top = '50%';
            copiedAlert.style.left = '50%';
            copiedAlert.style.transform = 'translate(-50%, -50%)';
            setTimeout(function () {
                document.body.removeChild(copiedAlert);
            }, 1000);
        });
    });

    const overlay = document.getElementById('overlay');
    overlay.style.display = 'none';

    overlay.addEventListener('click', function (event) {
        if (event.target === this) {
            hideGallery();
        }
    });
});

let currentIndex = 0;

function showGallery() {
    const overlay = document.getElementById('overlay');
    overlay.style.display = 'flex';
}

function hideGallery() {
    const overlay = document.getElementById('overlay');
    overlay.style.display = 'none';
}

function imgForward() {
    currentIndex = (currentIndex + 1) % images.length;
    updateImage();
}

function imgBack() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateImage();
}

function updateImage() {
    const galleryImage = document.getElementById('galleryImage');
    galleryImage.src = images[currentIndex];
}
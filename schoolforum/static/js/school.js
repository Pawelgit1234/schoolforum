let offset = 10;

function loadMoreDiscussions() {
    fetch(url + offset)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const discussionsContainer = document.querySelector('.discussions-container');

            data.forEach(discussion => {
                const discussionCard = document.createElement('div');
                discussionCard.classList.add('col-md-12', 'mb-4');
                discussionCard.innerHTML = `
                    <div class="card ${discussion.is_closed ? 'closed-discussion' : ''}">
                        <div class="card-body">
                            <p class="card-text">
                                <img src="${discussion.avatar_url}" alt="Avatar" width="30" height="30" style="border-radius: 50%;">
                                ${discussion.user}
                                <img src="${clock}" width="20">
                                ${discussion.creation_date}
                                <img src="${book}" width="20">
                                ${discussion.type}
                                <img src="${star_full}" width="20">
                                ${discussion.rating}
                                <img src="${comment}" width="20">
                                ${discussion.comments_count}
                            </p>
                            <h2 class="card-title">${discussion.title}</h2>
                        </div>
                        ${discussion.is_closed ? '<div class="closed-indicator"></div>' : ''}
                    </div>
                `;
                discussionsContainer.appendChild(discussionCard);
            });

            offset += data.length;
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

window.addEventListener('scroll', () => {
    if (isProcessing) {
        return;
    }
    if (isUserCloseToBottom()) {
        isProcessing = true;

        loadMoreDiscussions();

        setTimeout(() => {
            isProcessing = false;
        }, 1000);
    }
});

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
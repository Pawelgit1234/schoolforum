let offset = 10;

function loadMoreSchools() {
    fetch(url + offset)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const schoolsContainer = document.querySelector('.row');

            data.forEach(school => {
                const cardDiv = document.createElement('div');
                cardDiv.classList.add('col-md-6', 'mb-4');

                const cardLink = document.createElement('a');
                cardLink.classList.add('text-decoration-none');
                cardLink.href = `/school/${school.slug}`;

                const card = document.createElement('div');
                card.classList.add('card', 'home-card', 'mx-4');

                const cardImg = document.createElement('img');
                cardImg.classList.add('card-img-top');
                cardImg.src = school.image_url || 'https://via.placeholder.com/300';
                cardImg.alt = 'School Image';

                const cardBody = document.createElement('div');
                cardBody.classList.add('card-body');

                const cardTitle = document.createElement('h5');
                cardTitle.classList.add('card-title');
                cardTitle.textContent = school.name;

                const cardText = document.createElement('p');
                cardText.classList.add('card-text');
                cardText.textContent = school.description;

                cardBody.appendChild(cardTitle);
                cardBody.appendChild(cardText);
                card.appendChild(cardImg);
                card.appendChild(cardBody);
                cardLink.appendChild(card);
                cardDiv.appendChild(cardLink);

                schoolsContainer.appendChild(cardDiv);
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

        loadMoreSchools();

        setTimeout(() => {
            isProcessing = false;
        }, 1000);
    }
});
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
                            <a href="/discussion/${discussion.id}" class="no-underline"><h2 class="card-title">${discussion.title}</h2></a>
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

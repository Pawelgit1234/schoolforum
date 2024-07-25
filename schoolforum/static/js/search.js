let offset = 0;

function loadMoreSearchedObjects()
{
    fetch(load_more_searched_objects_url + '?offset=' + offset + "&query=" + query)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            offset += data.found_count;
            showData(data)
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

function showData(data) {
    let schoolsColumn = document.getElementById('schools-column');
    let discussionsColumn = document.getElementById('discussions-column');

    data.schools.forEach(school => {
            let schoolCard = `
                <div class="col-md-6 mb-4">
            <a href="/school/${school.slug}" class="text-decoration-none">
                <div class="card home-card mx-4">
                    <img src="${(school.photo_url) ? school.photo_url : 'https://via.placeholder.com/300'}" class="card-img-top" alt="School Image">
                    <div class="card-body">
                        <h5 class="card-title">${ school.name }</h5>
                        <p class="card-text">
                            ${school.description}
                        </p>
                    </div>
                </div>
            </a>
        </div>
            `;
            schoolsColumn.innerHTML += schoolCard;
        });

        data.discussions.forEach(discussion => {
            let discussionCard = `
                <div class="card mb-4 ${discussion.is_closed ? 'closed-discussion' : ''}">
                    <div class="card-body">
                        <p class="card-text">
                            <img src="${discussion.avatar}" alt="Avatar" width="30" height="30" style="border-radius: 50%;">
                            ${discussion.user}
                            <img src="${clock_img}" width="20">
                            ${new Date(discussion.created_at).toLocaleString()}
                            <img src="${book_img}" width="20">
                            ${discussion.lesson_type}
                            <img src="${star_img}" width="20">
                            ${discussion.rating}
                            <img src="${comment_img}" width="20">
                            ${discussion.comments_count}
                        </p>
                        <a href="/discussion/${discussion.id}" class="no-underline"><h2 class="card-title">${discussion.title}</h2></a>
                    </div>
                    ${discussion.is_closed ? '<div class="closed-indicator"></div>' : ''}
                </div>
            `;
            discussionsColumn.innerHTML += discussionCard;
        });
}

window.addEventListener('scroll', () => {
    if (isProcessing) {
        return;
    }
    if (isUserCloseToBottom()) {
        isProcessing = true;
        loadMoreSearchedObjects();
        setTimeout(() => {
            isProcessing = false;
        }, 1000);
    }
});

document.addEventListener('DOMContentLoaded', () => {
    loadMoreSearchedObjects(); // Load initial comments
});
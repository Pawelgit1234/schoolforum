function change_discussion_rating(id, is_up_arrow) {
    const data = {
        id: id,
        is_up_arrow: is_up_arrow
    };

    fetch(discussion_rating_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('rating-balance').textContent = data.new_rating;
        updateDiscussionArrowDisplay(data.is_up);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
}

function updateDiscussionArrowDisplay(is_up) {
    const upArrow = document.getElementById(`up-arrow`);
    const downArrow = document.getElementById(`down-arrow`);

     if (is_up === null) {
        upArrow.src = arrow_up;
        downArrow.src = arrow_down;
    } else if (!is_up) {
        upArrow.src = arrow_up;
        downArrow.src = arrow_down_black;
    } else if (is_up) {
        upArrow.src = arrow_up_black;
        downArrow.src = arrow_down;
    }
}

let offset = 0;

function createCommentElement(comment) {
    const commentElement = document.createElement('div');
    commentElement.className = 'comment';

    const commentContent = `
        <div class="d-flex align-items-start">
            <img src="${comment.avatar}" alt="Avatar" width="30" height="30" style="border-radius: 50%; margin-right: 10px;">
            <div>
                <p><strong>${comment.user}</strong> <span class="text-muted">${comment.created_at}</span></p>
                <p>${comment.content}</p>
                <div class="comment-photos">
                    ${comment.photos.map(photo => `<img src="${photo}" class="comment-photo" alt="Comment Photo" width="200px">`).join('')}
                </div>
            </div>
        </div>
    `;

    commentElement.innerHTML = commentContent;

    if (comment.replies.length > 0) {
        const repliesContainer = document.createElement('div');
        repliesContainer.className = 'replies';
        repliesContainer.style.marginLeft = '40px';
        comment.replies.forEach(reply => {
            const replyElement = createReplyElement(reply);
            repliesContainer.appendChild(replyElement);
        });
        commentElement.appendChild(repliesContainer);
    }

    return commentElement;
}

function createReplyElement(reply) {
    const replyElement = document.createElement('div');
    replyElement.className = 'reply';

    const replyContent = `
        <div class="d-flex align-items-start">
            <img src="${reply.avatar}" alt="Avatar" width="30" height="30" style="border-radius: 50%; margin-right: 10px;">
            <div>
                <p><strong>${reply.user}</strong> <span class="text-muted">${reply.created_at}</span></p>
                <p>${reply.content}</p>
                <div class="comment-photos">
                    ${reply.photos.map(photo => `<img src="${photo}" class="comment-photo" alt="Reply Photo" width="200px">`).join('')}
                </div>
            </div>
        </div>
    `;

    replyElement.innerHTML = replyContent;

    return replyElement;
}

function loadMoreComments() {
    fetch(load_more_comments_url + offset)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const commentsContainer = document.querySelector('.discussion-comments');
            data.forEach(comment => {
                const commentElement = createCommentElement(comment);
                commentsContainer.appendChild(commentElement);
            });
            offset += data.length;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
}

window.addEventListener('scroll', () => {
    if (isProcessing) {
        return;
    }
    if (isUserCloseToBottom()) {
        isProcessing = true;
        loadMoreComments();
        setTimeout(() => {
            isProcessing = false;
        }, 1000);
    }
});

document.addEventListener('DOMContentLoaded', () => {
    loadMoreComments(); // Load initial comments
});
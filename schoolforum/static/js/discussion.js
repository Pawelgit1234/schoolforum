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

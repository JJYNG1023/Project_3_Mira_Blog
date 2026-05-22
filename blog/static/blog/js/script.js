document.addEventListener('DOMContentLoaded', function () {
    const topicButtons = document.querySelectorAll('.topic-btn');
    const postCards = document.querySelectorAll('.mira-post-card');

    topicButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const selectedTagTopic = button.getAttribute('data-topic');

            topicButtons.forEach(function (btn) {
                btn.classList.remove('active');
            });

            button.classList.add('active');

            postCards.forEach(function (card) {
                const postTopics = card.getAttribute('data-topic') || '';
                const postColumn = card.closest('.col-6');

                if (selectedTagTopic === 'all' || postTopics.includes(selectedTagTopic)) {
                    postColumn.style.display = 'block';
                } else {
                    postColumn.style.display = 'none';
                }
            });
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const topicButtons = document.querySelectorAll('.topic-btn');

    let postCards = document.querySelectorAll('.post-card-wrapper');

    if (postCards.length === 0) {
        postCards = document.querySelectorAll('.mira-post-card');
    }

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


// Create post image preview
document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.getElementById("imageInput");
    const imagePreviewWrapper = document.getElementById("imagePreviewWrapper");

    if (!imageInput || !imagePreviewWrapper) {
        return;
    }
    imageInput.addEventListener("change", function () {
        const file = Array.from(imageInput.files).slice(0, 5); // Get the first file (limit to 5 files)

        imagePreviewWrapper.innerHTML = "";
        // Clear previous previews

        file.forEach(function (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                const img = document.createElement("img");
                img.src = e.target.result;
                img.classList.add("image-preview-thumb");
                imagePreviewWrapper.appendChild(img);
            }:
            reader.readAsDataURL(file);
        });
        const addButton = document.createElement("label");
        addButton.setAttribute("for", "imageInput");
        addButton.classList.add("image-upload-box");
        addButton.innerHTML = "<i class=\"bi bi-plus-lg\"></i>";
        imagePreviewWrapper.appendChild(addButton);
    });
});

# Create post tag preview
document.addEventListener("DOMContentLoaded", function () {
    const tagInput = document.getElementById("tagInput");
    const tagNames = document.getElementById("tagNames");
    const tagPreviewWrapper = document.getElementById("tagPreviewWrapper");

    if (!tagInput || !tagNames || !tagPreviewWrapper) {
        return;
    }

    let tags = [];

    function updateTags() {
        tagPreviewWrapper.innerHTML = "";
        tags.forEach(function (tag) {
            const tagElement = document.createElement("div");
            tagElement.classList.add("create-tag-item");
            tagElement.textContent = "#" + tag;
            tagPreviewWrapper.appendChild(tagElement);
        });
        tagNames.value = tags.join(",");
    }
    tagInput.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            event.preventDefault();

            let tag = tagInput.value.trim();

            tag = tag.replace("#", "");
            if (tag && !tags.includes(tag)) {
                tags.push(tag);
                updateTags();
            }
            tagInput.value = "";
        }
    });
});

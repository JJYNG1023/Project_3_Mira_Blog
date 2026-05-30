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

    const tagInput = document.getElementById("tagInput");
    const tagNames = document.getElementById("tagNames");
    const tagPreviewWrapper = document.getElementById("tagPreviewWrapper");
    const createPostForm = document.getElementById("createPostForm");

    // Image preview
    if (imageInput && imagePreviewWrapper) {
        let selectedFiles = [];

        function updateImageInputFiles() {
            const dataTransfer = new DataTransfer();

            selectedFiles.forEach(function (file) {
                dataTransfer.items.add(file);
            });

            imageInput.files = dataTransfer.files;
        }

        function updateImagePreview() {
            imagePreviewWrapper.innerHTML = "";

            if (selectedFiles.length < 5) {
                const addButton = document.createElement("label");
                addButton.setAttribute("for", "imageInput");
                addButton.classList.add("image-upload-box");
                addButton.innerHTML = '<i class="bi bi-plus-lg"></i>';
                imagePreviewWrapper.appendChild(addButton);
            }

            selectedFiles.forEach(function (file, index) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    const img = document.createElement("img");
                    img.src = e.target.result;
                    img.classList.add("image-preview-thumb");
                    imagePreviewWrapper.appendChild(img);
                };

                reader.readAsDataURL(file);
            });
        }
        imageInput.addEventListener("change", function () {
            const newFiles = Array.from(imageInput.files);
            newFiles.forEach(function (file) {
                if (selectedFiles.length < 5) {
                    selectedFiles.push(file);
                }
            });

            updateImageInputFiles();
            updateImagePreview();
        });
    }
    // Tag preview
    if (tagInput && tagNames && tagPreviewWrapper) {
        let tags = [];

        function updateTags() {
            tagPreviewWrapper.innerHTML = "";

            tags.forEach(function (tag) {
                const tagElement = document.createElement("span");
                tagElement.classList.add("create-tag-item");
                tagElement.textContent = "#" + tag;
                tagPreviewWrapper.appendChild(tagElement);
            });

            tagNames.value = tags.join(",");
        }

        tagInput.addEventListener("keydown", function (event) {
            if (event.key === "Enter" || event.key === ",") {
                event.preventDefault();

                let tag = tagInput.value.trim().replace("#", "");

                if (tag && !tags.includes(tag)) {
                    tags.push(tag);
                    updateTags();
                }

                tagInput.value = "";
            }
        });

        if (createPostForm) {
            createPostForm.addEventListener("keydown", function (event) {
                if (event.key === "Enter" && event.target === tagInput) {
                    event.preventDefault();
                }
            });
        }
    }
});

// Responsive tag filter visibility
document.addEventListener("DOMContentLoaded", function () {
    const filterWrappers = document.querySelectorAll(".topic-filter-wrapper");

    function updateVisibleTags() {
        filterWrappers.forEach(function (wrapper) {
            const tagButtons = wrapper.querySelectorAll(".tag-filter-item");

            // Reset all tags first
            tagButtons.forEach(function (tag) {
                tag.classList.remove("d-none");
            });

            const maxTags = window.innerWidth >= 768 ? 10 : 5;
            let visibleTagCount = 0;

            tagButtons.forEach(function (tag) {
                visibleTagCount++;

                if (visibleTagCount > maxTags) {
                    tag.classList.add("d-none");
                    return;
                }

                const wrapperRight = wrapper.getBoundingClientRect().right;
                const tagRight = tag.getBoundingClientRect().right;

                if (tagRight > wrapperRight) {
                    tag.classList.add("d-none");
                }
            });
        });
    }

    updateVisibleTags();

    window.addEventListener("resize", updateVisibleTags);
});

// Responsive recent search history/filter
document.addEventListener("DOMContentLoaded", function () {
    const recentSearchWrapper = document.getElementById("recentSearchWrapper");
    const clearSearchHistory = document.getElementById("clearSearchHistory");
    const currentSearchQueryElement = document.getElementById("current-search-query");

    if (!recentSearchWrapper) {
        return;
    }
let recentSearches = JSON.parse(localStorage.getItem("recentSearches")) || [];

    if (currentSearchQueryElement) {
        const currentSearchQuery = JSON.parse(currentSearchQueryElement.textContent);

        if (currentSearchQuery) {
            recentSearches = recentSearches.filter(function (search) {
                return search.toLowerCase() !== currentSearchQuery.toLowerCase();
            });

            recentSearches.unshift(currentSearchQuery);
            recentSearches = recentSearches.slice(0, 6);

            localStorage.setItem("recentSearches", JSON.stringify(recentSearches));
        }
    }
    // store recent search words

    // render recent search words on web page
    function renderRecentSearches() {
        recentSearchWrapper.innerHTML = "";

        if (recentSearches.length === 0) {
            recentSearchWrapper.innerHTML = `
                <p class="mira-post-preview text-muted mb-0">
                    No recent searches yet.
                </p>
            `;
            return;
        }

        recentSearches.forEach(function (search) {
            const searchLink = document.createElement("a");
            searchLink.href = "/search/?q=" + encodeURIComponent(search);
            searchLink.className = "btn btn-outline-dark btn-sm rounded-pill px-4";
            searchLink.textContent = search;

            recentSearchWrapper.appendChild(searchLink);
        });
    }
    // delete the recent search history 
    if (clearSearchHistory) {
        clearSearchHistory.addEventListener("click", function () {
            localStorage.removeItem("recentSearches");
            recentSearches = [];
            renderRecentSearches();
        });
    }

    renderRecentSearches();
});
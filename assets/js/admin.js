let editButtons = document.querySelectorAll('.edit-button');
editButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        let postId = event.target.dataset.postId;
        let postTitle = document.getElementById('post-title-' + postId);
        let postContent = document.getElementById('post-content-' + postId);
        let editTitleInput = button.parentNode.querySelector('input[name="title"]');
        let editContentInput = button.parentNode.querySelector('textarea[name="content"]');
        let saveButton = button.parentNode.querySelector('.save-button');
        
        // Hide the post title and show the edit input field and save button
        postTitle.style.display = 'none';
        postContent.style.display = 'none';
        editTitleInput.style.display = 'block';
        editContentInput.style.display = 'block';
        saveButton.style.display = 'inline-block';

        // Add event listener for Escape key press
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                // Show the post title and hide the edit input field and save button
                postTitle.style.display = 'inline-block';
                postContent.style.display = 'inline-block';
                editTitleInput.style.display = 'none';
                editContentInput.style.display = 'none';
                saveButton.style.display = 'none';
            }
        });
    });
});    



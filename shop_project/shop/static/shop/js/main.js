// shop/static/shop/js/main.js

document.addEventListener('DOMContentLoaded', function() {

    // --- Mobile Menu Toggle ---
    const menuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    if (menuButton && mobileMenu) {
        menuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
        // Optional: Close menu when a link is clicked
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
            });
        });
    }

    // --- Contact Form Submission ---
    const contactForm = document.getElementById('contact-form');
    const submitButton = document.getElementById('submit-button');
    const formFeedback = document.getElementById('form-feedback');

    if (contactForm && submitButton && formFeedback) {
        contactForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default browser form submission

            // Clear previous feedback and errors
            formFeedback.textContent = '';
            formFeedback.className = 'form-feedback'; // Reset classes
            clearErrors();

            // Disable submit button
            submitButton.disabled = true;
            submitButton.textContent = 'Sending...';

            // Get form data
            const formData = new FormData(contactForm);

            // Get CSRF token (Django sets a cookie named 'csrftoken')
            const csrfToken = getCookie('csrftoken');

            // Send data using Fetch API
            fetch(contactForm.action, { // Use the URL from the form's action attribute
                method: 'POST',
                body: formData, // Send as FormData
                headers: {
                    // 'Content-Type': 'application/x-www-form-urlencoded', // FormData sets this automatically with boundary
                    'X-CSRFToken': csrfToken, // Crucial: Include CSRF token
                    'X-Requested-With': 'XMLHttpRequest', // Identify as AJAX request (optional but good practice)
                },
            })
            .then(response => {
                // Check if response status indicates success (e.g., 200 OK) or client/server error
                if (!response.ok) {
                    // If status is 400 (Bad Request), likely validation errors
                    if (response.status === 400) {
                        return response.json().then(data => {
                            throw { type: 'validation', data: data }; // Throw specific error type
                        });
                    }
                    // Otherwise, throw a generic error
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json(); // Parse successful JSON response
            })
            .then(data => {
                // Handle success response from Django view
                if (data.status === 'success') {
                    formFeedback.textContent = data.message;
                    formFeedback.classList.add('success');
                    contactForm.reset(); // Clear the form fields
                } else {
                    // Should not happen if response.ok was true, but handle defensively
                    formFeedback.textContent = data.message || 'An unexpected error occurred.';
                    formFeedback.classList.add('error');
                }
            })
            .catch(error => {
                // Handle errors (network error, validation error, server error)
                console.error('Form submission error:', error);

                if (error.type === 'validation') {
                    // Handle validation errors from Django
                    formFeedback.textContent = error.data.message || 'Please correct the errors below.';
                    formFeedback.classList.add('error');
                    displayErrors(error.data.errors); // Display field-specific errors
                } else {
                    // Handle generic network/server errors
                    formFeedback.textContent = 'Could not send message. Please check your connection or try again later.';
                    formFeedback.classList.add('error');
                }
            })
            .finally(() => {
                // Re-enable submit button regardless of success or failure
                submitButton.disabled = false;
                submitButton.textContent = 'Send Message';
            });
        });
    }

    // --- Helper Functions ---

    // Function to get a cookie value by name (needed for CSRF token)
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Function to display field-specific validation errors
    function displayErrors(errors) {
        if (!errors) return;
        for (const fieldName in errors) {
            const errorElement = document.getElementById(`error-${fieldName}`);
            const inputElement = document.getElementById(`id_${fieldName}`); // Django usually prefixes ids with 'id_'
            if (errorElement) {
                errorElement.textContent = errors[fieldName];
            }
            if (inputElement) {
                inputElement.classList.add('border-red-500'); // Add error styling
            }
        }
    }

    // Function to clear all field-specific validation errors
    function clearErrors() {
        const errorMessages = contactForm.querySelectorAll('.error-message');
        errorMessages.forEach(el => el.textContent = '');
        const errorInputs = contactForm.querySelectorAll('.border-red-500');
        errorInputs.forEach(el => el.classList.remove('border-red-500'));
    }

}); // End DOMContentLoaded


const loginForm = document.getElementById('loginForm');
const errorMessage = document.getElementById('error-message');

loginForm.addEventListener('submit', async function (event) {
    event.preventDefault();  // prevent default form submission behavior

    const username = document.getElementById('user_name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Prepare login request payload
    const payload = {
        user_name: user_name,
        email: email,
        password: password
    };

    try {
        // Send the login request to your backend API
        const response = await fetch('http://0.0.0.0:50051/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });

        // Check if login was successful
        if (response.ok) {
            const data = await response.json();

            // Store the JWT token in localStorage or sessionStorage
            localStorage.setItem('jwtToken', data.token);

            // Optionally redirect to a different page
            window.location.href = '/dashboard.html'; // or any other page
        } else {
            // Display error if login fails
            errorMessage.style.display = 'block';
        }
    } catch (error) {
        console.error('Error during login:', error);
        errorMessage.style.display = 'block';
    }
});

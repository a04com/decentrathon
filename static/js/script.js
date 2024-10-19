const tg = window.Telegram.WebApp;

let userFirstName = tg.initDataUnsafe.user.first_name;
let userLastName = tg.initDataUnsafe.user.last_name;
let userId = tg.initDataUnsafe.user.id;
let userName = tg.initDataUnsafe.user.username;
let userPhoto = tg.initDataUnsafe.user.photo_url;

document.addEventListener('DOMContentLoaded', function() {
    let infoDiv = document.querySelector('.info');
    
    infoDiv.innerHTML = `
        <p>First Name: ${userFirstName}</p>
        <p>Last Name: ${userLastName}</p>
        <p>User ID: ${userId}</p>
        <p>Username: ${userName}</p>
        <p><img src="${userPhoto}" alt="User Photo"></p>
    `;
});

// Send data to Flask backend via POST request
fetch('/auth/telegram/callback', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(userData)
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});
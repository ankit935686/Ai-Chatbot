const chatbox = document.getElementById('chatbox');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

sendBtn.addEventListener('click', () => {
    const userMessage = userInput.value.trim();
    if (!userMessage) return;

    // Display user message
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'message user';
    userMessageDiv.textContent = userMessage;
    chatbox.appendChild(userMessageDiv);

    // Clear input
    userInput.value = '';

    // Fetch response from Django API
    fetch('/api/chatbot/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage }),
    })
        .then(response => response.json())
        .then(data => {
            const botMessageDiv = document.createElement('div');
            botMessageDiv.className = 'message bot';
            botMessageDiv.textContent = data.response || 'Sorry, no response!';
            chatbox.appendChild(botMessageDiv);

            // Scroll to the bottom
            chatbox.scrollTop = chatbox.scrollHeight;
        })
        .catch(error => {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'message bot';
            errorDiv.textContent = `Error: ${error.message}`;
            chatbox.appendChild(errorDiv);
        });
});

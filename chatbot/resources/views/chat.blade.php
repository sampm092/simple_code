<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Chatbot</title>
    <style>
        #chatbox {
            width: 400px;
            height: 400px;
            border: 1px solid #ccc;
            padding: 10px;
            overflow-y: scroll;
            margin-bottom: 10px;
        }
        #userInput {
            width: 300px;
            padding: 5px;
        }
        #sendBtn {
            padding: 5px 10px;
        }
    </style>
</head>
<body>

<div id="chatbox"></div>

<input type="text" id="userInput" placeholder="Type your message...">
<button id="sendBtn">Send</button>

<script>
document.getElementById('sendBtn').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;
    if (!userInput.trim()) return;

    // Add user message to chatbox
    const chatbox = document.getElementById('chatbox');
    chatbox.innerHTML += `<div><strong>You:</strong> ${userInput}</div>`;

    // Send the message to Laravel backend
    fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': '{{ csrf_token() }}' // Important!
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatbox.innerHTML += `<div><strong>Bot:</strong> ${data.reply}</div>`;
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    document.getElementById('userInput').value = '';
});
</script>

</body>
</html>

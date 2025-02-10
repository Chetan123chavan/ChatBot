document.getElementById("start-chat").addEventListener("click", function () {
    document.getElementById("chat-container").style.display = "block";
});

document.getElementById("send-btn").addEventListener("click", async function () {
    const userInput = document.getElementById("user-input").value;
    if (!userInput.trim()) return;

    // Display user message
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class="message user">${userInput}</div>`;

    // Send message to backend (Flask)
    const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();
    const botMessage = data.response;

    // Display bot response
    chatBox.innerHTML += `<div class="message bot">${botMessage}</div>`;

    // Clear input field
    document.getElementById("user-input").value = "";
});

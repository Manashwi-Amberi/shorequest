const sendBtn = document.getElementById("send-btn")
const userInput = document.getElementById("chat-input")
const chatMessages = document.getElementById("chat-messages")

function addMessage(message, sender) {

    const messageDiv = document.createElement("div")

    messageDiv.classList.add("message")

    if(sender === "user") {
        messageDiv.classList.add("user-message")
    }
    else {
        messageDiv.classList.add("bot-message")
    }

    messageDiv.innerText = message

    chatMessages.appendChild(messageDiv)

    chatMessages.scrollTop = chatMessages.scrollHeight
}

async function sendMessage() {

    const message = userInput.value.trim()

    if(message === "") return

    addMessage(message, "user")

    userInput.value = ""

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        })

        const data = await response.json()

        addMessage(data.response, "bot")

    }

    catch(error) {

        console.error(error)

        addMessage("Backend connection failed ⚠️", "bot")
    }
}

sendBtn.addEventListener("click", sendMessage)

userInput.addEventListener("keypress", function(e){

    if(e.key === "Enter"){
        sendMessage()
    }

})
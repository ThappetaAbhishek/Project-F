import { useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Hello! I am Project F."
    }
  ]);

  async function sendMessage() {
    if (!message.trim()) return;

    const userMessage = message;

    setMessages(prev => [
      ...prev,
      {
        sender: "user",
        text: userMessage
      }
    ]);

    setMessage("");

    try {
      const response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message: userMessage
        })
      });

      const data = await response.json();

      setMessages(prev => [
        ...prev,
        {
          sender: "bot",
          text: data.reply
        }
      ]);
    } catch (error) {
      setMessages(prev => [
        ...prev,
        {
          sender: "bot",
          text: "Unable to connect to Project F."
        }
      ]);
    }
  }

  return (
    <div className="app">

      <h1>🤖 Project F</h1>

      <div className="chat-window">

        {messages.map((msg, index) => (
          <div
            key={index}
            className={msg.sender}
          >
            {msg.text}
          </div>
        ))}

      </div>

      <div className="input-area">

        <input
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask me anything..."
          onKeyDown={(e) => {
            if (e.key === "Enter") sendMessage();
          }}
        />

        <button onClick={sendMessage}>
          Send
        </button>

      </div>

    </div>
  );
}

export default App;
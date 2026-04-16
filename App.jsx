// 


import { useState, useEffect } from "react";
import Sidebar from "./components/Sidebar";
import ChatHeader from "./components/Chatheader";
import MessageList from "./components/MessageList";
import MessageInput from "./components/MessageInput";
import { chatUsers } from "./data/chats";

const API_URL = "http://127.0.0.1:8000";

export default function App() {
  const [selectedUser, setSelectedUser] = useState(chatUsers[0]);
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetch messages from backend on load
  useEffect(() => {
    fetchMessages();
  }, []);

  const fetchMessages = async () => {
    try {
      const res = await fetch(`${API_URL}/messages/`);
      const data = await res.json();

      // Map backend fields to frontend format
      const formatted = data.map((msg) => ({
        id: msg.id,
        text: msg.content,
        sender: msg.sender,
        time: new Date(msg.timestamp).toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        }),
      }));

      setMessages(formatted);
    } catch (err) {
      console.error("Failed to fetch messages:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleSendMessage = async (newMessage) => {
    if (!newMessage.trim()) return;

    try {
      const res = await fetch(
        `${API_URL}/messages/?content=${encodeURIComponent(newMessage)}&sender=me`,
        { method: "POST" }
      );

      const data = await res.json();

      // Add new message to state
      setMessages((prev) => [
        ...prev,
        {
          id: data.id,
          text: data.content,
          sender: data.sender,
          time: new Date(data.timestamp).toLocaleTimeString([], {
            hour: "2-digit",
            minute: "2-digit",
          }),
        },
      ]);
    } catch (err) {
      console.error("Failed to send message:", err);
    }
  };

  return (
    <div className="app">
      <Sidebar
        users={chatUsers}
        selectedUser={selectedUser}
        setSelectedUser={setSelectedUser}
      />

      <div className="chat-section">
        <ChatHeader user={selectedUser} />
        {loading ? (
          <p style={{ padding: "1rem" }}>Loading messages...</p>
        ) : (
          <MessageList messages={messages} />
        )}
        <MessageInput onSend={handleSendMessage} />
      </div>
    </div>
  );
}
export default function MessageBubble({ message }) {
  return (
    <div className={`message-row ${message.sender === "me" ? "me" : "other"}`}>
      <div className={`message-bubble ${message.sender === "me" ? "sent" : "received"}`}>
        <p>{message.text}</p>
        <span>{message.time}</span>
      </div>
    </div>
  );
}
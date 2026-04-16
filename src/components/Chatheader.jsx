export default function ChatHeader({ user }) {
  return (
    <div className="chat-header">
      <div className="chat-user">
        <img src={user.avatar} alt={user.name} className="avatar" />
        <div>
          <h3>{user.name}</h3>
          <span>online</span>
        </div>
      </div>
    </div>
  );
}
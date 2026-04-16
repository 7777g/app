export default function Sidebar({ users, selectedUser, setSelectedUser }) {
  return (
    <div className="sidebar">
      <div className="sidebar-header">Chats</div>

      <div className="chat-list">
        {users.map((user) => (
          <div
            key={user.id}
            className={`chat-item ${selectedUser.id === user.id ? "active" : ""}`}
            onClick={() => setSelectedUser(user)}
          >
            <img src={user.avatar} alt={user.name} className="avatar" />
            <div className="chat-info">
              <div className="chat-top">
                <h4>{user.name}</h4>
                <span>{user.time}</span>
              </div>
              <p>{user.lastMessage}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
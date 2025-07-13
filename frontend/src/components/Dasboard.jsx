import React, { useEffect, useState } from "react";
import axios from "../axios";

export default function Dashboard() {
  const [user, setUser] = useState(null);
  const [bots, setBots] = useState([]);
  const [name, setName] = useState("");
  const [token, setToken] = useState("");
  const [msg, setMsg] = useState("");

  useEffect(() => {
    axios.get("/users/").then(res => setUser(res.data[0])).catch(() => {});
    axios.get("/bots?user_id=1").then(res => setBots(res.data)).catch(() => {});
    // user_id=1 для демо, в реальной системе брать из токена
  }, []);

  const handleAddBot = async e => {
    e.preventDefault();
    try {
      await axios.post("/bots", { name, telegram_token: token, user_id: 1 });
      setMsg("Бот добавлен!");
      setName(""); setToken("");
      const res = await axios.get("/bots?user_id=1");
      setBots(res.data);
    } catch {
      setMsg("Ошибка добавления бота");
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto" }}>
      <h2>Панель управления</h2>
      {user && <div>Привет, {user.email}</div>}
      <hr />
      <h3>Мои Telegram-боты</h3>
      <ul>
        {bots.map(b => (
          <li key={b.id}>{b.name} — <code>{b.telegram_token.slice(0, 8)}...</code></li>
        ))}
      </ul>
      <form onSubmit={handleAddBot} style={{ marginTop: 16 }}>
        <input value={name} onChange={e => setName(e.target.value)} placeholder="Название бота" required />
        <input value={token} onChange={e => setToken(e.target.value)} placeholder="Telegram token" required />
        <button type="submit">Добавить бота</button>
      </form>
      {msg && <div>{msg}</div>}
    </div>
  );
}

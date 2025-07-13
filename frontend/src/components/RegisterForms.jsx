import React, { useState } from "react";
import axios from "../axios";

export default function RegisterForm({ onRegister }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");

  const handleRegister = async e => {
    e.preventDefault();
    try {
      await axios.post("/register", { email, password });
      setMsg("Регистрация успешна! Выполните вход.");
      onRegister();
    } catch (err) {
      setMsg("Ошибка регистрации");
    }
  };

  return (
    <form onSubmit={handleRegister} style={{ marginBottom: 24 }}>
      <h2>Регистрация</h2>
      <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" required />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Пароль" required />
      <button type="submit">Зарегистрироваться</button>
      {msg && <div>{msg}</div>}
    </form>
  );
}

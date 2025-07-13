import React, { useState } from "react";
import axios from "axios";

export default function LoginForm({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async e => {
    e.preventDefault();
    try {
      const res = await axios.post("/login", { email, password });
      localStorage.setItem("access_token", res.data.access_token);
      onLogin();
    } catch (err) {
      setError("Ошибка входа");
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <h2>Вход</h2>
      <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Пароль" />
      <button type="submit">Войти</button>
      {error && <div>{error}</div>}
    </form>
  );
}

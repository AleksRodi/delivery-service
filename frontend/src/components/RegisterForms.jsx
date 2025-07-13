import React, { useState } from "react";
import axios from "axios";

export default function RegisterForm({ onRegister }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleRegister = async e => {
    e.preventDefault();
    try {
      await axios.post("/register", { email, password });
      onRegister();
    } catch (err) {
      setError("Ошибка регистрации");
    }
  };

  return (
    <form onSubmit={handleRegister}>
      <h2>Регистрация</h2>
      <input value={email} onChange={e => setEmail(e.target.value)} placeholder="Email" />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Пароль" />
      <button type="submit">Зарегистрироваться</button>
      {error && <div>{error}</div>}
    </form>
  );
}

import React, { useState } from "react";
import RegisterForm from "./components/RegisterForm";
import LoginForm from "./components/LoginForm";
import Dashboard from "./components/Dashboard";

export default function App() {
  const [isAuth, setAuth] = useState(!!localStorage.getItem("access_token"));

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    setAuth(false);
  };

  if (!isAuth) {
    return (
      <div style={{ maxWidth: 400, margin: "2rem auto" }}>
        <RegisterForm onRegister={() => setAuth(true)} />
        <LoginForm onLogin={() => setAuth(true)} />
      </div>
    );
  }

  return (
    <div>
      <button style={{ float: "right" }} onClick={handleLogout}>Выйти</button>
      <Dashboard />
    </div>
  );
}

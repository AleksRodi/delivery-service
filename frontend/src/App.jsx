import React, { useState } from "react";
import RegisterForm from "./components/RegisterForm";
import LoginForm from "./components/LoginForm";
import Dashboard from "./components/Dashboard"; // ваша админка

export default function App() {
  const [isAuth, setAuth] = useState(!!localStorage.getItem("access_token"));
  if (!isAuth) {
    return (
      <>
        <RegisterForm onRegister={() => setAuth(true)} />
        <LoginForm onLogin={() => setAuth(true)} />
      </>
    );
  }
  return <Dashboard />;
}

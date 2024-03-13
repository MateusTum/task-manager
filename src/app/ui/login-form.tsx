"use client";

import { useState, FormEvent } from "react";

const LoginForm = () => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const handleLoginSuccess = () => {
    console.log("Login successful");
  };

  const handleLogin = async (e: FormEvent) => {
    e.preventDefault();

    const response = await fetch(
      `${process.env.NEXT_PUBLIC_API_URL}/auth/login/`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      }
    );

    if (response.ok) {
      // Handle successful login here
      handleLoginSuccess();
    } else {
      // Handle login failure here
      console.error("Login failed");
    }
  };

  return (
    <form onSubmit={handleLogin} className="flex flex-col space-y-4">
      <div>
        <label htmlFor="username" className="text-md font-medium text-white">
          Username
        </label>
        <input
          id="username"
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="mt-1 w-full rounded-md border-blue-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          required
        />
      </div>
      <div>
        <label htmlFor="password" className="text-md font-medium text-white">
          Password
        </label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="mt-1 w-full rounded-md border-blue-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
          required
        />
      </div>
      <button
        type="submit"
        className="rounded-md bg-blue-600 py-2 px-4 text-md font-medium text-white shadow hover:bg-blue-800 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
      >
        Login
      </button>
    </form>
  );
};

export default LoginForm;

"use client";

import { useState, useEffect } from "react";
import { loginUser } from "@/services/authService";
import { useRouter } from "next/navigation";
import Link from "next/link";

export default function LoginPage() {

  const router = useRouter();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // ADD THIS HERE
  useEffect(() => {

    const token =
      localStorage.getItem("access_token");

    if (token) {

      router.push("/dashboard");

    }

  }, [router]);


  const handleLogin = async () => {

    try {

      const data =
        await loginUser(email, password);

      localStorage.setItem(
        "access_token",
        data.access_token
      );

      router.push("/dashboard");

    } catch {

      alert("Login failed");

    }

  };

  return (

    <div className="flex items-center justify-center min-h-screen bg-gray-900">

      <div className="bg-gray-800 p-8 rounded-lg shadow-lg w-96">

        <h2 className="text-2xl font-bold text-white mb-6 text-center">
          Login
        </h2>

        <input
          type="email"
          placeholder="Email"
          className="w-full p-2 mb-4 rounded bg-gray-700 text-white"
          onChange={(e)=>setEmail(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          className="w-full p-2 mb-4 rounded bg-gray-700 text-white"
          onChange={(e)=>setPassword(e.target.value)}
        />

        <button
          onClick={handleLogin}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white p-2 rounded"
        >
          Login
        </button>

        <p className="text-gray-400 mt-4 text-center">

          No account?{" "}

          <Link href="/register" className="text-blue-400">
            Register
          </Link>

        </p>

      </div>

    </div>

  );

}

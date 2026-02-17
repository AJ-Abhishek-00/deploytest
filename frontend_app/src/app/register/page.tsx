"use client";

import { useState } from "react";
import { registerUser } from "@/services/authService";
import { useRouter } from "next/navigation";
import Link from "next/link";

export default function RegisterPage() {

  const router = useRouter();

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {

    try {

      await registerUser(
        name,
        email,
        password
      );

      alert("Registration successful");

      router.push("/login");

    } catch {

      alert("Registration failed");

    }

  };

  return (

    <div className="flex items-center justify-center min-h-screen bg-gray-900">

      <div className="bg-gray-800 p-8 rounded-lg shadow-lg w-96">

        <h2 className="text-2xl font-bold text-white mb-6 text-center">
          Register
        </h2>

        <input
          placeholder="Full Name"
          className="w-full p-2 mb-4 rounded bg-gray-700 text-white"
          onChange={(e)=>setName(e.target.value)}
        />

        <input
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
          onClick={handleRegister}
          className="w-full bg-green-600 hover:bg-green-700 text-white p-2 rounded"
        >
          Register
        </button>

        <p className="text-gray-400 mt-4 text-center">

          Already have account?{" "}

          <Link href="/login"
            className="text-blue-400">
            Login
          </Link>

        </p>

      </div>

    </div>

  );

}

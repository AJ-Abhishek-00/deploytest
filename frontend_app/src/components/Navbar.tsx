"use client";

import { useRouter } from "next/navigation";
import { useTheme } from "@/hooks/useTheme";

export default function Navbar() {

  const router = useRouter();

  const { theme, toggleTheme } =
    useTheme();

  const logout = () => {

    localStorage.removeItem(
      "access_token"
    );

    router.push("/login");

  };

  return (

    <div className="bg-gray-200 dark:bg-gray-800 text-black dark:text-white p-4 shadow flex justify-between">


      <h1 className="text-xl font-bold">
        Dashboard
      </h1>

      <div className="flex gap-3">

        <button
          onClick={toggleTheme}
          className="bg-blue-500 px-4 py-2 rounded text-white"
        >
          {theme === "dark"
            ? "Light"
            : "Dark"}
        </button>

        <button
          onClick={logout}
          className="bg-red-500 px-4 py-2 rounded text-white"
        >
          Logout
        </button>

      </div>

    </div>

  );

}

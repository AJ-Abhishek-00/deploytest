"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

export default function Sidebar() {

  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {

    const token =
      localStorage.getItem("access_token");

    setIsLoggedIn(!!token);

  }, []);

  return (

    <div className="w-64 bg-gray-200 dark:bg-gray-800 text-black dark:text-white min-h-screen p-4">



    

        <div className="mb-4 hover:text-blue-400 cursor-pointer">
          Profile
        </div>

      {/* Show only if NOT logged in */}
      {!isLoggedIn && (

        <>
          <Link href="/login">

            <div className="mb-4 hover:text-blue-400 cursor-pointer">
              Login
            </div>

          </Link>

          <Link href="/register">

            <div className="mb-4 hover:text-blue-400 cursor-pointer">
              Register
            </div>

          </Link>
        </>

      )}

    </div>

  );

}

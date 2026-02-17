"use client";

import { useEffect, useState } from "react";

export function useTheme() {

  const [theme, setTheme] =
    useState("dark");

  useEffect(() => {

    const savedTheme =
      localStorage.getItem("theme") || "dark";

    setTheme(savedTheme);

    document.documentElement.classList.toggle(
      "dark",
      savedTheme === "dark"
    );

  }, []);

  const toggleTheme = () => {

    const newTheme =
      theme === "dark" ? "light" : "dark";

    localStorage.setItem("theme", newTheme);

    document.documentElement.classList.toggle("dark");

    setTheme(newTheme);

  };

  return { theme, toggleTheme };

}

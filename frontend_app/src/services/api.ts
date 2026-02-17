import axios from "axios";

const BASE_URL =
  process.env.NEXT_PUBLIC_API_URL ||
  "http://127.0.0.1:8000";

export const api = axios.create({
  baseURL: BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});


// Automatically attach token
api.interceptors.request.use((config) => {

  const token =
    localStorage.getItem("access_token");

  if (token) {

    config.headers.Authorization =
      `Bearer ${token}`;

  }

  return config;

});

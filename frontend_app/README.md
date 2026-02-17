
# Frontend Development Assignment – Round 3

## Overview

This project is a scalable, production-ready frontend application built using **Next.js, TypeScript, and TailwindCSS**, implementing authentication, dashboard layout, and advanced product listing with **cursor-based pagination, search, sorting, and filtering**.

The application follows a **clean architecture and feature-based folder structure**, ensuring maintainability, scalability, and separation of concerns.

This frontend integrates with a FastAPI backend using a centralized API service layer.

---

## Tech Stack

| Technology               | Purpose                |
| ------------------------ | ---------------------- |
| Next.js (App Router)     | Frontend framework     |
| React                    | UI rendering           |
| TypeScript               | Type safety            |
| TailwindCSS              | Styling                |
| Axios                    | API communication      |
| Zustand (optional ready) | State management       |
| FastAPI Backend          | Data provider          |
| Cursor-based Pagination  | Efficient data loading |

---

## Features Implemented

### Authentication

**Login Page**

* Email and password validation
* Error handling
* Secure JWT storage in localStorage
* Redirect to dashboard after login

**Registration Page**

* Full Name
* Email validation
* Password validation
* Confirm password validation
* Redirect after successful registration

---

### Dashboard

Includes:

* Navbar with:

  * Logout
  * Dark/Light mode toggle

* Sidebar navigation

* Summary metric cards

* Product listing table

---

### Product Listing Page (Core Requirement)

Fully implemented advanced product management:

✔ Cursor-based pagination
✔ Previous and Next navigation
✔ Search functionality
✔ Category filtering
✔ Sorting (price, rating, created date)
✔ Combined filtering + sorting + pagination
✔ Backend API integration
✔ Dynamic cursor handling

---

## Cursor Pagination Logic

Instead of page numbers, cursor-based pagination uses a unique cursor returned by backend.

Example backend response:

```
{
  data: [...],
  next_cursor: "encoded_cursor_value",
  has_more: true
}
```

Frontend stores cursor history:

```
Page 1 cursor: undefined
Page 2 cursor: cursor_A
Page 3 cursor: cursor_B
```

Navigation works using cursor history stack.

Benefits:

* High performance
* No offset inefficiency
* Scales to millions of records

---

## Folder Structure

```
src/
│
├── app/
│   ├── login/
│   ├── register/
│   ├── dashboard/
│   └── layout.tsx
│
├── features/
│   └── products/
│       ├── components/
│       │   └── ProductTable.tsx
│       ├── services.ts
│       ├── types.ts
│       └── index.ts
│
├── components/
│   ├── Navbar.tsx
│   ├── Sidebar.tsx
│   └── SummaryCards.tsx
│
├── services/
│   ├── api.ts
│   ├── authService.ts
│   └── productService.ts
│
├── hooks/
│   └── useTheme.ts
│
├── store/
│   └── index.ts
│
├── types/
│   ├── product.ts
│   ├── auth.ts
│   └── index.ts
│
├── utils/
│   └── constants.ts
│
└── styles/
    └── globals.css
```

---

## Architecture Explanation

### Feature-Based Architecture

Each feature contains:

* Components
* Services
* Types
* Hooks

Benefits:

* Modular
* Scalable
* Easy maintenance

---

### API Layer

Centralized API client:

```
src/services/api.ts
```

Handles:

* Base URL
* Token injection
* Request handling

Example:

```ts
export const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
});
```

---

## Environment Variables

Create:

```
.env.local
```

Example:

```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

For production:

```
NEXT_PUBLIC_API_URL=https://your-backend-url.com
```

---

## Dark Mode Support

Fully implemented dark/light theme:

* Persistent theme storage
* Tailwind dark mode integration
* Toggle via Navbar

---

## Setup Instructions

### 1. Clone Repository

```
git clone <repository-url>
```

---

### 2. Install Dependencies

```
npm install
```

---

### 3. Setup Environment Variables

Create:

```
.env.local
```

Add:

```
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

---

### 4. Run Development Server

```
npm run dev
```

App runs at:

```
http://localhost:3000
```

---

## Backend Requirement

Backend must be running at:

```
http://127.0.0.1:8000
```

Required endpoints:

```
POST /auth/login
POST /auth/register
GET /products
```

---

## Pagination Implementation Details

Frontend stores cursor history:

```
cursorHistory = [
  undefined,
  cursor_A,
  cursor_B
]
```

Navigation logic:

```
Next → use next_cursor
Previous → use previous cursor from history
```

---

## Best Practices Followed

✔ Feature-based structure
✔ Separation of concerns
✔ Reusable components
✔ Cursor-based pagination
✔ Type safety
✔ Clean code principles
✔ Scalable architecture
✔ API abstraction layer

---

## Assumptions Made

* Backend provides cursor-based pagination
* Backend returns valid cursor values
* JWT authentication used

---

## Time Taken

Approximate time spent:

```
8–12 hours
```

Includes:

* Architecture setup
* Pagination logic
* API integration
* UI development
* Debugging
* Optimization

---

## Future Improvements

Possible enhancements:

* Unit testing
* Zustand global state
* Loading skeleton UI
* Error boundary handling
* Role-based authentication
* API caching

---

## Deployment Ready

Frontend can be deployed on:

* Vercel
* Netlify

Backend can be deployed on:

* Render
* Railway
* AWS

Only environment variable change required.

---

## Conclusion

This project demonstrates:

* Scalable frontend architecture
* Cursor-based pagination implementation
* Proper separation of concerns
* Production-ready Next.js application

The system is designed to be maintainable, extensible, and efficient.

---

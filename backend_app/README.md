# Backend Development Assignment – FastAPI (Round 3)

## Overview

This project is a production-ready backend API built using FastAPI that demonstrates clean architecture, secure authentication, cursor-based pagination, and scalable service-layer design.

The implementation follows industry best practices including modular architecture, separation of concerns, JWT authentication, structured logging, and comprehensive testing.

This backend supports authentication, product management, and dashboard analytics with real cursor-based pagination.

---

## Tech Stack

Component: Framework  
Technology: FastAPI  

Component: Database  
Technology: SQLite  

Component: ORM  
Technology: SQLAlchemy  

Component: Authentication  
Technology: JWT (python-jose)  

Component: Password Hashing  
Technology: bcrypt + passlib  

Component: Testing  
Technology: pytest  

Component: Containerization  
Technology: Docker  

Component: Validation  
Technology: Pydantic  

Component: Language  
Technology: Python 3.11  

---

## Key Features Implemented

### Authentication & Security

- User Registration with hashed password
- User Login with JWT access token and refresh token
- OAuth2 compatible token endpoint
- Protected routes using dependency injection
- Password hashing using bcrypt
- Token validation and expiry handling

Endpoints:

POST /auth/register  
POST /auth/login  
POST /auth/token  
GET /auth/me  

---

### Product Management

Full CRUD operations implemented with clean service-layer separation.

Product fields:

id  
name  
category  
price  
rating  
created_at  

Endpoints:

POST /products  
GET /products  
GET /products/{id}  
PUT /products/{id}  
DELETE /products/{id}  

Soft delete is implemented to preserve data integrity.

---

### Cursor-Based Pagination (Core Requirement)

Implemented real cursor-based pagination using Base64-encoded opaque cursors.

Features:

- No offset-based pagination used
- Stable ordering using created_at and id
- Base64 encoded opaque cursor
- next_cursor returned in response
- has_more flag returned
- page size validation enforced

Supported filters:

search → search by product name  
category → filter by category  
min_price → minimum price filter  
max_price → maximum price filter  
sort_by → price, rating, created_at  
sort_order → asc, desc  
limit → page size  
cursor → opaque pagination cursor  

Example response:

{
  "data": [...],
  "next_cursor": "opaque_cursor",
  "has_more": true
}

---

### Dashboard Analytics

Provides aggregated analytics using efficient SQLAlchemy queries.

Endpoint:

GET /dashboard/summary  

Returns:

- Total products count
- Average product rating
- Highest priced product
- Recently added products (limit 5)

Example:

{
  "total_products": 10,
  "average_rating": 4.5,
  "highest_priced_product": {...},
  "recent_products": [...]
}

---

## Project Architecture

This project follows layered architecture and separation of concerns.

backend_app/  
│  
├── config/ → centralized configuration  
│  
├── src/  
│   ├── core/ → database, security, middleware  
│   ├── modules/  
│   │   ├── auth/  
│   │   ├── user/  
│   │   ├── product/  
│   │   └── dashboard/  
│   ├── utils/ → pagination helpers  
│   ├── app.py  
│   └── main.py  
│  
├── tests/ → unit, integration, e2e tests  
├── data/ → SQLite database  
├── logs/ → application logs  
│  
├── Dockerfile  
├── requirements.txt  
├── pyproject.toml  
├── README.md  

Architecture principles followed:

- Thin routers  
- Service-layer business logic  
- Centralized database session management  
- Modular domain-based structure  

---

## Authentication Flow

1. User registers with email and password  
2. Password is hashed using bcrypt  
3. User logs in and receives JWT access token and refresh token  
4. Access token is used to access protected routes  
5. Token is validated using dependency injection  

JWT payload contains:

user_id  
expiration timestamp  

---

## Cursor Pagination Implementation Details

Cursor contains encoded values of:

created_at  
id  

Encoded using Base64 to create opaque cursor.

Pagination query uses:

WHERE (created_at, id) < cursor_values  
ORDER BY created_at DESC, id DESC  
LIMIT page_size  

This ensures:

- Stable pagination  
- No skipped records  
- No duplicate records  
- High performance at scale  

---

## Testing

Implemented using pytest with structured test layers:

tests/  
├── unit/  
├── integration/  
└── e2e/  

Test coverage includes:

- Authentication flow  
- JWT token creation and validation  
- Product queries  
- Pagination behavior  
- Dashboard analytics  
- Full end-to-end flow  

Run tests:

python -m pytest  

---

## Running the Application

Install dependencies:

pip install -r requirements.txt  

Start server:

python -m src.main  

Access Swagger:

http://127.0.0.1:8000/docs  

---

## Docker Support

Build container:

docker build -t backend-app .  

Run container:

docker run -p 8000:8000 backend-app  

---

## Database

SQLite is used for simplicity and portability.

Database file:

data/database.db  

Tables are automatically created at startup.

---

## Security Best Practices Implemented

- Password hashing (bcrypt)  
- JWT token authentication  
- Token expiry validation  
- No plaintext password storage  
- Modular security implementation  

---

## Assumptions Made

- SQLite used for assignment simplicity  
- Soft delete implemented logically  
- Cursor pagination uses created_at and id  
- Role system implemented for future extensibility  

---

## Time Taken

Approximately 12–15 hours including:

- Architecture design  
- Implementation  
- Pagination logic  
- Testing  
- Documentation  

---

## Highlights

- Clean modular architecture  
- Real cursor-based pagination  
- JWT authentication system  
- Service-layer separation  
- Comprehensive testing  
- Docker-ready deployment  
- Production-grade backend design  

---

## Author

Abhishek  

Backend Assignment Submission – Round 3  

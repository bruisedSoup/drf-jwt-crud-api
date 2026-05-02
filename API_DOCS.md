# Django REST Framework Items API Usage Guide

JWT-protected CRUD API for `Item` records, serving as the backend for the React frontend.


### Authentication

- `POST /api/token/` returns JWT `access` and `refresh` tokens.
- `POST /api/token/refresh/` returns a new access token.
- Item endpoints use `IsAuthenticated`, so requests without a valid token are blocked.

### CRUD Endpoints

- `GET /api/items/` list items
- `POST /api/items/` create item
- `GET /api/items/<id>/` get one item
- `PUT /api/items/<id>/` full update
- `PATCH /api/items/<id>/` partial update
- `DELETE /api/items/<id>/` delete item

## Required Postman or Thunder Client Test Flow

Follow this exact order for your testing.

### 1. Prove unauthenticated access is blocked

Request:

- Method: `GET`
- URL: `http://127.0.0.1:8000/api/items/`
- Headers: none

Expected response:

```json
{
  "detail": "Authentication credentials were not provided."
}
```

Expected status: `401 Unauthorized`

### 2. Log in and get a JWT token

Request:

- Method: `POST`
- URL: `http://127.0.0.1:8000/api/token/`
- Header: `Content-Type: application/json`

Body:

```json
{
  "username": "superuser",
  "password": "superuser123"
}
```

Expected response:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

Expected status: `200 OK`

### 3. Add the token to later requests

Header for protected endpoints:

```text
Authorization: Bearer your_access_token
```

### 4. Create an item

Request:

- Method: `POST`
- URL: `http://127.0.0.1:8000/api/items/`
- Headers:
  - `Content-Type: application/json`
  - `Authorization: Bearer your_access_token`

Body:

```json
{
  "name": "Mechanical Keyboard",
  "description": "A clicky 80% mechanical keyboard",
  "price": "89.99",
  "quantity": 25
}
```

Expected status: `201 Created`

### 5. Read all items

Request:

- Method: `GET`
- URL: `http://127.0.0.1:8000/api/items/`
- Header: `Authorization: Bearer your_access_token`

Expected status: `200 OK`

### 6. Read one item

Request:

- Method: `GET`
- URL: `http://127.0.0.1:8000/api/items/1/`
- Header: `Authorization: Bearer your_access_token`

Expected status: `200 OK`

### 7. Full update with PUT

Request:

- Method: `PUT`
- URL: `http://127.0.0.1:8000/api/items/1/`
- Headers:
  - `Content-Type: application/json`
  - `Authorization: Bearer your_access_token`

Body:

```json
{
  "name": "Wonu Mechanical Keyboard Pro",
  "description": "RGB version",
  "price": "129.99",
  "quantity": 10
}
```

Expected status: `200 OK`

### 8. Partial update with PATCH

Request:

- Method: `PATCH`
- URL: `http://127.0.0.1:8000/api/items/1/`
- Headers:
  - `Content-Type: application/json`
  - `Authorization: Bearer your_access_token`

Body:

```json
{
  "price": "99.99"
}
```

Expected status: `200 OK`

### 9. Delete the item

Request:

- Method: `DELETE`
- URL: `http://127.0.0.1:8000/api/items/1/`
- Header: `Authorization: Bearer your_access_token`

Expected response:

```json
{
  "message": "Item 'Mechanical Keyboard Pro' has been deleted successfully."
}
```

Expected status: `200 OK`

## Endpoint Reference

| Method | Endpoint | Auth Required | Purpose |
|---|---|---|---|
| `POST` | `/api/token/` | No | Get JWT access and refresh tokens |
| `POST` | `/api/token/refresh/` | No | Refresh an expired access token |
| `GET` | `/api/items/` | Yes | List all items |
| `POST` | `/api/items/` | Yes | Create an item |
| `GET` | `/api/items/<id>/` | Yes | Retrieve one item |
| `PUT` | `/api/items/<id>/` | Yes | Replace all editable fields |
| `PATCH` | `/api/items/<id>/` | Yes | Update selected fields |
| `DELETE` | `/api/items/<id>/` | Yes | Delete an item |

## Item Input Fields

| Field | Type | Required | Notes |
|---|---|---|---|
| `name` | string | Yes | Maximum 200 characters |
| `description` | string | No | Can be blank or `null` |
| `price` | decimal string | Yes | Cannot be negative |
| `quantity` | integer | No | Defaults to `0`; cannot be negative |

Do not send these fields in create or update requests:

- `id`
- `created_at`
- `updated_at`

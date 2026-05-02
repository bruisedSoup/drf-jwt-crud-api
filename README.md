# Django REST Framework Items API

This project is a Django-based CRUD web service integrated with a MySQL database, designed to manage item records through JSON-based HTTP API endpoints protected by JWT authentication.

## Tech Stack
- **Backend**: Django 5.0.4 (Python 3.11+)
- **API Framework**: Django REST Framework
- **Authentication**: Simple JWT
- **Database**: MySQL 8.0 (via `mysqlclient` / `PyMySQL`)
- **CORS**: `django-cors-headers`
- **API Testing**: Postman / Thunder Client

## Project Structure
```text
django_items_api/
│
├── items/                   # Core application logic
│   ├── models.py            # Item database schema
│   ├── serializers.py       # Data validation & JSON conversion
│   ├── views.py             # CRUD logic & authentication logic
│   └── urls.py              # API route definitions for items
├── items_project/           # Global project configuration
│   ├── settings.py          # Database, JWT, and CORS settings
│   └── urls.py              # Root routing (auth & API paths)
├── manage.py                # Django CLI tool
└── requirements.txt         # Python backend dependencies
```

## API Endpoints
| Method | URL | Action | Auth Required |
|---|---|---|---|
| `POST` | `/api/token/` | Get JWT access and refresh tokens | No |
| `POST` | `/api/token/refresh/` | Refresh an expired access token | No |
| `GET` | `/api/items/` | Retrieve all items | Yes |
| `POST` | `/api/items/` | Create a new item | Yes |
| `GET` | `/api/items/<id>/` | Retrieve one item by ID | Yes |
| `PUT` | `/api/items/<id>/` | Full update of an item by ID | Yes |
| `PATCH`| `/api/items/<id>/` | Partial update of an item by ID | Yes |
| `DELETE`| `/api/items/<id>/` | Delete an item by ID | Yes |

## How to Clone and Run
Follow these steps to set up the backend server.

**Prerequisites**
- Python 3.11+
- MySQL 8.0
- Git

**Step 1 — Clone the repository**
```powershell
git clone https://github.com/bruisedSoup/drf-items-api.git
cd drf-items-api
```

**Step 2 — Create and activate a virtual environment**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Step 3 — Install dependencies**
```powershell
pip install -r requirements.txt
```

**Step 4 — Create the MySQL database**
```sql
CREATE DATABASE django_items_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Step 5 — Update settings.py**
Ensure your MySQL `PASSWORD` is correct in `items_project/settings.py`.

**Step 6 — Run migrations**
```powershell
python manage.py migrate
```

**Step 7 — Start the server**
```powershell
python manage.py runserver
```

The server runs at: `http://127.0.0.1:8000`

## Frontend Repository
The companion React frontend for this API can be found here:
[drf-react-auth](https://github.com/bruisedSoup/drf-react-auth)



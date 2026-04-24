# Django REST Framework Items API

This project is a Django-based CRUD web service integrated with a MySQL database, designed to manage item records through JSON-based HTTP API endpoints protected by JWT authentication.

## Project Requirements
The application meets the following functional and technical requirements:

- **Framework**: The project is built using the Django web framework (version 5.0.4) and Django REST Framework for API construction.
- **Authentication**: Uses `djangorestframework-simplejwt` to secure endpoints. All item operations require a valid JWT bearer token.
- **Database Configuration**: The Django project is configured to use MySQL as the backend database (`django_items_db`), with proper connection settings defined in `settings.py`.
- **Application & Model**: A Django application (`items`) has been created containing a model (`Item`) that defines a database table with the fields: `name`, `description`, `price`, `quantity`, `created_at`, and `updated_at`.
- **Migrations**: Database migrations successfully create the `items` table in MySQL.
- **JSON Request & Response Handling**: All client requests must be sent in JSON format. The server uses Django REST Framework serializers to parse and validate incoming JSON data. All responses are returned strictly in valid JSON format.
- **Complete CRUD Functionality**:
  - **Create** (`POST /api/items/`): Accepts JSON body and inserts a new item record.
  - **Retrieve All** (`GET /api/items/`): Returns all item records as JSON.
  - **Retrieve One** (`GET /api/items/<id>/`): Returns a single item record by ID as JSON.
  - **Update** (`PUT /api/items/<id>/` and `PATCH /api/items/<id>/`): Accepts JSON body and updates an existing item record.
  - **Delete** (`DELETE /api/items/<id>/`): Removes an item record.
- **Error Handling**: Proper JSON-based error responses are returned for all failure cases (e.g., unauthorized `401`, not found `404`, bad request `400`).
- **URL Routing**: Routing is configured in `items_project/urls.py` and `items/urls.py`.

## Tech Stack
- **Backend**: Django 5.0.4 (Python 3.11+)
- **API Framework**: Django REST Framework
- **Authentication**: Simple JWT
- **Database**: MySQL 8.0 (via `mysqlclient` / `PyMySQL`)
- **CORS**: `django-cors-headers`
- **API Testing**: Postman / Thunder Client

## Project Structure
```text
items_project/
│
├── manage.py                    # Django command-line utility
├── requirements.txt             # Python package dependencies
├── .gitignore                   # Files excluded from version control
├── README.md                    # Project documentation (this file)
├── API_DOCS.md                  # Detailed API usage and testing guide
│
├── items_project/               # Django project configuration package
│   ├── __init__.py              
│   ├── settings.py              # Settings: MySQL config, DRF, JWT, CORS
│   ├── urls.py                  # Root URL config → routes /api/ to items app and token auth
│   └── wsgi.py                  # WSGI entry point
│
└── items/                       # Django application — core of the project
    ├── __init__.py              
    ├── apps.py                  
    ├── admin.py                 
    ├── models.py                # Item model → maps to MySQL table
    ├── serializers.py           # Data validation and JSON serialization
    ├── views.py                 # Protected CRUD logic
    ├── urls.py                  # URL patterns for item API endpoints
    └── tests.py                 # Automated tests for auth and CRUD
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

## How to Clone and Run (School Lab Setup)
Follow these steps exactly if you are setting up this project on a new machine such as a school laboratory computer.

**Prerequisites — install these first if not already installed**
- Python 3.11 or 3.12 → https://www.python.org/downloads/
- MySQL 8.0 → https://dev.mysql.com/downloads/installer/ (or via XAMPP)
- Git → https://git-scm.com/downloads

**Step 1 — Open Command Prompt**
Press `Win + R` → type `cmd` or `powershell` → press Enter.

**Step 2 — Clone the repository**
```powershell
cd Desktop
git clone https://github.com/YOUR_USERNAME/django-items-api.git
cd django-items-api
```
Replace `YOUR_USERNAME` with the actual GitHub username.

**Step 3 — Create and activate a virtual environment**
```powershell
python -m venv venv
venv\Scripts\activate
```
Your prompt should now start with `(venv)`.

**Step 4 — Install dependencies**
```powershell
pip install -r requirements.txt
```

**Step 5 — Create the MySQL database**
Open MySQL Command Line Client or phpMyAdmin, enter your root password, then run:
```sql
CREATE DATABASE django_items_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

**Step 6 — Update the database password in settings.py**
Open `items_project/settings.py` and update the `PASSWORD` field to match the MySQL root password on this machine:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_items_db',
        'USER': 'root',
        'PASSWORD': 'your_mysql_password_here',   # ← change this
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

**Step 7 — Run migrations**
```powershell
python manage.py makemigrations
python manage.py migrate
```

**Step 8 — Create admin superuser (optional)**
```powershell
python manage.py createsuperuser
```

**Step 9 — Start the server**
```powershell
python manage.py runserver
```

**Step 10 — Test the API**
See `API_DOCS.md` (or `API_USAGE.md`) for the exact Postman test flow, including getting a token and making requests.

The server runs at: `http://127.0.0.1:8000`

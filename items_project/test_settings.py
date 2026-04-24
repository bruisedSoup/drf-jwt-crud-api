from .settings import *


# Use SQLite only for automated tests so they can run without depending on XAMPP.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'test_db.sqlite3',
    }
}

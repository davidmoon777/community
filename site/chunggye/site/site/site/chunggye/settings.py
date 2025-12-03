INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'site',  # 단일 사이트 앱
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / "templates"],
        ...
    }
]

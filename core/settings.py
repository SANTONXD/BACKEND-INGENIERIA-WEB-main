from pathlib import Path
import os
import dj_database_url  # 👈 importante: asegúrate de tenerlo en requirements.txt

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-reemplaza-esto')

# 🔒 En Render, debe ser False para producción
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# Render genera automáticamente un hostname, por eso usamos *
ALLOWED_HOSTS = ['*']


# --- APPS INSTALADAS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'contacto',
]


# --- MIDDLEWARE ---
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 👈 necesario para servir estáticos en Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# --- BASE DE DATOS ---
# Render provee DATABASE_URL como variable de entorno
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}


# --- CORS & CSRF ---
CORS_ALLOW_ALL_ORIGINS = True  # 👈 más simple para pruebas; luego puedes restringirlo

CSRF_TRUSTED_ORIGINS = [
    'https://tu-nombre-de-app.onrender.com',
]


# --- ARCHIVOS ESTÁTICOS ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise configuración (sirve archivos estáticos sin servidor externo)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# --- LOGGING OPCIONAL ---
# Esto ayuda a depurar errores si Render falla
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

from pathlib import Path
import os
import dj_database_url  # 👈 asegúrate de que está en requirements.txt

BASE_DIR = Path(__file__).resolve().parent.parent

# --- CONFIGURACIÓN GENERAL ---
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-reemplaza-esto')

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [
    '*',  # Puedes dejarlo así en Render; Render usa subdominios dinámicos
]


# --- APPS INSTALADAS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Terceros
    'rest_framework',
    'corsheaders',

    # Tus apps
    'contacto',
]


# --- MIDDLEWARE ---
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 👈 debe ir arriba
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 👈 importante para servir estáticos
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
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}


# --- CORS & CSRF CONFIG ---
CORS_ALLOWED_ORIGINS = [
    "https://ingenieria-web-amber.vercel.app",  # frontend en Vercel
]

CSRF_TRUSTED_ORIGINS = [
    "https://ingenieria-web-amber.vercel.app",          # frontend
    "https://backend-ingenieria-web-main.onrender.com", # backend en Render (sin / final)
]

CORS_ALLOW_CREDENTIALS = True  # 👈 necesario si el frontend envía cookies o tokens


# --- ARCHIVOS ESTÁTICOS ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# --- ARCHIVOS MEDIA (si los llegas a usar) ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


# --- LOGGING (para depuración) ---
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


# --- REST FRAMEWORK CONFIG OPCIONAL ---
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}

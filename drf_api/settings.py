# from pathlib import Path
# import dj_database_url
# import os
# import re

# if os.path.exists('env.py'):
#     import env

# CLOUDINARY_STORAGE = {
#     'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
# }
# MEDIA_URL = '/media/'
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Django REST Framework Settings
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.SessionAuthentication'
#         if 'DEV' in os.environ
#         else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
#     ],
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10,
#     'DATETIME_FORMAT': '%d %b %Y',
# }
# if 'DEV' not in os.environ:
#     REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
#         'rest_framework.renderers.JSONRenderer',
#     ]

# REST_USE_JWT = True
# JWT_AUTH_SECURE = True
# JWT_AUTH_COOKIE = 'my-app-auth'
# JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
# JWT_AUTH_SAMESITE = 'None'

# # REST Auth Serializers
# REST_AUTH_SERIALIZERS = {
#     'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
# }

# CSRF_TRUSTED_ORIGINS = [
#     'https://8000-meenarathi-drfapiexpens-wyrd33tvxwu.ws.codeinstitute-ide.net',
# ]

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-l=vwb68gu!e2^289p!d$hvlzg#q7s629%o35ct&)8!#k#_g#=c'


# DEBUG = True

# ALLOWED_HOSTS = [
#     '8000-meenarathi-drfapiexpens-wyrd33tvxwu.ws.codeinstitute-ide.net',
#     os.environ.get('ALLOWED_HOST', 'expensesapi-6d53f1465c6d.herokuapp.com'),  
#     'localhost',
# ]

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'expenses',
#     'rest_framework',
#     'rest_framework.authtoken',
#     'django.contrib.sites',
#     'dj_rest_auth',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'dj_rest_auth.registration',
#     'corsheaders',
# ]

# SITE_ID = 1

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

# MIDDLEWARE = [
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
# if 'CLIENT_ORIGIN' in os.environ:
#     CORS_ALLOWED_ORIGINS = [
#         os.environ.get('CLIENT_ORIGIN')
#     ]

# if 'CLIENT_ORIGIN_DEV' in os.environ:
#     CORS_ALLOWED_ORIGINS = [os.environ.get('CLIENT_ORIGIN_DEV')]

# CORS_ALLOW_CREDENTIALS = True

# CSRF_TRUSTED_ORIGINS = [
#     'https://8000-meenarathi-drfapiexpens-wyrd33tvxwu.ws.codeinstitute-ide.net',
# ]
# ROOT_URLCONF = 'drf_api.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'drf_api.wsgi.application'

# # Database Configuration
# if 'DEV' in os.environ:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
#     DATABASES = {
#         'default': dj_database_url.parse(os.environ.get("DATABASE_URL", ""))
#     }
#     print('connected')

# # CORS Configuration


# # Database
# # https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# # Password validation
# # https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# # Internationalization
# # https://docs.djangoproject.com/en/5.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/5.0/howto/static-files/

# STATIC_URL = 'static/'

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Django REST Framework Settings
if 'DEV' in os.environ:
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication'
        ],
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
        'DATETIME_FORMAT': '%d %b %Y',
    }
else:
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
        ],
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
        'DATETIME_FORMAT': '%d %b %Y',
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
        ],
    }

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}

CORS_ALLOWED_ORIGINS = [
    # 'https://8000-meenarathi-drfapiexpens-wyrd33tvxwu.ws.codeinstitute-ide.net',
    # 'https://expenses-6281b20ca824.herokuapp.com',

    'https://3000-meenarathi-expensestrac-lhnzjhzshcd.ws.codeinstitute-ide.net',  # Your frontend in the development environment
    'https://expensesapi-6d53f1465c6d.herokuapp.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://8000-meenarathi-drfapiexpens-wyrd33tvxwu.ws.codeinstitute-ide.net',
    'https://expenses-6281b20ca824.herokuapp.com',
]

SECRET_KEY = 'django-insecure-l=vwb68gu!e2^289p!d$hvlzg#q7s629%o35ct&)8!#k#_g#=c'

DEBUG = True

ALLOWED_HOSTS = [
    '8000-meenarathi-drfapiexpens-wyrd33tvxwu.ws.codeinstitute-ide.net',
    os.environ.get('ALLOWED_HOST', 'expensesapi-6d53f1465c6d.herokuapp.com'),  
    'localhost',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'expenses',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'corsheaders',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drf_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'drf_api.wsgi.application'

# Database Configuration
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL:
        DATABASES = {
            'default': dj_database_url.parse(DATABASE_URL)
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
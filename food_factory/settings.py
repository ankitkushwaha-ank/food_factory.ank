from pathlib import Path
from django.contrib.messages import constants as messages

from django.conf.global_settings import STATICFILES_DIRS, MEDIA_ROOT, MEDIA_URL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7a&(!rga6lhdlh-!uai8q_3abj98bw+@&)u5a!$d6!c--w&3vq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['food-factory-41z6.onrender.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'service',
    'tinymce',
    'contactenquery',
    'Orderedfood',
    'SysAdmin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'food_factory.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'SysAdmin.context_processors.webuser_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'food_factory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS =[
    BASE_DIR,'static'
]

MEDIA_ROOT= BASE_DIR /"media"

MEDIA_URL="/media/"



MESSAGE_TAGS = {
    messages.ERROR: 'error',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.INFO: 'info',
}

# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.azuread.AzureADOAuth2',  # OR
#     'social_core.backends.microsoft.MicrosoftOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )
#
# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = '/home/'
#
# SOCIAL_AUTH_MICROSOFT_OAUTH2_KEY = 'your-client-id'
# SOCIAL_AUTH_MICROSOFT_OAUTH2_SECRET = 'your-client-secret'
# SOCIAL_AUTH_MICROSOFT_OAUTH2_SCOPE = ['User.Read']

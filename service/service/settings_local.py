import os


# Настройки для локальной разработки
DEBUG = True

# Настройки для локальной базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',   # Используется PostgreSQL
        'NAME': os.environ.get('DB_NAME'), # Имя базы данных
        'USER': os.environ.get('DB_USER'), # Имя пользователя
        'PASSWORD': os.environ.get('DB_PASS'), # Пароль пользователя
        'HOST': os.environ.get('DB_HOST'), # Наименование контейнера для базы данных в Docker Compose
    }
}

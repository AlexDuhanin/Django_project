# Установка Django
pip install django

# Проверка версии Django
django-admin --version

# Создание проекта в текущей директории
django-admin startproject myproject .

# Запуск сервера Django http://127.0.0.1:8000/admin/
python manage.py runserver

# Создание магазина
python manage.py startapp store

# Создание миграции
python manage.py makemigrations

# Применить миграции
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser


release: python manage.py db init --directory migrations
release: python manage.py db migrate
web: gunicorn app:app
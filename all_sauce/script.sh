python /usr/src/app/manage.py makemigrations
python /usr/src/app/manage.py migrate
python /usr/src/app/manage.py loaddata /usr/src/app/initial_data.json
python /usr/src/app/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
/usr/local/bin/gunicorn all_sauce.wsgi:application -w 2 -b :8000 --chdir /usr/src/app
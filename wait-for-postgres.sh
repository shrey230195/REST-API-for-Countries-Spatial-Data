#!/bin/bash

# ### WAITING POSTGRES START ###
RETRIES=1
while [ "$RETRIES" -gt 0 ]
do
  echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
  PG_STATUS="$(pg_isready -h $host -U postgres)"
  PG_EXIT=$(echo $?)
  echo "Postgres Status: $PG_EXIT - $PG_STATUS"
  if [ "$PG_EXIT" = "0" ];
    then
      RETRIES=0
  fi
  sleep 3  # timeout for new loop
done

python manage.py makemigrations && 
python manage.py migrate &&
python manage.py load-data &&
# python manage.py collectstatic --noinput --clear && 
python manage.py collectstatic --noinput --clear && 
gunicorn core.wsgi:application --bind 0.0.0.0:8000 --workers=2
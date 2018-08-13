#!/bin/sh

until pg_isready -h ${DB_HOST} -p ${DB_PORT}
do
    echo "Awating POSTGRES container"
    sleep 1
done
sleep 2

cd /code

if [ "$1" = 'local' ]; then
    python manage.py runserver 0:8000
fi

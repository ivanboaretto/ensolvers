#!/bin/bash
cd ./backend/myapi/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver &
cd ../../frontend/vue-spa/
npm run dev

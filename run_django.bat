@echo off
:: Run makemigrations
echo Running makemigrations...
python manage.py makemigrations

:: Run migrate
echo Running migrations...
python manage.py migrate

:: Run the Django development server
echo Starting the server...
python manage.py runserver

:: Pause the window so it doesn't close immediately after execution
pause

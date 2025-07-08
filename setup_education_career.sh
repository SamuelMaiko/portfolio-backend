#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Make migrations for new apps
echo "Creating migrations for education app..."
python manage.py makemigrations a_education

echo "Creating migrations for career app..."
python manage.py makemigrations a_career

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Populate data
echo "Populating education data..."
python manage.py populate_education

echo "Populating career data..."
python manage.py populate_career

echo "Setup complete!"

#!/bin/sh
set -e

# Run database migrations
python manage.py migrate

# Create superuser if it does not exist
python manage.py createsuperuser \
  --noinput \
  || true

# Continue with the container's main command
exec "$@"
#!/bin/sh

# shell will finish script execution if a command fails
set -e

# Function to show logs with a prefix
log() {
  echo "🔹 $1"
}

# Debug environment 
log "Debugging environment:"
log "Current directory: $(pwd)"
log "Python path: $PYTHONPATH"
log "Python executable: $(which python)"
log "Installed packages:"
pip list

# Wait for Postgres initialization
log "Checking PostgreSQL availability at $POSTGRES_HOST:$POSTGRES_PORT..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  log "Waiting for PostgreSQL to start..."
  sleep 2
done
log "✅ PostgreSQL is available at $POSTGRES_HOST:$POSTGRES_PORT"

# Migrate database
log "Applying database migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput
log "✅ Database migrations completed."

# Inicia o servidor Django
log "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000
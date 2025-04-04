# Install Python dependencies
pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p staticfiles

# Collect static files
python manage.py collectstatic --noinput

# Make sure the script doesn't fail if there are no static files
touch staticfiles/.keep 
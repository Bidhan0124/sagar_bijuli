import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electric_shop_project.settings') # Replace 'electric_shop_project'

application = get_wsgi_application()

# Vercel handler
def handler(event, context):
    return application(event.get('body', {}), lambda x, y: (x, y, []))
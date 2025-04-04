import os
from django.core.wsgi import get_wsgi_application
from serverless_wsgi import handle

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electric_shop_project.settings') # Replace 'electric_shop_project'

application = get_wsgi_application()

def handler(event, context):
    return handle(application, event, context)
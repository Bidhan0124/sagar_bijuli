import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electric_shop_project.settings') # Replace 'electric_shop_project'

application = get_wsgi_application()

# Vercel handler
def handler(event, context):
    return application(
        {
            'REQUEST_METHOD': event.get('httpMethod', ''),
            'PATH_INFO': event.get('path', ''),
            'QUERY_STRING': event.get('queryStringParameters', ''),
            'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
            'wsgi.input': event.get('body', ''),
            'wsgi.errors': '',
            'wsgi.version': (1, 0),
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
            'wsgi.url_scheme': 'https',
            'SERVER_NAME': event.get('headers', {}).get('host', ''),
            'SERVER_PORT': '443',
        },
        lambda status, headers: (
            {
                'statusCode': status,
                'headers': dict(headers),
                'body': ''
            },
            lambda content: content
        )
    )
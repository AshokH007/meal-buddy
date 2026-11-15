import os
import sys
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_buddy.settings')

# Get Django application
django_app = get_wsgi_application()

# Vercel serverless handler
def handler(request):
    """
    Vercel serverless function handler for Django
    """
    try:
        # Convert Vercel request to WSGI format
        environ = {
            'REQUEST_METHOD': request.method,
            'PATH_INFO': request.path,
            'SERVER_NAME': 'vercel.app',
            'SERVER_PORT': '443',
            'wsgi.url_scheme': 'https',
            'wsgi.input': request.body,
            'wsgi.errors': sys.stderr,
            'wsgi.version': (1, 0),
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': True,
        }
        
        # Add headers
        for key, value in request.headers.items():
            key = key.upper().replace('-', '_')
            if key not in ['CONTENT_LENGTH', 'CONTENT_TYPE']:
                key = f'HTTP_{key}'
            environ[key] = value
        
        # Start response callback
        response_data = {}
        
        def start_response(status, headers):
            response_data['status'] = status
            response_data['headers'] = headers
        
        # Get Django response
        django_response = django_app(environ, start_response)
        
        # Convert to Vercel response
        response_body = b''.join(django_response)
        
        return {
            'status': int(response_data['status'].split()[0]),
            'headers': dict(response_data['headers']),
            'body': response_body.decode('utf-8')
        }
        
    except Exception as e:
        return {
            'status': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': JsonResponse({'error': str(e)}).content.decode('utf-8')
        }

# For Vercel deployment
def lambda_handler(event, context):
    """
    AWS Lambda handler (alternative for Vercel)
    """
    class MockRequest:
        def __init__(self, event):
            self.method = event.get('httpMethod', 'GET')
            self.path = event.get('path', '/')
            self.headers = event.get('headers', {})
            self.body = event.get('body', '').encode()
    
    return handler(MockRequest(event))

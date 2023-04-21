# mysite/asgi.py
import os
import django
from channels.routing import ProtocolTypeRouter , URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import  AuthMiddlewareStack
from accounts.routing import  websocket_urlpatterns
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "esteps.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        'websocket':
        	URLRouter(
        	websocket_urlpatterns)
        # Just HTTP for now. (We can add other protocols later.)
    }
)
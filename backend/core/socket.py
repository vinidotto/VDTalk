import socketio

from django.conf import settings
# criando socket
socket = socketio.Server(
    cors_allowed_origins=settings.CORS_ALLOWED_ORIGINS
)
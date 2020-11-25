from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path
from firstpage import consumer

websocket_urlPattern=[
    path('ws/polData',consumer.DashConsumer),
]


application=ProtocolTypeRouter({
    #'http':
    'websockets':AuthMiddlewareStack(URLRouter(websocket_urlPattern)),
})
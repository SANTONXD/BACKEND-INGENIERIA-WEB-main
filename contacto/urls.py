from django.urls import path
from .views import MensajeAPIView

urlpatterns = [
    path('mensaje/', MensajeAPIView.as_view(), name='api-mensaje'),
    path('ver/', VerMensajesAPIView.as_view(), name='ver-mensajes'),
]


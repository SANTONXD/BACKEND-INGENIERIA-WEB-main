from django.urls import path
from .views import MensajeAPIView

urlpatterns = [
    path('api/contacto/', MensajeAPIView.as_view(), name='api-contacto'),
]

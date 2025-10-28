from django.urls import path
from .views import MensajeAPIView

urlpatterns = [
    path('mensaje/', MensajeAPIView.as_view(), name='api-mensaje'),
]



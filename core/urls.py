from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# 👇 Vista simple para la raíz del proyecto
def home(request):
    return JsonResponse({
        "status": "ok",
        "message": "API de contacto funcionando correctamente 🚀"
    })

urlpatterns = [
    path('', home, name='home'),  # ✅ Página de inicio
    path('admin/', admin.site.urls),
    path('', include('contacto.urls')),
]

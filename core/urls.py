from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# 👇 Vista simple para probar que el backend funciona
def home(request):
    return JsonResponse({
        "status": "ok",
        "message": "API de contacto funcionando correctamente 🚀"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),              # raíz
    path('api/', include('contacto.urls')),   # 👈 prefijo para la app de contacto
]

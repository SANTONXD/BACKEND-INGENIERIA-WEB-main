from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MensajeSerializer
from .models import Mensaje  # 👈 Asegúrate de importar el modelo

class MensajeAPIView(APIView):
    def get(self, request):
        """Permite ver todos los mensajes guardados (solo para prueba en Render)."""
        mensajes = Mensaje.objects.all().values('id', 'nombre', 'email', 'mensaje')
        return Response(list(mensajes), status=status.HTTP_200_OK)

    def post(self, request):
        """Guarda un nuevo mensaje enviado desde el formulario."""
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "message": "Mensaje recibido ✅"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

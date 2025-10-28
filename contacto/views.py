from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MensajeSerializer

class MensajeAPIView(APIView):
    def post(self, request):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True, "message": "Mensaje recibido"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

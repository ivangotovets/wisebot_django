from rest_framework import viewsets

from .models import Message
from .serializers import MessageSerialiser


class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerialiser
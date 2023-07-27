from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from random import randint

from .models import Message
from .serializers import MessageSerialiser


class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerialiser


class RandomMessageView(APIView):
    def get(self):
        last_obj = Message.objects.latest('pub_date')
        number = randint(1, last_obj.id)
        message = get_object_or_404(Message, id=number)
        response = {'random_message': message.text}
        return Response(response)

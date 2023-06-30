from rest_framework import serializers
from .models import Message


class MessageSerialiser(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'text', 'pub_date',)
        model = Message
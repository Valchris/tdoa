__author__ = 'Daniel'
from rest_framework import serializers
from glue.models import *
from swampdragon.serializers.model_serializer import ModelSerializer


class GameRoomSerializer(ModelSerializer):
    class Meta:
        model = 'glue.GameRoom'
        publish_fields = ('users',)
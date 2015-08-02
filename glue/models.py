from django.db import models
from django.contrib.auth.models import User
from swampdragon.models import SelfPublishModel
from .serializers import GameRoomSerializer


class GameRoom(SelfPublishModel, models.Model):
    serializer_class = GameRoomSerializer
    users = models.ManyToManyField(User)

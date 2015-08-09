from django.db import models
from django.contrib.auth.models import User
from swampdragon.models import SelfPublishModel
from .serializers import *


class Location(SelfPublishModel, models.Model):
    serializer_class = LocationSerializer

    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return u'(x=%s, y=%s)' % (self.x, self.y)


class PlayerConfig(SelfPublishModel, models.Model):
    serializer_class = PlayerConfigSerializer

    position = models.IntegerField()
    mobSpawn = models.ForeignKey(Location, related_name='mobSpawn')
    mobEnd = models.ForeignKey(Location, related_name='mobEnd')


class Player(SelfPublishModel, models.Model):
    serializer_class = PlayerSerializer

    user = models.ForeignKey(User)
    config = models.ForeignKey(PlayerConfig)
    currentLife = models.IntegerField()


class GameRoom(SelfPublishModel, models.Model):
    serializer_class = GameRoomSerializer

    users = models.ManyToManyField(Player)


class MobType(SelfPublishModel, models.Model):
    serializer_class = MobTypeSerializer

    name = models.CharField(max_length=255)
    startingHp = models.IntegerField()


class Mob(SelfPublishModel, models.Model):
    serializer_class = MobSerializer

    hp = models.IntegerField()
    location = models.ForeignKey(Location)


class Stage(SelfPublishModel, models.Model):
    serializer_class = StageSerializer

    mobType = models.ForeignKey(MobType)
    maxQuantity = models.IntegerField()
    spawnTimer = models.TimeField()


class CurrentStage(SelfPublishModel, models.Model):
    serializer_class = CurrentStageSerializer

    stage = models.ForeignKey(Stage)
    mobs = models.ManyToManyField(Mob)
    spawnIteration = models.IntegerField()







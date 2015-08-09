__author__ = 'Daniel'
from glue.models import *
from swampdragon.serializers.model_serializer import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        publish_fields = ('id', 'username')


class LocationSerializer(ModelSerializer):
    class Meta:
        model = 'glue.Location'


class PlayerConfigSerializer(ModelSerializer):
    class Meta:
        model = 'glue.PlayerConfig'


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = 'glue.Player'

    user = UserSerializer


class GameRoomSerializer(ModelSerializer):
    class Meta:
        model = 'glue.GameRoom'

    users = PlayerSerializer


class MobTypeSerializer(ModelSerializer):
    class Meta:
        model = 'glue.MobType'


class MobSerializer(ModelSerializer):
    class Meta:
        model = 'glue.Mob'


class StageSerializer(ModelSerializer):
    class Meta:
        model = 'glue.Stage'


class CurrentStageSerializer(ModelSerializer):
    class Meta:
        model = 'glue.CurrentStage'



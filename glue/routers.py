__author__ = 'Daniel'
from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from .models import *
from .serializers import *


class GameRoomRouter(ModelRouter):
    route_name = 'game-room'
    serializer_class = GameRoomSerializer
    model = GameRoom
    include_related = [PlayerSerializer, ]

    def get_object(self, **kwargs):
        return self.model.objects.get(users__user__username=kwargs['username'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

route_handler.register(GameRoomRouter)


class PlayerRouter(ModelRouter):
    route_name = 'player'
    serializer_class = PlayerSerializer
    model = Player
    include_related = [UserSerializer, ]

    def get_object(self, **kwargs):
        return self.model.objects.get(user__username=kwargs['username'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()


route_handler.register(PlayerRouter)
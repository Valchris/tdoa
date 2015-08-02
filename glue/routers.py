__author__ = 'Daniel'
from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from .models import GameRoom
from .serializers import GameRoomSerializer


class GameRoomRouter(ModelRouter):
    route_name = 'game-room'
    serializer_class = GameRoomSerializer
    model = GameRoom

    def get_object(self, **kwargs):
        return self.model.objects.get(users__username=kwargs['username'])

    def get_query_set(self, **kwargs):
        return self.model.objects.all()

route_handler.register(GameRoomRouter)
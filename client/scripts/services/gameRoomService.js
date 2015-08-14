app.service('gameRoomService', ['$rootScope', '$dragon', '$http', function($rootScope, $dragon, $http) {
    var gameRoomChannel = 'game-room-channel';

    this.subscribeToGameRoom = function() {
        $dragon.onReady(function () {
            $dragon.getSingle('game-room', {username: 'test'}).then(function (success) {
                $dragon.subscribe('game-room', gameRoomChannel, {id: success.data.id}).then(function (subscribeSuccess) {
                    console.log('Subscribed to gameRoom ', success.data.id);
                });
                $rootScope.$broadcast('GameRoomUpdated', success.data);
            });


            $dragon.onChannelMessage(function (channels, message) {
                if (indexOf.call(channels, gameRoomChannel) > -1) { // GameRoom message
                    $dragon.getSingle('game-room', {username: 'test'}).then(function (success) {
                        $rootScope.$broadcast('GameRoomUpdated', success.data);
                    });
                } else {
                    console.log('Unknown Message:', channels, message);
                }
            });
        });
    }

    this.startRound = function() {
        return $http.post('/api/gameroom/startround/', {});
    }
}]);

app.controller('homeCtrl', ['$scope', '$rootScope', '$timeout', '$dragon', function($scope, $rootScope, $timeout, $dragon){
    $scope.channel = 'local-channel';

    // We get a notice when the user has authenticated
    $scope.$on('UserUpdated', function(event, user) {

    });

    $dragon.onReady(function() {
        $dragon.getSingle('game-room', {username: 'test'}).then(function(response) {
            $scope.gameRoom = response.data;

            console.log($scope.gameRoom);
            $dragon.subscribe('game-room', $scope.channel, {id: $scope.gameRoom.id}).then(function(response) {
                $scope.dataMapper = new DataMapper(response.data);
                console.log('Subscribed to gameRoom ' , $scope.gameRoom.id);
            });
        });


        $dragon.onChannelMessage(function(channels, message) {
            if(indexOf.call(channels, $scope.channel) > -1) { // GameRoom message
                $dragon.getSingle('game-room', {username: 'test'}).then(function(response) {
                   $scope.gameRoom = response.data;
                    console.log('Game Room refreshed', response.data);
                });
                console.log('Game Room updated.');
            } else {
                console.log('Message:', channels, message);
            }
        });
    });


}]);
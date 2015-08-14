app.controller('homeCtrl', ['$scope', '$rootScope', 'gameRoomService', function($scope, $rootScope, gameRoomService){
    $scope.channel = 'local-channel';
    $scope.reset = function() {
        $scope.gameRoom = null;
        gameRoomService.subscribeToGameRoom();
    }
    $scope.reset();

    // We get a notice when the user has authenticated
    $scope.$on('UserUpdated', function(event, user) {

    });

    $scope.$on('gameRoomUpdated', function(event, model) {
        $scope.gameRoom = model;
    })


}]);
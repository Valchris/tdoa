app.controller('HeaderController', ['$scope', '$rootScope', 'gameRoomService', function($scope, $rootScope, gameRoomService) {
    $scope.reset = function() {
        $scope.gameRoom = null;
    };
    $scope.reset();

    $scope.$on('GameRoomUpdated', function(event, model) {
        $scope.gameRoom = model;
    });

    $scope.startRound = function() {
        gameRoomService.startRound().then(function(success) {
            console.log(success.data);
        })
    }

}]);
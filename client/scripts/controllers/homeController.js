app.controller('homeCtrl', ['$scope', '$rootScope', '$timeout', '$dragon', function($scope, $rootScope, $timeout, $dragon){
    // We get a notice when the user has authenticated
    $scope.$on('UserUpdated', function(event, user) {

    });
    $dragon.onReady(function() {
        $dragon.getSingle('game-room', {username: 'test'}).then(function(response) {
            $scope.dataMapper = new DataMapper(response.data);
           console.log(response);
        });
    })



}]);
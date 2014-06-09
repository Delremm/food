angular.module('macroApp.services', []).factory('macroManager', ['$http', function ($http) {
    return {
        get: function(url, callback){
            $http.get(url).success(function(data) {
                //data = JSON.parse(data);
                callback(data);
            });
        }
    };
}]);
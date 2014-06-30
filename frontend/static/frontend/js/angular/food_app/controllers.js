angular.module('foodApp.controllers', []).controller(
        'CartCtrl', ['$scope', '$http', 'foodManager', function($scope, $http, foodManager) {
    $scope.ready = false;
    $scope.tst = 'privet';
    $scope.menus = '';
    $scope.message = '';
    $scope.cart_is_ready = false;
    $scope.cart_total = 0;
    foodManager.get('/api/menu_by_type/?format=json', function(data) {
        $scope.menus = data;
        $scope.ready = true;
        $('body').removeClass('wait');
    });
    foodManager.get('/api/order_options/?format=json', function(data) {
        $scope.order_options = data;
    });
    foodManager.get('/api/cart/?format=json', function(data) {
        $scope.cart = data;
        $scope.calc_total();
        $scope.cart_is_ready = true;
    });
    $scope.calc_price = function(menu, cals){
        menu.calculated_price = (cals*menu.price).toFixed();
    };
    $scope.add_to_cart = function(menu){
        $http.get('/api/add_to_cart/', config={params: {item_to_add:  JSON.stringify({id: menu.id, cals: menu.cals})}}).success(function(data, status) {
            $scope.status = status;
            $scope.message = 'Добавлено в корзину';
            $scope.refresh_cart();
            $('body').removeClass('wait');
        }).
        error(function(data, status) {
            $scope.status = status;
            $scope.message = 'Ошибка добавления в корзину'
            $('body').removeClass('wait');
        });
    };
    $scope.refresh_cart = function(){
        $http.get('/api/cart/?format=json').success(function(data) {
            $scope.cart = data;
            $scope.calc_total();
        });
    };
    $scope.calc_total = function(){
        var total = 0;
        for (var i in $scope.cart) {
            total += $scope.cart[i].price*$scope.cart[i].quantity;
        };
        $scope.cart_total = total.toFixed();
    };
    $scope.clear_cart = function(){
        $http.get('/api/clear_cart/?format=json').success(function(data) {
            $scope.refresh_cart();
        });
    };
    $scope.cart_is_empty = function(){
        if ($scope.cart) {
            return false
        } else {
            return true
        };
    };
}]);
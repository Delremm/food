angular.module('diceApp.controllers', []).controller(
        'DiceCtrl', ['$scope', '$http', 'diceManager', function($scope, $http, diceManager) {
    $scope.ready = false;
    $scope.btc = {
        balance: '',
        withdraw_address: '',
        withdraw_amount: '',
    };
    $scope.roll = {
        roll_amount: '',
        win_amount: '',
        currency: 'btc',
        win_odds: '50',
        multiplier: '',
        max_bet: '',
        min_bet: '',
        raw_chance: '',
        client_seed: 'randoddm',
    };
    // in play.html from django context
    $scope.settings = settings;
    $scope.currencies = ['btc',];
    $scope.roll_in_progress = false;
    count_multiplier();
    count_max_min_bet();
    refresh_history();
    refresh_balance();
    // diceManager.get('/api/bet_history/?format=json', function(data){
    //     $scope.bet_history_list = data;
    // });
    function refresh_balance(){
        diceManager.get('/api/get_balance/?format=json', function(data) {
            $scope.btc.balance = data.btc_amount;
        });
    }
    function refresh_history(){
        diceManager.get('/api/my_bet_history/?format=json', function(data){
            $scope.bet_history_list = data;
        });
    }
    function count_max_min_bet(){
        $scope.roll.min_bet = $scope.settings.min_bet;
        $scope.roll.max_bet = (
            ($scope.settings.total_btc/$scope.roll.multiplier)/$scope.settings.num_of_max_bets).toFixed(
                $scope.settings.max_bet_comma_digits);
    };
    function count_win_amount(){
        if ($scope.roll.roll_amount) {
            $scope.roll.win_amount = ($scope.roll.roll_amount*(
                $scope.roll.multiplier)).toFixed($scope.settings.comma_digits);
        } else {
            $scope.roll.win_amount = '';
        }
    };
    function count_multiplier(){
        $scope.roll.multiplier = (100/$scope.roll.win_odds)*(
            (100-$scope.settings.house_edge)/100);
    };
    function count_win_odds(){
        $scope.roll.win_odds = (100/$scope.roll.multiplier)*(
            (100-$scope.settings.house_edge)/100);
    }
    $scope.set_win_odds = function(win_odds){
        $scope.roll.win_odds = win_odds;
        count_multiplier();
        count_max_min_bet();
        count_win_amount();
    }
    $scope.win_odds_changed = function(){
        count_multiplier();
        count_max_min_bet();
        count_win_amount();
    };
    $scope.roll_amount_changed = function(){
        count_win_amount();
    };
    $scope.set_multiplier = function(multiplier){
        $scope.roll.multiplier = multiplier;
        count_win_odds();
        count_max_min_bet();
        count_win_amount();
    }
    $scope.withdraw = function(){
        $('body').addClass('wait');
        $http.get('/api/withdraw_btc/?format=json').success(function(data, status) {
            $scope.status = status;
            console.log(data);
            if (data[0] == 'test') {
                $scope.body_data = 'yes';
                $('#withdraw_form').text("You've successfully withdrawed the money");
            } else {
                $scope.body_data = data;
            }
            $('body').removeClass('wait');
        }).
        error(function(data, status) {
            $scope.body_data = data || "Request failed";
            $scope.status = status;
            $('body').removeClass('wait');
        });
    };
    $scope.roll_dices = function(){
        $scope.roll_in_progress = true;
        $('body').addClass('wait');
        var post_data = {
            client_seed: "234234dfg43234",
        };
        //post('/api/roll/?format=json', $scope.roll).
        $http.post('/api/roll/?format=json', $scope.roll).success(function(data, status) {
            $scope.status = status;
            console.log(data);
            if (data['result'] == 'win') {
                $('.roll_result').text('WIN');
            };
            if (data['result'] == 'lose') {
                $('.roll_result').text('LOSE');
            };
            refresh_history();
            refresh_balance();
            $('body').removeClass('wait');
            $scope.roll_in_progress = false;
        }).
        error(function(data, status) {
            $scope.status = status;
            $('body').removeClass('wait');
            $scope.roll_in_progress = false;
        });
    }
    $scope.btc_withdraw_is_valid = function(){
        if (($scope.btc.balance >= $scope.btc.withdraw_amount) && ($scope.btc.withdraw_amount >= 0.0005)) {
            return false;
        }
        else {
            return true;
        };
    };
    $scope.roll_is_allowed = function(){
        if ($scope.roll_in_progress){
            return true;
        }
        if ($scope.roll.currency=='btc'){
            if (($scope.roll.roll_amount <= $scope.btc.balance)&&(
                    $scope.roll.roll_amount>=$scope.settings.minimal_roll_amount)&&(
                        $scope.roll.roll_amount>=$scope.roll.min_bet)&&(
                            $scope.roll.roll_amount<=$scope.roll.max_bet)) {
                return false;
            } else {
                return true;
            }            
        } else {
            return true;
        };
    };
}]);
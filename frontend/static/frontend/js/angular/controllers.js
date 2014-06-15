angular.module('macroApp.controllers', []).controller(
        'MacroTdeeCtrl', ['$scope', '$http', 'macroManager', function($scope, $http, macroManager) {
    $scope.ready = false;
    $scope.body_data = {
        weight: '',
        height: '',
        age: '',
        activity: '',
        activity_options: '',
        gender: 'm',
        bfp: ''
    };
    macroManager.get('/api/apps/macro/tdee/?format=json', function(data) {
        $scope.macro_data = data;
        $scope.ready = true;
        $scope.body_data.activity = data.ACTIVITIES[1];
        $scope.body_data.activity_options = data.ACTIVITIES;
        $scope.body_data.gender = 'm';
    });
    function Harris_Benedict_method(body_data){
        var height = parseFloat(body_data.height);
        var weight = parseFloat(body_data.weight);
        var age = parseFloat(body_data.age);
        if (body_data.gender == 'm'){
            result = (13.397*weight+4.799*height-5.677*age+88.362)
        }
        else {
            result = (9.247*weight+3.098*height-4.330*age+447.593) 
        }
        return result
    };
    function Mifflin_St_Jeor_method(body_data){
        var height = parseFloat(body_data.height);
        var weight = parseFloat(body_data.weight);
        var age = parseFloat(body_data.age);
        var p = (10*weight+6.25*height-5*age);
        return (body_data.gender == 'm')?p+5:p-161
    };
    function calculate_lean_body_mass(body_data){
        //bfp - body fat percentage
        //lbm - lean body mass
        var bfp = parseFloat(body_data.bfp);
        var weight = parseFloat(body_data.weight);
        var height = parseFloat(body_data.height);
        var lbm = weight*(100-bfp)/100.0;
        // if (bfp){
        //     var lbm = weight*(100-bfp)/100.0;
        // }
        // else {
        //     if (body_data.gender == 'm'){
        //         lbm = (0.32810 * weight) + (0.33929 * height) - 29.5336;
        //     }
        //     else {
        //         lbm = ( 0.29569 * weight) + (0.41813 * height) - 43.2933
        //     }
        // }
        return lbm
    }
    function calculate_fat_mass(body_data){
        //bfp - body fat percentage
        //fm - fat mass
        var bfp = parseFloat(body_data.bfp);
        var weight = parseFloat(body_data.weight);
        var fm = weight*bfp/100.0;
        return fm
    }
    function Katch_McArdle_method(body_data){
        //lbm - lean body mass
        var lbm = calculate_lean_body_mass(body_data);
        return 370+21.6*lbm
    };
    function Katch_McArdle_method_is_ready(body_data){
        return True;
    }
    $scope.bmr = {
        current_method_id: 0,
        methods: [
            {id: 0, name: 'Mifflin St Jeor формула', callback: Mifflin_St_Jeor_method},
            //{id: 1, name: 'Harris-Benedict формула', callback: Harris_Benedict_method},
            {id: 1, name: 'Katch-McArdle формула', callback: Katch_McArdle_method, ready_callback: Katch_McArdle_method_is_ready},
        ],
    };

    $scope.results = {
        bmr: '',
        tdee: '',
        bmi: '',
    };
    function calculate_body_mass_index(body_data){
        //bmi - body mass index
        var height = parseFloat(body_data.height);
        var weight = parseFloat(body_data.weight);
        return Math.floor(weight/((height/100)*(height/100)))
    }
    function calculate_bmr(bmr_method_id, body_data){
        // bmr - basal metabolic ratio
        var result = $scope.bmr.methods[bmr_method_id].callback(body_data);
        return Math.floor(result)
    };
    function calculate_max_fat_metabolism(body_data){
        //bfp - body fat percentage
        //lbm - lean body mass
        var bfp = parseFloat(body_data.bfp);
        var weight = parseFloat(body_data.weight);
        var fat = weight*bfp/100.0;
        return Math.floor(fat*(30/0.4535))
    }
    function calculate_waist_to_height_ratio(body_data){
        var waist = parseFloat(body_data.waist);
        var height = parseFloat(body_data.height);
        return 100*waist/height
    }
    $scope.$watchCollection('body_data', function(value){
        // value is $scope.body_data
        $scope.results.bmr = calculate_bmr($scope.bmr.current_method_id, value);
        $scope.results.bmi = calculate_body_mass_index(value);
        $scope.results.max_fat_metabolism = calculate_max_fat_metabolism(value);
        $scope.results.lean_body_mass = calculate_lean_body_mass(value);
        $scope.results.waist_to_height_ratio = calculate_waist_to_height_ratio(value);
        $scope.results.fat_mass = calculate_fat_mass(value);
    })
    $scope.set_bmr_method = function(bmr_method_id){
        $scope.bmr.current_method_id = bmr_method_id;
        $scope.results.bmr = calculate_bmr(bmr_method_id, $scope.body_data);
    };
    function calculate_tdee(bmr, body_data){
        //bmr - basal metabolic rate
        var mul = parseFloat(body_data.activity.mul);
        return Math.floor(bmr*mul)
    };
    $scope.$watch('results.bmr + body_data.activity.mul', function(value){
        $scope.results.tdee = calculate_tdee(value, $scope.body_data);
    });
    //$scope.results.bmr = calculate_bmr($scope.bmr.current_method_id, $scope.body_data);
    // var activity_options = [
    //         { id:1, name: "сидячий образ жизни", mul: 1.2 },
    //         { id:2, name: "легкая активность", mul: 1.35 },
    //         { id:3, name: "умеренная активность", mul: 1.45 },
    //         { id:4, name: "высокая активность", mul: 1.575},
    //         { id:3, name: "сверхвысокая активность", mul: 1.7 }, ];
    $scope.body_data = {
        weight: '',
        activity: '',
        activity_options: '',
    };
}]);
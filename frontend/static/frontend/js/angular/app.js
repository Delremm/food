// Declare app level module which depends on filters, and services
'use strict';
var myModule = angular.module('diceApp', ['diceApp.directives', 'diceApp.controllers', 'diceApp.services']);
myModule.config(['$interpolateProvider', '$httpProvider', function($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'; 
}]);

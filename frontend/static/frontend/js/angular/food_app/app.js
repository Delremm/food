// Declare app level module which depends on filters, and services
'use strict';
var foodModule = angular.module('foodApp', ['foodApp.directives', 'foodApp.controllers', 'foodApp.services']);
foodModule.config(['$interpolateProvider', '$httpProvider', function($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'; 
}]);

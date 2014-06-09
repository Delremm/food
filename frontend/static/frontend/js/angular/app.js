// Declare app level module which depends on filters, and services
'use strict';
var macroModule = angular.module('macroApp', ['macroApp.directives', 'macroApp.controllers', 'macroApp.services']);
macroModule.config(['$interpolateProvider', '$httpProvider', function($interpolateProvider, $httpProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'; 
}]);

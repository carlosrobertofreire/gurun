'use strict';

/**
 * @ngdoc overview
 * @name numerologiaWsApp
 * @description
 * # numerologiaWsApp
 *
 * Main module of the application.
 */
angular
  .module('numerologiaWsApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });

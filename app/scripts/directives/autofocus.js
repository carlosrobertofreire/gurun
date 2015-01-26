'use strict';

/**
 * @ngdoc directive
 * @name numerologiaWsApp.directive:autofocus
 * @description
 * # autofocus
 */
angular.module('numerologiaWsApp').directive('autofocus', ['$timeout', function($timeout) {
    return {
        restrict: 'A',
        link: function($scope, $element) {
            $timeout(function() {
                $element[0].focus();
            });
        }
    }
}]);
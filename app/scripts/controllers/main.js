'use strict';

/**
 * @ngdoc function
 * @name numerologiaWsApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the numerologiaWsApp
 */
angular.module('numerologiaWsApp').controller('MainCtrl',
    function($scope, NumerologiaService) {

        $scope.resultList = [];
        $scope.name = '';

        $scope.analyze = function() {
            if ($scope.name) {
                $scope.resultList.push(NumerologiaService.analyze($scope.name));
                $scope.name = '';
            }
        };

        $scope.setText = function(name) {
            $scope.name = name;
        };

    }
);
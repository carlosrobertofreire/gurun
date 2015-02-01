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

        $scope.analyze = function() {
            if (this.name) {
                $scope.resultList.push(NumerologiaService.analyze(this.name));
                this.name = '';
            }
        };


    }
);
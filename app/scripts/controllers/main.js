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
            $scope.resultList.push({
                'text': NumerologiaService.exemplo() + this.name,
                'number': 3,
                'value': 'EXCELENTE'
            })
        };


    }
);
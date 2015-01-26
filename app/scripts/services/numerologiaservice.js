'use strict';

/**
 * @ngdoc service
 * @name numerologiaWsApp.NumerologiaService
 * @description
 * # NumerologiaService
 * Service in the numerologiaWsApp.
 */
angular.module('numerologiaWsApp').service('NumerologiaService', function() {

    this.analyze = function(text) {
        return {
            'id': new Date().getTime(),
            'text': text,
            'number': 3,
            'value': 'EXCELENTE'
        };
    };

});
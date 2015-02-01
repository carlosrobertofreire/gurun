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
        var textNormalized = this.normalize(text);
        var chars = textNormalized.split('');

        var sum = 0;
        for (var i = 0; i < textNormalized.length; i++) {
            sum = sum + this.charValue(textNormalized.charAt(i));
        }

        console.log(sum);
        /*var s = "overpopulation";
        for (var i = 0; i < s.length; i++) {
            console.log(s.charAt(i));
        }*/



        return {
            'id': new Date().getTime(),
            'text': text,
            'number': 3,
            'value': 'EXCELENTE'
        };


    };

    this.charValue = function(c) {
        switch (c) {
            case 'A':
                return 1;
            case 'B':
                return 2;
            case 'C':
                return 3;
            case 'D':
                return 4;
            case 'E':
                return 5;
            case 'F':
                return 6;
            case 'G':
                return 7;
            case 'H':
                return 8;
            case 'I':
            case 'J':
                return 9;
            case 'K':
                return 10;
            case 'L':
                return 20;
            case 'M':
                return 30;
            case 'N':
                return 40;
            case 'O':
                return 50;
            case 'P':
                return 60;
            case 'Q':
                return 70;
            case 'R':
                return 80;
            case 'S':
                return 90;
            case 'T':
                return 100;
            case 'U':
            case 'V':
            case 'W':
                return 200;
            case 'X':
            case 'Y':
                return 300;
            case 'Z':
                return 400;
            default:
                return 0;
        }
    };

    this.normalize = function(str) {
        str = str.replace(/^\s+|\s+$/g, ''); // trim
        str = str.toLowerCase();
        // remove accents, swap ñ for n, etc
        var from = 'àáäâèéëêìíïîòóöôùúüûñç·/_,:;';
        var to = 'aaaaeeeeiiiioooouuuunc------';
        for (var i = 0, l = from.length; i < l; i++) {
            str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
        }
        str = str.replace(/[^a-z0-9 -]/g, '') // remove invalid chars
            .replace(/\s+/g, '-') // collapse whitespace and replace by -
            .replace(/-+/g, '-'); // collapse dashes
        return str.toUpperCase();
    };

});
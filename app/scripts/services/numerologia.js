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
        var textNumber = this.calculate(text);
        var textValue = this.interpret(textNumber);
        return {
            'id': new Date().getTime(),
            'text': text,
            'number': textNumber,
            'value': textValue
        };
    };

    this.interpret = function(textNumber){
        switch (textNumber) {
            case 7:
            case 9:
            case 11:
            case 14:
            case 17:
            case 19:
            case 22:
            case 25:
                return 'EXCELENTE';
            case 2:
            case 3:
            case 4:
            case 5:
            case 8:
            case 20:
            case 22:
            case 23:
                return 'BOM';
            case 6:
            case 24:
                return 'RUIM';
            case 1:
            case 10:
            case 12:
            case 13:
            case 15:
            case 16:
            case 18:
            case 21:
                return 'PÉSSIMO';
            default:
                return 'NÃO INTERPRETADO';
        }

    };

    this.calculate = function(text) {
        var textNormalized = this.normalize(text);
        var sum = 0;
        for (var i = 0; i < textNormalized.length; i++) {
            sum = sum + this.charValue(textNormalized.charAt(i));
        }
        if (sum <= 22) {
            return sum;
        } else {
            var sumString = String(sum);
            var finalSum = 0;
            for (var k = 0; k < sumString.length; k++) {
                finalSum = finalSum + Number(sumString.charAt(k));
            }
            return finalSum;
        }
    };

    this.charValue = function(c) {
        if (!isNaN(c)){
            return Number(c);
        }
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
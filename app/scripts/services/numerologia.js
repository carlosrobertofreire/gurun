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
        textNormalized = this.normalize(text);
        var chars = textNormalized.split('');


        //console.log(letters);
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
            case 'a':
                return 1;
            case 'b':
                return 2;
            case 'c':
                return 3;
            case 'd':
                return 4;
            case 'e':
                return 5;
            case 'f':
                return 6;
            case 'g':
                return 7;
            case 'h':
                return 8;
            case 'i':
            case 'j':
                return 9;
            case 'k':
                return 10;
            case 'l':
                return 20;
            case 'm':
                return 30;
            case 'n':
                return 40;
            case 'o':
                return 50;
            case 'p':
                return 60;
            case 'q':
                return 70;
            case 'r':
                return 80;
            case 's':
                return 90;
            case 't':
                return 100;
            case 'u':
            case 'v':
            case 'w':
                return 200;
            case 'x':
            case 'y':
                return 300;
            case 'z':
                return 400;

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
        return str;
    };

});
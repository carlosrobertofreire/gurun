'use strict';

describe('Service: NumerologiaService', function () {

  // load the service's module
  beforeEach(module('numerologiaWsApp'));

  // instantiate service
  var NumerologiaService;
  beforeEach(inject(function (_NumerologiaService_) {
    NumerologiaService = _NumerologiaService_;
  }));

  it('should do something', function () {
    expect(!!NumerologiaService).toBe(true);
  });

});

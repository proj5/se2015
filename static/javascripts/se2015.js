(function () {
  'use strict';
  
  angular
    .module('se2015', [
      'se2015.config',
      'se2015.routes',
      'se2015.users',
      'se2015.profiles',
      'se2015.layout',
      'se2015.controllers',
      'se2015.learning',
      'se2015.exam'
  ]);

  angular
    .module('se2015')
    .run(run);

  run.$inject = ['$http'];

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }

  angular
    .module('se2015.routes', ['ngRoute']);

  angular
    .module('se2015.config', []);
    
  angular.module('se2015.controllers', [
    'ngResource'
  ]);
})();
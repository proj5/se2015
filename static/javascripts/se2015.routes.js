(function () {
  'use strict';

  angular
    .module('se2015.routes')
    .config(config);

  config.$inject = ['$routeProvider'];
  window.alert("Route Provider")
  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/register', {
      controller: 'RegisterController', 
      controllerAs: 'vm',
      templateUrl: '/static/templates/users/register.html'
    }).otherwise('/');
  }
})();
(function () {
  'use strict';
  
  angular
    .module('se2015.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
    $routeProvider.when('/register', {
      controller: 'RegisterController', 
      controllerAs: 'vm',
      templateUrl: '/static/templates/users/register.html'
    }).when('/login', {
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: 'static/templates/users/login.html'
    })
    .when('/learning', {
      controller: 'LearningController',
      controllerAs: 'vm',
      templateUrl: 'static/templates/learning.html'
    })
    .when('/learning/:gradeId', {
      controller: 'QuestionController',
      controllerAs: 'vm',
      templateUrl: 'static/templates/question.html'
    })
    .when('/main', {
      templateUrl: '/static/templates/main/main.html'
    })
    .when('/admin', {
      redirectTo: '/'
    })
    .otherwise('/main')
  }
})();
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
    })
    .when('/login', {
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: 'static/templates/users/login.html'
    })
    .when('/learning', {
      controller: 'LearningController1',
      controllerAs: 'vm',
      templateUrl: 'static/templates/learning/learning1.html'
    })    
    .when('/learning/toan-lop-1', {
      controller: 'LearningController1',
      controllerAs: 'vm',
      templateUrl: 'static/templates/learning/learning1.html'
    })
    .when('/learning/toan-lop-2', {
      controller: 'LearningController2',
      controllerAs: 'vm',
      templateUrl: 'static/templates/learning/learning2.html'
    })
    .when('/learning/toan-lop-3', {
      controller: 'LearningController3',
      controllerAs: 'vm',
      templateUrl: 'static/templates/learning/learning3.html'
    })
    .when('/learning/toan-lop-4', {
      controller: 'LearningController4',
      controllerAs: 'vm',
      templateUrl: 'static/templates/learning/learning4.html'
    })
    .when('/learning/toan-lop-5', {
      controller: 'LearningController5',
      controllerAs: 'vm',
      templateUrl: 'static/templates/learning/learning5.html'
    })
    .when('/learning/toan-lop-6', {
      controller: 'LearningController6',
      controllerAs: 'vm',
      templateUrl: 'static/templates/learning/learning6.html'
    })
    .when('/learning/:gradeId/:skillId', {
      controller: 'QuestionController',
      controllerAs: 'vm',
      templateUrl: 'static/templates/learning/question.html'
    })
    .when('/exam', {
      controller: 'ExamController',
      controllerAs: 'vm',
      templateUrl: 'static/templates/exam/exam.html'
    })
    .when('/exam/:examId', {
      controller: 'ExamDetailController',
      controllerAs: 'vm',
      templateUrl: 'static/templates/exam/exam_detail.html'
    })
    .when('/main', {
      controller: 'MainController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/main/main.html'
    })
    .when('/user/:username', {
      controller: 'ProfileController',
      controllerAs: 'vm',
      templateUrl: 'static/templates/profiles/profile.html'
    })
    .when('/user/:username/settings', {
      controller: 'ProfileSettingsController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/profiles/settings.html'
    })
    .otherwise('/main')
  }
})();
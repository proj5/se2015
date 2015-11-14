(function() {
  'use strict';

  var questionController = angular.module('se2015.learning.controllers');

  questionController.controller('QuestionController', function($http, $routeParams) { 
    var vm = this;
    vm.gradeId = $routeParams.gradeId;            
    vm.questionId = "1";
    vm.url = "api/v1/exercises/" + vm.questionId + "/";            
    vm.answer = "0";
    vm.submitted = false;    
    
    getExercise();
     
    function getExercise() {       
      $http.get(vm.url, { headers: {
          'Content-type': 'application/json'
        }
      }).success(function(data, status, headers, config) {               
        vm.data = JSON.parse(JSON.stringify(data));                                  
      }).error(function(data, status, headers, config) {
        console.log("Error");
      });
    }        
    vm.change = function() {        
      var num = Math.floor(Math.random() * 6 + 1);        
      vm.questionId = num.toString();    
      vm.url = "api/v1/exercises/" + vm.questionId + "/";            
      vm.submitted = false;        
      vm.answer = "0";
      getExercise();        
    };           
  });
})();

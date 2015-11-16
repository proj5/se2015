(function() {
  'use strict';

  var questionController = angular.module('se2015.learning.controllers');

  questionController.controller('QuestionController', function($http, $routeParams) { 
    var vm = this;
    vm.gradeId = $routeParams.gradeId; 
    vm.skillId = $routeParams.skillId;        
    vm.userAnswer = "";
    vm.submitted = false;    
    vm.answerCorrect = false;

    getExercise();
     
    function getExercise() {       
      vm.url = "api/v1/exercise/" + vm.gradeId + "/" + vm.skillId + "/";
      $http.get(vm.url, { headers: {
          'Content-type': 'application/json'
        }
      }).then(function successCallback(response) {                       
        vm.data = response.data;
      }, function errorCallback(response) {
        console.log("Error");
      });
    }        
    
    vm.change = function() {                           
      vm.url = "api/v1/exercise/" + vm.gradeId + "/" + vm.skillId + "/";
      vm.submitted = false;        
      vm.userAnswer = "";            
      vm.answerCorrect = false;
      getExercise();  
    };   

    vm.checkAnswer = function() {      
      vm.url = "api/v1/exercise/" + vm.gradeId + "/" + vm.skillId + "/";
      postAnswer();                        
    };

    function postAnswer() { 
      vm.answerCorrect = false;                 
      vm.submitted = false;
      $http.post(vm.url, { 
        "id": vm.data.id,
        "answer": vm.userAnswer 
      })
      .then(function successCallback(response) {                  
        vm.submitted = true;
        vm.answerCorrect = response.data;                            
      }, function errorCallback(response) {          
        console.log("Post Error");
      });    
    }        
  });
})();

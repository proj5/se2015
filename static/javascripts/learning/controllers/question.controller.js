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

    var list_answer = [];

    vm.chooseAnswer = function(answer) {
      var position = -1;
      for (var i = 0; i < list_answer.length; i++) {
        if (list_answer[i] == answer)
          position = i;
      }
      if (position == -1) list_answer.push(answer);
      else {
        list_answer[position] = list_answer[list_answer.length-1];
        list_answer.pop()
      }
    }

    function postAnswer() {
      vm.answerCorrect = false;
      vm.submitted = false;
      if (list_answer.length > 0) {
        vm.userAnswer = "";
        for(var i=0; i < list_answer.length; i++) {
          vm.userAnswer += list_answer[i];
          if (i < list_answer.length-1)
             vm.userAnswer += '|'
        }
      }
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

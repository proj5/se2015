(function() {
  'use strict';

  var examDetailController = angular.module('se2015.exam.controllers');

  examDetailController.controller('ExamDetailController', function($http, $routeParams, $timeout) {
    var vm = this;
    vm.examId = $routeParams.examId;    
    vm.userAnswer = {};
    vm.fillAnswer = false;
    vm.stop_timer = false;
    vm.correct = {};
    vm.show_exercise_result = false;

    getExam();

    function getExam() {
      vm.url = "api/v1/exam/" + vm.examId + "/";
      $http.get(vm.url, { headers: {
          'Content-type': 'application/json'
        }
      }).then(function successCallback(response) {
        vm.exam = response.data;
        for (var i = 0; i < vm.exam.num_exercises; i++) {
          var id = vm.exam.exercises[i].id;
          vm.correct[id] = false;
        }
        timer();
        if (vm.exam.taken == true) getExamRecord();
      }, function errorCallback(response) {
        console.log("Error get exam");
      });
    }

    function getExamRecord() {
      document.getElementById("button_submit").disabled = true;
      var url = "api/v1/exam_record_user/" + vm.examId + "/";
      $http.get(url)
      .then(function successCallback(response) {
        vm.record = response.data;
        console.log(vm.record);
        for (var i = 0; i < vm.exam.num_exercises; i++) {
          var id = vm.exam.exercises[i].id;
          vm.checkScore(id);
        }
        vm.show_exercise_result = true;
      }, function errorCallback(response) {
        console.log("Error get exam record for certain users");
      })
    }

    function timer() {
      vm.counter = vm.exam.time_limit;       
      vm.minutes = Math.floor(vm.counter / 60);
      vm.seconds = vm.counter % 60;
      if (vm.exam.taken == false) vm.countDown();
    }

    vm.checkScore = function(id) {
      for (var i = 0; i < vm.exam.num_exercises; i++) 
        if (vm.record.exercise_records[i]) {        
          var exercise_id = vm.record.exercise_records[i].exercise.id;
          if (exercise_id == id) {
            if (vm.record.exercise_records[i].score == 1) {
              vm.correct[id] = true;
              // Set panel heading green
              document.getElementById("panel" + id).style.backgroundColor = '#def2de';
              document.getElementById("panel" + id).style.color = '#44a942';
              for (var j = 0; j < vm.record.exercise_records[i].answer.length; j++) {   
                var answer = vm.record.exercise_records[i].answer[j].answer;
                if (vm.exam.exercises[i].question_type == 'AN') vm.userAnswer[id] = answer;
                else 
                  if (vm.exam.exercises[i].question_type == 'MC') 
                    document.getElementById("checkbox" + answer).click();
                  else document.getElementById("radio" + answer).click();
              }
            } else {
              vm.correct[id] = false;
              // Set panel heading red
              document.getElementById("panel" + id).style.backgroundColor = '#f2dede';
              document.getElementById("panel" + id).style.color = '#a94442';              
              for (var j = 0; j < vm.record.exercise_records[i].answer.length; j++) {
                answer = vm.record.exercise_records[i].answer[j].answer;
                console.log(answer);
                if (vm.exam.exercises[i].question_type == 'AN') vm.userAnswer[id] = answer;
                else 
                  if (vm.exam.exercises[i].question_type == 'MC') {
                    document.getElementById("checkbox" + answer).click();                    
                  }
                  else document.getElementById("radio" + answer).click();
              }              
            }
          }
        } else {
          vm.correct[id] = false;
          // Set panel heading red
          document.getElementById("panel" + id).style.backgroundColor = '#f2dede';
          document.getElementById("panel" + id).style.color = '#a94442';
        }
    }

    vm.countDown = function() {
      if (vm.counter < 0 || vm.stop_timer) {
        if (vm.counter < 0) vm.submit();
        $timeout.cancel(vm.countDown);
        return;
      }
      var stopped = $timeout(function() {
        vm.minutes = Math.floor(vm.counter / 60);
        vm.seconds = vm.counter % 60;
        vm.counter--;   
        vm.countDown();   
      }, 1000);
    }

    vm.chooseAnswer = function(id, answer) {
      if (!vm.userAnswer[id]) vm.userAnswer[id] = answer;
      else {
        var strings = vm.userAnswer[id].split('|');
        var position = -1;
        for (var i = 0; i < strings.length; i++) 
          if (answer == strings[i]) position = i;
        if (position = -1) strings.push(answer);
        else {
          strings[position] = strings[strings.length - 1];
          strings.pop();
        }
        vm.userAnswer[id] = strings.join('|');
      }
    }

    vm.checkFillAnswer = function() {
      /*
      if (!Authentication.getAuthenticatedAccount()) {
        $('#modal_not_login').modal('show');
        return;
      }
      */
      for (var i = 0; i < vm.exam.num_exercises; i++) {
        var key = vm.exam.exercises[i].id;
        var found = false;
        if (!vm.userAnswer[key]) {
          found = true;
          vm.fillAnswer = false;
          break;
        }
      }
      if (!found) vm.fillAnswer = true;
      for (var i = 0; i < vm.exam.num_exercises; i++) {
        var key = vm.exam.exercises[i].id;
        if (!vm.userAnswer[key]) {
          // Set panel heading red
          document.getElementById("panel" + key).style.backgroundColor = '#f2dede';
          document.getElementById("panel" + key).style.color = '#a94442';
        } else {
          // Set panel heading green
          document.getElementById("panel" + key).style.backgroundColor = '#def2de';
          document.getElementById("panel" + key).style.color = '#44a942';
        }
      }
    }

    vm.submit = function() {
      vm.stop_timer = true;
      document.getElementById("button_submit").disabled = true;
      var url = "api/v1/exam/" + vm.examId + "/";
      var answer = "";
      for (var i = 0; i < vm.exam.num_exercises; i++) {
        var key = vm.exam.exercises[i].id;
        if (!vm.userAnswer[key]) answer += key + "|&";
        else answer += key + '|' + vm.userAnswer[key] + '&';
      }
      answer = answer.slice(0, answer.length - 1);
      $http.post(url, {
        "id": vm.examId,
        "exercises": answer,
        "done_time": vm.exam.time_limit - vm.counter
      })
      .then(function successCallback(response) {
        vm.score = response.data;
        $('#modal_result').modal('show');        
        getExamRecord();
      }, function errorCallback(response) {
        console.log("Error post exam answer");
      })
    }

  });

  examDetailController
    .filter('fixedLength', function () {
      return function (n, len) {
          var num = parseInt(n, 10);
          len = parseInt(len, 10);
          if (isNaN(num) || isNaN(len)) {
              return n;
          }
          num = ''+num;
          while (num.length < len) {
              num = '0'+num;
          }
          return num;
      };
    });
})();

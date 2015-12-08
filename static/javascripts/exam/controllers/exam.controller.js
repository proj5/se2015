(function() {
  var examController = angular.module('se2015.exam.controllers');
      
  examController.controller('ExamController', function($http, $routeParams) {
    var vm = this;        

    init();

    function init() {
      vm.url = "api/v1/grades/";
      $http.get(vm.url)
      .then(function successCallback(response) {
        vm.grades = response.data;        
        vm.currentGrade = vm.grades[0];                
        getExamList(vm.currentGrade.id);
      }, function errorCallback(response) {
        console.log("Error get grade list");
      });
    }

    function getExamList(gradeId) {      
      var url = "api/v1/exam_list/" + gradeId + "/";
      $http.get(url) 
      .then(function successCallback(response) {
        vm.exams = response.data;
      }, function errorCallback(response) {
        console.log("Error get skill list");
      });
    }

    vm.switchGrade = function() {
      getExamList(vm.currentGrade.id);
    };
  });
})();

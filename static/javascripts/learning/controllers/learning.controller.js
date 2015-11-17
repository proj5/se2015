(function() {
  var learningController = angular.module('se2015.learning.controllers');
      
  learningController.controller('LearningController', function($http) {
    var vm = this;    

    init();

    function init() {
      vm.url = "api/v1/grades/";
      $http.get(vm.url)
      .then(function successCallback(response) {
        vm.grades = response.data;        
        vm.currentGrade = vm.grades[0];                
        getSkills(vm.currentGrade.id);
      }, function errorCallback(response) {
        console.log("Error get grade list");
      });
    }

    function getSkills(gradeId) {      
      var skillUrl = "api/v1/exercise/" + gradeId + "/";
      $http.get(skillUrl) 
      .then(function successCallback(response) {
        vm.skills = response.data;
      }, function errorCallback(response) {
        console.log("Error get skill list");
      });
    }

    vm.switchGrade = function() {
      getSkills(vm.currentGrade.id);
    };
  });
})();

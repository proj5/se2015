(function() {
  'use strict';

  var skillController = angular.module('se2015.learning.controllers');

  skillController.controller('SkillController', function($http, $routeParams) {
    var vm = this;
    vm.url = "";    
    vm.gradeId = $routeParams.gradeId;   

    getSkillList();

    function getSkillList() {
      vm.url = "api/v1/exercise/" + vm.gradeId + "/";
      $http.get(vm.url)
      .then(function successCallback(response) {                
        vm.skills = response.data;
      }, function errorCallback(response) {
        console.log("Error");
      });
    }
  });
})();

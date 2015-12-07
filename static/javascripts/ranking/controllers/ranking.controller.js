(function() {
  var rankingController = angular.module('se2015.ranking.controllers');

  rankingController.controller('RankingController', function($http) {
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
      var exam_list_url = "api/exam_list/" + gradeId + "/";
      $http.get(exam_list_url)
      .then(function successCallback(response) {
        vm.exam_list = response.data;
      }, function errorCallback(response) {
        console.log("Error get exam list");
      });
    }

    vm.switchGrade = function() {
      getExamList(vm.currentGrade.id);
    };
  });
})();

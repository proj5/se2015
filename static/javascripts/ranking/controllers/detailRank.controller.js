(function() {
  'use strict';

  var detailRankController = angular.module('se2015.ranking.controllers');

  detailRankController.controller('DetailRankController', function($http, $routeParams) {
    var vm = this;
    vm.exam_id = $routeParams.examId;
    getExamRecord(vm.exam_id);
    getExam(vm.exam_id);

    function getExamRecord(exam_id) {
      var exam_record_url = "api/exam_record/" + exam_id + "/";
      $http.get(exam_record_url)
      .then(function successCallback(response){
        vm.exam_record = response.data;
      }, function errorCallback(response) {
        console.log("Error get exam record");
      });
    }

    function getExam(exam_id) {
      var exam_record_url = "api/exam/" + exam_id + "/";
      $http.get(exam_record_url)
      .then(function successCallback(response){
        vm.exam = response.data;
      }, function errorCallback(response) {
        console.log("Error get exam");
      });
    }

  });
})();

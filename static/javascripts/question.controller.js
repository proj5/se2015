'use strict';

var questionModule = angular.module('se2015.controllers');

questionModule.controller('QuestionController', function($http, $routeParams) { 
  var vm = this;
  vm.gradeId = $routeParams.gradeId;            
  vm.questionId = "1";
  vm.url = "api/v1/exercises/" + vm.questionId + "/";            
  vm.answer = "0";
  vm.submitted = false;    
  
  getData();
   
  function getData() {       
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
    getData();        
  };           
});

questionModule.factory('myFactory', function($resource) {
  return $resource('api/v1/exercises/:id', {
    id : '@id'}, {
    query: {
      method: 'GET',
      params: {
        id : "1"
      },        
      isArray : false
    }
  });
});
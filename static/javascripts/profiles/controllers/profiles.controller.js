(function () {
  'use strict';

  angular
    .module('se2015.profiles.controllers')
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$location', '$routeParams', 'Profile', '$http'];

  function ProfileController($location, $routeParams, Profile, $http) {
    var vm = this;

    vm.profile = undefined;

    activate();
    getRecord();

    /*
    * @desc Actions to be performed when this controller is instantiated
    */
    function activate() {
      var username = $routeParams.username.substr(0);

      Profile.get(username).then(SuccessFn, ErrorFn);

      /*
      * @desc Update `profile` on viewmodel
      */
      function SuccessFn(data, status, headers, config) {
        vm.profile = data.data;
      }

      /*
      * @desc Redirect to index and show error Snackbar
      */
      function ErrorFn(data, status, headers, config) {
        $location.url('/');
      }      
    }

    function getRecord () {
      var username = $routeParams.username.substr(0);
      $http.get('/api/v1/accounts/records/' + username + '/')
      .then(function successCallback(response) {
        vm.total_score = response.data.total_score;
        vm.count_correct_answer = response.data.count_correct_answer;
        vm.count_wrong_answer = response.data.count_wrong_answer;
        vm.total_record = response.data.total_record;
      }, function errorCallback(response) {
        console.log("Error");
      });
    }
  }
})();
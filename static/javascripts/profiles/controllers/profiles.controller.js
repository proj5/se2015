(function () {
  'use strict';

  angular
    .module('se2015.profiles.controllers')
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$location', '$routeParams', 'Profile'];

  function ProfileController($location, $routeParams, Profile) {
    var vm = this;

    vm.profile = undefined;

    activate();

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
  }
})();
(function () {
  'use strict';

  angular
    .module('se2015.profiles.controllers')
    .controller('ProfileSettingsController', ProfileSettingsController);

  ProfileSettingsController.$inject = [
    '$location', '$routeParams', 'Authentication', 'Profile'
  ];

  function ProfileSettingsController($location, $routeParams, Authentication, Profile) {
    var vm = this;

    vm.destroy = destroy;
    vm.update = update;

    activate();

    /*
    * @desc Actions to be performed when this controller is instantiated.
    */
    function activate() {
      var authenticatedAccount = Authentication.getAuthenticatedAccount();
      var username = $routeParams.username.substr(0);

      // Redirect if not logged in
      if (!authenticatedAccount) {
        $location.url('/');
      } else {
        // Redirect if logged in, but not the owner of this profile.
        if (authenticatedAccount.username !== username) {
          $location.url('/');
        }
      }

      Profile.get(username).then(SuccessFn, ErrorFn);

      /*
      * @desc Update `profile` for view
      */
      function SuccessFn(data, status, headers, config) {
        vm.profile = data.data;
      }

      /*
      * @desc Redirect to index
      */
      function ErrorFn(data, status, headers, config) {
        $location.url('/');
      }
    }


    /*
    * @desc Destroy this user's profile
    */
    function destroy() {
      Profile.destroy(vm.profile).then(SuccessFn, ErrorFn);

      /*
      * @desc Redirect to index 
      */
      function SuccessFn(data, status, headers, config) {
        Authentication.unauthenticate();
        window.location = '/';
      }


      /*
      * @desc Display error snackbar
      */
      function ErrorFn(data, status, headers, config) {
        console.log('Error when deleting profile')
      }
    }


    /*
    * @desc Update this user's profile
    */
    function update() {
      Profile.update(vm.profile).then(SuccessFn, ErrorFn);

      /*
      * @desc Show success 
      */
      function SuccessFn(data, status, headers, config) {
        console.log('Your profile has been updated.');
      }


      /**
      * @desc Show error 
      */
      function ErrorFn(data, status, headers, config) {
        console.log('Error when updating profile');
      }
    }
  }
})();
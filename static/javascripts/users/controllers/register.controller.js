(function () {
  'use strict';
  
  angular
    .module('se2015.users.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['$location', '$scope', 'Authentication'];

  /**
  * @namespace RegisterController
  */
  function RegisterController($location, $scope, Authentication) {
    var vm = this;

    vm.register = register;

    /*
    * @name register
    * @desc Register a new user
    */
    function register() {
      Authentication.register(vm.username, vm.name, vm.email, vm.password, vm.confirm_password, 
                              vm.school, vm.class_in_school);
      /*
      if (!Authentication.getAuthenticatedAccount())
        $('#modal_not_login').modal('show');
      */
    }

    activate();

    /**
     * @name activate
     * @desc Actions to be performed when this controller is instantiated
     * @memberOf se2015.users.controllers.RegisterController
     */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }
    
  }
})();
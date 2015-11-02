(function () {
  'use strict';

  angular
    .module('se2015.layout.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', 'Authentication'];

  function NavbarController($scope, Authentication) {
    var vm = this;

    vm.logout = logout;

    /*
    * @desc Log the user out
    */
    function logout() {
      Authentication.logout();
    }
  }
})();
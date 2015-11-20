(function () {
  'use strict';

  angular
    .module('se2015.layout.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['$scope', 'Authentication', '$location'];

  function NavbarController($scope, Authentication, $location) {
    var vm = this;

    vm.logout = logout;

    /*
    * @desc Log the user out
    */
    function logout() {
      Authentication.logout();
    }

    vm.isActive = function (currentLocation) {
      return currentLocation === $location.path();
    }
  }
})();
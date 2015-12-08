(function () {
  'use strict';

  angular
    .module('se2015.layout.controllers')
    .controller('MainController', MainController);

  MainController.$inject = [];

  function MainController() {
    var vm = this;

    vm.link = function(id) {
      return "static/img/Grade" + id + ".png";
    }
  }
})();
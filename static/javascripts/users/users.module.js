(function () {
  'use strict';

  angular
    .module('se2015.users', [
      'se2015.users.controllers',
      'se2015.users.services'
    ]);

  angular
    .module('se2015.users.controllers', []);

  angular
    .module('se2015.users.services', ['ngCookies']);
})();
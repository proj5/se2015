(function () {
  'use strict';

  angular
    .module('se2015.profiles.services')
    .factory('Profile', Profile);

  Profile.$inject = ['$http'];

  function Profile($http) {
    var Profile = {
      destroy: destroy,
      get: get,
      update: update
    };

    return Profile;

    /////////////////////

    /*
    * @desc Destroys the given profile
    * @param {Object} profile The profile to be destroyed
    * @returns {Promise}
    */
    function destroy(profile) {
      return $http.delete('/api/v1/accounts/' + profile.user.username + '/');
    }


    /*
    * @desc Gets the profile for user with username 'username'
    * @param {string} username The username of the user to fetch
    * @returns {Promise}
    */
    function get(username) {
      return $http.get('/api/v1/accounts/' + username + '/');
    }


    /*
    * @desc Update the given profile
    * @param {Object} profile The profile to be updated
    * @returns {Promise}
    */
    function update(profile) {
      return $http.put('/api/v1/accounts/' + profile.user.username + '/', profile);
    }
  }
})();
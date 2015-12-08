(function () {
  'use strict';

  angular
    .module('se2015.profiles.controllers', ['chart.js'])
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['$location', '$routeParams', 'Profile', '$http', '$window', 'fileUpload'];

  function ProfileController($location, $routeParams, Profile, $http, $window, fileUpload) {
    var vm = this;

    vm.profile = undefined;

    activate();
    getRecord();
    getAvatar();

    vm.labels = ["Đúng", "Sai"];

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
        vm.dataChart = [vm.count_correct_answer, vm.count_wrong_answer]
      }, function errorCallback(response) {
        console.log("Error");
      });
    }

    function getAvatar() {
      var url = "api/v1/avatar/" + $routeParams.username + "/";
      $http.get(url)
      .then(function successCallback(response) {
        vm.avatar = response.data;        
      }, function errorCallback(response) {
        console.log("Error get avatar");
      })
    }

    vm.uploadAvatar = function() {
      var file = vm.newAvatar;
      var uploadUrl = "api/v1/avatar/" + $routeParams.username + "/";
      fileUpload.uploadFileToUrl(file, uploadUrl);
      $window.location.reload();
    }
  }

  angular
    .module('se2015.profiles.controllers')
    .directive('fileModel', ['$parse', function ($parse) {
      return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            var model = $parse(attrs.fileModel);
            var modelSetter = model.assign;
            
            element.bind('change', function(){
                scope.$apply(function(){
                    modelSetter(scope, element[0].files[0]);
                });
            });
        }
      };
    }]);
})();
'use strict';

angular.module('frontendApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'ngRoute'
])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/detail/:id', {
        templateUrl: 'views/postDetail.html',
        controller: 'PostDetailCtrl'
      })
      .when('/edit/:id', {
        templateUrl: 'views/postForm.html',
        controller: 'PostEditCtrl'
      })
      .when('/new', {
        templateUrl: 'views/postForm.html',
        controller: 'PostNewCtrl'
      })
      .when('/delete/:id', {
        templateUrl: 'views/postDelete.html',
        controller: 'PostDeleteCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });

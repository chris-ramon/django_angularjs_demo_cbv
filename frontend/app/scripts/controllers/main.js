'use strict';

angular.module('frontendApp')
  .controller('MainCtrl', function ($scope, Post) {
    $scope.currentPage = 1;
    Post.query(setPosts);
    $scope.pages = function(n) {
      return new Array(n);
    }
    $scope.updateQuery = function(page) {
      $scope.currentPage = page;
      Post.query({page: page}, setPosts);
    }
    function setPosts(response) {
      $scope.posts = response.results;
      $scope.numberOfPages = response.count;
    }
  })
  .controller('PostDetailCtrl', function($scope, $routeParams, Post) {
    $scope.post = Post.get({id: $routeParams.id});
  })
  .controller('PostEditCtrl', function($scope, $routeParams, Post) {
    $scope.post = Post.get({id: $routeParams.id});
    $scope.save = function() {
      $scope.post.$update(function() {
        $scope.flashMessage = 'Post was successfully updated!';
      }, function(response) {
        $scope.flashMessage = response;
      })
    }
  })
  .controller('PostNewCtrl', function($scope, Post, $location) {
    $scope.post = new Post();
    $scope.save = function() {
      $scope.post.$save(function() {
        $location.path('/');
      });
    }
  })
  .controller('PostDeleteCtrl', function($scope, $routeParams, $location, Post) {
    $scope.post = Post.get({id: $routeParams.id});
    $scope.delete = function() {
      $scope.post.$delete(function() {
        $location.path('/');
      });
    }
    $scope.cancel = function() {
      $location.path('/detail/' + $scope.post.id);
    }
  });

// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'

function str2ab(str) {
  var buf = new ArrayBuffer(str.length); // 2 bytes for each char
  var bufView = new Uint8Array(buf);
  for (var i=0, strLen=str.length; i<strLen; i++) {
    bufView[i] = str.charCodeAt(i);
  }
  return buf;
}

angular.module('starter', ['ionic', 'ngCordova'])
.controller('Controller', function($scope, $ionicPlatform, $cordovaDeviceMotion) {
    $ionicPlatform.ready(function() {
        $scope.test = function() {
            alert('test');
        };
    });
    
    $scope.x = 0;
    $scope.y = 0;
    $scope.z = 0;
    
    var options = { frequency: 50 };
    
    var buffer = 'n'

    document.addEventListener("deviceready", function () {

        var watch = $cordovaDeviceMotion.watchAcceleration(options);
        watch.then(
          null,
          function(error) {
          // An error occurred
          },
          function(result) {
            $scope.x = result.x;
            $scope.y = result.y;
            $scope.z = result.z;

            buffer = 'nn'

            if(result.z > 7) {
              if(result.y > 4.5) buffer = 'fr'
              else if(result.y < -4.5) buffer = 'fl'
              else buffer = 'fn'
            }
            else if(result.z < 0) {
              if(result.y > 4.5) buffer = 'br'
              else if(result.y < -4.5) buffer = 'bl'
              else buffer = 'bn'
            }
            else {
              if(result.y > 4.5) buffer = 'nr'
              else if(result.y < -4.5) buffer = 'nl'
              else buffer = 'nn'
            }
              
            chrome.sockets.udp.create({}, function(socketInfo) {
              // The socket is created, now we can send some data
              var socketId = socketInfo.socketId;
              chrome.sockets.udp.send(socketId, str2ab(buffer),
                '172.24.1.1', 55056, function(sendInfo) {
                  //completed here
              });
            });
        });
      }, false);
    
  })
.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if(window.cordova && window.cordova.plugins.Keyboard) {
      // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
      // for form inputs)
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);

      // Don't remove this line unless you know what you are doing. It stops the viewport
      // from snapping when text inputs are focused. Ionic handles this internally for
      // a much nicer keyboard experience.
      cordova.plugins.Keyboard.disableScroll(true);
    }
    if(window.StatusBar) {
      StatusBar.styleDefault();
    }
      
      
  });
})

function ab2str(buf) {
  return String.fromCharCode.apply(null, new Uint16Array(buf));
}

function str2ab(str) {
  var buf = new ArrayBuffer(str.length*2); // 2 bytes for each char
  var bufView = new Uint16Array(buf);
  for (var i=0, strLen=str.length; i<strLen; i++) {
    bufView[i] = str.charCodeAt(i);
  }
  return buf;
}
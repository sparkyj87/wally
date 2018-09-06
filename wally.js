// 'use strict';
const $ = require('jQuery');
const spawn = require('child_process').spawn;
var wallpaperMacOS = require('wallpaper-macos');

let dataString = '';
let path = document.location.pathname;
path = path.substring(0, path.lastIndexOf('/')+1);
path = path + "WallpaperChanger.py";

document.getElementById("next-btn").addEventListener('click', setWallpaper);

function setWallpaper()
{
  //Spawn new python process with the path to the file to be executed
  py = spawn('python3', [path]);
  //Set the standard output of data to dataString
  py.stdout.on('data', function(data){
    dataString += data.toString();
  });
  //At the end of the function, output to console
  py.stdout.on('end', function(){
    console.log('Python Output', dataString);
  });

  // Update wallpaper of the current space
wallpaperMacOS.setOnCurrentSpace('test.jpg');
  // Update wallpaper of all spaces
  wallpaperMacOS.setOnAllSpaces('test.jpg');
};

import json
import ssl
import urllib.request
from random import randint
import subprocess
import sys
import os
# set url
url = "http://www.reddit.com/r/wallpapers/top/.json?sort=top&t=week&limit=50"
# get apple script call ready
SCRIPT = 'tell application "System Events" to tell every desktop to set picture to '

# get file path
path = "\"" + os.getcwd()
path = path + '/test.jpg' + "\""
SCRIPT = SCRIPT + path
print(SCRIPT)

class WallpaperChanger:

    pictureHeight = None
    pictureWidth = None
    imageURL = None
    output = None

    # Wont need this if changing from js
    def runAppleScript(script):
        p = subprocess.Popen(['osascript', '-e', script])

    def printInfo(self):
        # Print image info
        print("Your JSON file:")
        print (imageURL)
        print("Width: " + str(pictureWidth))
        print("Height: " + str(pictureHeight))

    def getJsonData(self):
        # Something to do with SSL verification
        # Custom user-agent so that requests are not denied due to bad requests
        # Add url and header to request
        # retrieve information and store locally
        # Load information as json file
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        hdr = {'User-Agent' : 'Wallpaper Scraper'}
        req = urllib.request.Request(url, headers=hdr)
        data = urllib.request.urlopen(req, context=gcontext).read()
        global output
        output = json.loads(data)

    def selectImage(self):

        width = 0
        height = 0
        counter = 0
        hdr = {'User-Agent': 'Wallpaper Scraper'}
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

        # Get the number of elements on the page
        numberOfElements = len(output["data"]["children"])

        # Select an image of appropriate size
        while height < 800 or width < 1280 or height > width:
            randomPic = randint(0,numberOfElements-1)
            width = output["data"]["children"][randomPic]["data"]["preview"]["images"][0]["source"]["width"]
            height = output["data"]["children"][randomPic]["data"]["preview"]["images"][0]["source"]["height"]
            imageLink = output["data"]["children"][randomPic]["data"]["url"]
            counter = counter + 1

        # Send a request to read the image file from the image URL
        req = urllib.request.Request(imageLink, headers=hdr)

        # Copy values so they can be output
        global pictureHeight
        pictureHeight = height
        global pictureWidth
        pictureWidth = width
        global imageURL
        imageURL = imageLink

        image = urllib.request.urlopen(req, context=gcontext).read()
        # Save the retrieved file as a local file
        f = open("test.jpg", "wb")
        f.write(image)
        f.close()

# Run necessary methods
changer = WallpaperChanger
changer.getJsonData(changer)
changer.selectImage(changer)
changer.printInfo(changer)

# might be able to take call out here and only use python for scraping image
# then read file in node and set as Wallpaper
# Checks to see if system is Macintosh
# comment out when done moving to js for file change
# if sys.platform == 'darwin':
#     changer.runAppleScript(SCRIPT)
#     subprocess.Popen(['killall', 'Dock'])

#==============================================================================
# AutoPinMap.py
# Purpose: Program to automatically read in a list of Twitter links, navigate
#          the web to each link, extract data required in a GoogleDoc, and then
#          insert data into the GoogleDoc. End goal is to populate a map with
#          coordinates and other information related to Tweet.
#
# Warning: Program must be configured properly and used as described in the
#          README.txt file. Not doing so can cause undesirable effects, as
#          program will move the mouse and input key strokes automatically.
#          Ensure that coordinates and colours have been configured properly.
#          mouseNow.py can be used to assist in editing the config.txt file.
#
# Created by Liam Gowan, November 2018.
#==============================================================================

import pyautogui as auto
import pyperclip as clip
import time
import datetime as dt
from timeit import default_timer as timer

startConfigAndExtractionTime = timer()

#Function selects all on line, and copys to clipboard
def copyToClip():
        auto.click()
        auto.click()
        auto.click()
        auto.hotkey('ctrl','c')

#Read in and handle configurations
config=open("config.txt","r")

#configure tab 1 location
line = config.readline()
tab1=line.split(',')
tab1[0],tab1[1] = int(tab1[0]),int(tab1[1])

#configure tab 2 location
line = config.readline()
tab2=line.split(',')
tab2[0],tab2[1] = int(tab2[0]),int(tab2[1])

#configure url bar location
line = config.readline()
URLBar=line.split(',')
URLBar[0],URLBar[1] = int(URLBar[0]),int(URLBar[1])

#configure twitter text location
line = config.readline()
twitterText=line.split(',')
twitterText[0],twitterText[1] = int(twitterText[0]),int(twitterText[1])

#configure twitter logo location
line = config.readline()
twitterBird=line.split(',')
twitterBird[0],twitterBird[1] = int(twitterBird[0]),int(twitterBird[1])

#configure twitter logo colour
line = config.readline()
twitterBirdCol=line.split(',')
twitterBirdCol[0],twitterBirdCol[1],twitterBirdCol[2] = int(twitterBirdCol[0]),int(twitterBirdCol[1]),int(twitterBirdCol[2])

#configure Garmin test point location
line = config.readline()
garminTest=line.split(',')
garminTest[0],garminTest[1] = int(garminTest[0]),int(garminTest[1])

#configure Garmin test point colour
line = config.readline()
garminTestCol=line.split(',')
garminTestCol[0],garminTestCol[1],garminTestCol[2] = int(garminTestCol[0]),int(garminTestCol[1]),int(garminTestCol[2])

#configure Garmin date location
line = config.readline()
INRDate=line.split(',')
INRDate[0],INRDate[1] = int(INRDate[0]),int(INRDate[1])

#configure Garmin date (back up) location
line = config.readline()
INRDateBackup=line.split(',')
INRDateBackup[0],INRDateBackup[1] = int(INRDateBackup[0]),int(INRDateBackup[1])

#configure Garmin text location
line = config.readline()
INRText = line.split(',')
INRText[0],INRText[1] = int(INRText[0]),int(INRText[1])

#configure Garmin more button location
line = config.readline()
INRMoreButton=line.split(',')
INRMoreButton[0],INRMoreButton[1] = int(INRMoreButton[0]),int(INRMoreButton[1])

#configure Garmin elevation location
line = config.readline()
elv=line.split(',')
elv[0],elv[1] = int(elv[0]),int(elv[1])

#configure Garmin latitude location
line = config.readline()
lat=line.split(',')
lat[0],lat[1] = int(lat[0]),int(lat[1])

#configure Garmin longitude location
line = config.readline()
lon=line.split(',')
lon[0],lon[1] = int(lon[0]),int(lon[1])

#configure Google check point 1 location
line = config.readline()
googleCheck1=line.split(',')
googleCheck1[0],googleCheck1[1] = int(googleCheck1[0]),int(googleCheck1[1])

#configure Google check point 1 colour
line = config.readline()
googleCheck1Col=line.split(',')
googleCheck1Col[0],googleCheck1Col[1],googleCheck1Col[2] = int(googleCheck1Col[0]),int(googleCheck1Col[1]),int(googleCheck1Col[2])

#configure Google tweet button location
line = config.readline()
googleTweetButton=line.split(',')
googleTweetButton[0],googleTweetButton[1] = int(googleTweetButton[0]),int(googleTweetButton[1])

#configure Google next button location
line = config.readline()
googleNextButton=line.split(',')
googleNextButton[0],googleNextButton[1] = int(googleNextButton[0]),int(googleNextButton[1])

#configure Google check point 2 location
line = config.readline()
googleCheck2=line.split(',')
googleCheck2[0],googleCheck2[1] = int(googleCheck2[0]),int(googleCheck2[1])

#configure Google check point 2 colour
line = config.readline()
googleCheck2Col=line.split(',')
googleCheck2Col[0],googleCheck2Col[1],googleCheck2Col[2] = int(googleCheck2Col[0]),int(googleCheck2Col[1]),int(googleCheck2Col[2])

#configure Google text field location
line = config.readline()
googleTextField1=line.split(',')
googleTextField1[0],googleTextField1[1] = int(googleTextField1[0]),int(googleTextField1[1])

#configure Google check point 3 location
line = config.readline()
googleCheck3=line.split(',')
googleCheck3[0],googleCheck3[1] = int(googleCheck3[0]),int(googleCheck3[1])

#configure Google check point 3 colour
line = config.readline()
googleCheck3Col=line.split(',')
googleCheck3Col[0],googleCheck3Col[1],googleCheck3Col[2] = int(googleCheck3Col[0]),int(googleCheck3Col[1]),int(googleCheck3Col[2])

#configure Google another location
line = config.readline()
googleAnother=line.split(',')
googleAnother[0],googleAnother[1] = int(googleAnother[0]),int(googleAnother[1])


#Code intentionally commented so can copy and paste new coordinates as required
#[0],[1] = int([0]),int([1])
config.close() #End configuring

#list to hold all classes containing data for each pin
allPins = []

#Reads in allLinks.txt. First line is the line for Google Form, all others are for Tweets
links = open("allLinks.txt","r")
googleDoc = links.readline() #get first line, and save
currentLink = links.readline() #read next

count = 1
#While loop handles extracting information from all Tweets/inReach sites.
while currentLink != "":
    print("Extracting data for link %d..."%count)
    count +=1
    #clean link
    currentLink = currentLink.replace("\n","")

    #pastes tweet link to search bar and looks up
    toPaste = clip.copy(currentLink)
    auto.moveTo(URLBar[0],URLBar[1])
    auto.click()
    auto.click()
    auto.click()
    auto.hotkey('ctrl','v')
    auto.hotkey('enter')

    #waits for twitter to load
    loaded = False
    while loaded ==False:
        if auto.pixel(twitterBird[0],twitterBird[1])==(twitterBirdCol[0],twitterBirdCol[1],twitterBirdCol[2]):
            loaded = True
        time.sleep(0.5)

    #copies tweet text, cleans text and extracts link to inReach
    auto.moveTo(twitterText[0],twitterText[1],0.5)
    copyToClip()
    tweet = clip.paste()
    goToLink = tweet[tweet.index("http"):]
    clip.copy(goToLink)
    tweet = tweet[:tweet.index("http")]

    #copy inReach link to broswer
    auto.click(URLBar[0],URLBar[1])
    auto.hotkey('ctrl','v')
    auto.hotkey('enter')
    time.sleep(0.5)

    #wait for inReach to load
    loaded = False
    while loaded ==False:
        if auto.pixel(garminTest[0],garminTest[1])==(garminTestCol[0],garminTestCol[1],garminTestCol[2]):
            loaded = True
        time.sleep(0.5)

    #save the real inReach link, as the first was a short one
    auto.click(URLBar[0],URLBar[1])
    auto.hotkey('ctrl','c')
    inReachURL = clip.paste()

    #get date, format and clean it as required
    auto.moveTo(INRDate[0],INRDate[1])
    copyToClip()
    auto.hotkey('ctrl','c')
    date = clip.paste()
    date = date.replace(",","")
    try:
        dtobj = dt.datetime.strptime(date,'%b %d %Y')
    except:
        auto.moveTo(INRDateBackup[0],INRDateBackup[1])
        copyToClip()
        auto.hotkey('ctrl','c')
        date = clip.paste()
        date = date.replace(",","")
    firstThree = date[0:3]
    date = str(dtobj)
    date = "'"+date[8:9].replace("0","")+date[9:10]+" "+firstThree+" "+date[:4]

    #get text
    auto.moveTo(INRText[0],INRText[1])
    copyToClip()
    inReachText = clip.paste()
    if(len(inReachText)<5):
        auto.moveTo(INRText[0],INRText[1]+20)
        copyToClip()
        inReachText = clip.paste()
    inReachText = inReachText.replace("\n","")
    inReachText = inReachText.replace("\r","")
    inReachText = inReachText.replace("\t","")

    #click more button
    auto.click(INRMoreButton[0],INRMoreButton[1])

    #get elevation and clean it
    auto.moveTo(elv[0],elv[1])
    copyToClip()
    elevation = clip.paste()
    elevation = elevation.replace("Elevation: ","")
    elevation = elevation.replace(" ft.","")
    elevation = elevation.replace(",","")
    elevation = elevation.replace("\n","")
    elevation = elevation.replace("\r","")
    elevation = elevation.replace("\t","")
    

    #get latitude and clean it
    auto.moveTo(lat[0],lat[1])
    copyToClip()
    latitude = clip.paste()
    latitude = latitude.replace("Lat: ","")
    latitude = latitude.replace("\n","")
    latitude = latitude.replace("\r","")
    latitude = latitude.replace("\t","")

    #get longitude and clean it
    auto.moveTo(lon[0],lon[1])
    copyToClip()
    longitude = clip.paste()
    longitude = longitude.replace("Lon: ","")
    longitude = longitude.replace("\n","")
    longitude = longitude.replace("\r","")
    longitude = longitude.replace("\t","")

    #save all information to object
    class pinMapInfo:
        trekDate = date
        trekTweetText = tweet
        trekTweetURL = currentLink
        trekINRText = inReachText
        trekINRURL = inReachURL
        trekLat = latitude
        trekLong = longitude
        trekElevation = elevation

    #append object to list and read next line
    allPins.append(pinMapInfo)
    currentLink = links.readline()
print("=========== ALL DATA EXTRACTED ===========\n\n")
#close links file
links.close()

#Print all data to have user confirm
for i in range(len(allPins)):
    print("Pin " +str(i+1)+" Data:")
    print("Date: %s\nTweet Text: %s\nTweet URL: %s\n" % (allPins[i].trekDate, allPins[i].trekTweetText,allPins[i].trekTweetURL) +
          "inReach Text: %s\ninReach URL: %s\nLatitude: %s\n" %(allPins[i].trekINRText, allPins[i].trekINRURL,allPins[i].trekLat)+
          "Longitude: %s\nElevation: %s\n" %(allPins[i].trekLong,allPins[i].trekElevation))

#get and print time taken for config and extraction
endConfigAndExtractionTime = timer()
totalCAETime = endConfigAndExtractionTime - startConfigAndExtractionTime
print("Time taken for configuration and extraction: " + str(dt.timedelta(seconds = int(totalCAETime))))

#Prompt user to either confirm all data is correct, or exit.
print("User, scroll up to ALL DATA EXTRACTED line, and read downwards to confirm all data is an appropriate format")
confirmation = input("Enter Y to confirm and begin data upload, or anything else to exit: ")
if(confirmation !="Y"):
    print("Exiting.")
    raise SystemExit
print("Beginning data upload")

#start timer for upload timing
startUploadTime = timer()

#Go to google forms link
toPaste = clip.copy(googleDoc)
auto.moveTo(URLBar[0],URLBar[1])
auto.click()
auto.click()
auto.click()
auto.hotkey('ctrl','v')
auto.hotkey('enter')

#Enter all informations for all pins
for i in range(len(allPins)):
    #Ensure first check has loaded
    loaded = False
    while loaded ==False:
        if auto.pixel(googleCheck1[0],googleCheck1[1])==(googleCheck1Col[0],googleCheck1Col[1],googleCheck1Col[2]):
            loaded = True
            time.sleep(0.5)
    #click tweet option button
    auto.moveTo(googleTweetButton[0],googleTweetButton[1])
    auto.click()
    auto.click()
    #click next button
    auto.moveTo(googleNextButton[0],googleNextButton[1])
    auto.click()
    #ensure second check has loaded
    loaded = False
    while loaded ==False:
        if auto.pixel(googleCheck2[0],googleCheck2[1])==(googleCheck2Col[0],googleCheck2Col[1],googleCheck2Col[2]):
            loaded = True
            time.sleep(0.5)
    #click text field
    auto.moveTo(googleTextField1[0],googleTextField1[1])
    auto.click()

    #paste date and tab
    clip.copy(allPins[i].trekDate)
    auto.hotkey('ctrl','v')
    auto.hotkey('tab')

    #paste tweet text and tab
    clip.copy(allPins[i].trekTweetText)
    auto.hotkey('ctrl','v')
    auto.hotkey('tab')

    #paste tweet url and tab
    clip.copy(allPins[i].trekTweetURL)
    auto.hotkey('ctrl','v')
    auto.hotkey('tab')

    #paste INR text and tab
    clip.copy(allPins[i].trekINRText)
    auto.hotkey('ctrl','v')
    auto.hotkey('tab')

    #paste INR url and tab
    clip.copy(allPins[i].trekINRURL)
    auto.hotkey('ctrl','v')
    auto.hotkey('tab')

    #paste latitude and tab
    clip.copy(allPins[i].trekLat)
    auto.hotkey('ctrl','v')
    auto.hotkey('tab')

    #paste longitude and tab
    clip.copy(allPins[i].trekLong)
    auto.hotkey('ctrl','v')
    auto.hotkey('tab')

    #paste longitude and tab
    clip.copy(allPins[i].trekElevation)
    auto.hotkey('ctrl','v')

    #Tab and hit the add another button
    auto.hotkey('tab')
    auto.hotkey('tab')
    auto.hotkey('enter')

    #ensure third google check has loaded
    loaded = False
    while loaded ==False:
        if auto.pixel(googleCheck3[0],googleCheck3[1])==(googleCheck3Col[0],googleCheck3Col[1],googleCheck3Col[2]):
            loaded = True
            time.sleep(0.5)

    #click another button
    auto.moveTo(googleAnother[0],googleAnother[1])
    auto.doubleClick()

#Print the upload time, and total upload time
endUploadTime = timer()
totalUploadTime = endUploadTime - startUploadTime
print("Time taken for upload: " + str(dt.timedelta(seconds = int(totalUploadTime))))
totalTime = totalCAETime + totalUploadTime
print("Total Time: " + str(dt.timedelta(seconds = int(totalTime))))

        
        
        




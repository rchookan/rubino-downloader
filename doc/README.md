## Document for developer
### What should we do?

well, rubino posts saving to ***android/data/ir.resaneh1.iptv/cache/Rubika/ru/***<br>
they not format. we must copy posts from location to user location and convert to **.jpg** or **.mp4**.<br>
also temp file in folder must deleting. (.perload and more).

so:

1. check package name for rubika, rubx and more rubika.
2. delete temp
3. check post for **.jpg** and **.mp4**
4. question from user for save rubino post
5. save rubino post

### Methods and Code

#### packageNames.py

```python
pnArray = ["ir.resaneh1.iptv", "ir.rubx.bapp"]
```
rubika, rubx and more informal rubika package name in **packageNames.py** saving.

#### Library
```python
import os
import random
import packageNames as pn

```

#### Variable
```python
successPn = "" #packageName in variable saving (ir.resaneh1.iptv and more)
whrubika = "" #(../SUCCESSPN/cache/WHRUBIKA/ru)
postArrayJPG = [] #photo file name in array saving
postArrayMP4 = [] #video file name in array saving
red = '\033[91m' #color
green = '\033[92m'
white = '\033[0m'
```

#### checkPn()

```python
global successPn, whrubika

   for i in pn.pnArray:
      cdToPn = format(os.system("cd android/data/" + i))
      if "512" in cdToPn:
         print(red + "not found: " + white + i)
      else:
         print(green + "success: " + white + i)
         successPn = i

         if "ir.re" in successPn: # ir.resaneh1.iptv
            whrubika = "Rubika"
         elif "ir.ru" in successPn: # ir.rubx.bapp
            whrubika = "Rubx"
         else:
            whrubika = "Rubika"

         break

   if successPn == "":
      print("package names in your phone not found, you can add package name in library (packagesName)")

   else:
      deleteTemp()

```
This method testing package name and if package name in folder goes to **deleteTemp()**.

#### deleteTemp()
```python
   global successPn

   os.system("cd android/data/" + successPn + "/*/*/ru; ls > listFile.txt")
   openListFile = open("android/data/" + successPn + "/cache/" + whrubika + "/ru/listFile.txt")

   listLineNumber = 0
   linewhile = "none"

   while linewhile == "none":
      line = openListFile.readline()
      if line == "":
         linewhile = ""
         checkPost()
      else:
         if "." in line:
            os.system("rm android/data/" + successPn + "/*/*/ru/" + line)
            listLineNumber = listLineNumber + 1
```

This method create ***listFile.txt** in ***../SUCCESSPN/cache/WHRUBIKA/ru/*** and read name post from ***listFile.txt***<br>.
so goes to **checkPost()**.

#### checkPost()
```python
   global successPn, postArrayJPG, postArrayMP4, whrubika

   os.system("cd android/data/" + successPn + "/*/*/ru; ls > listFile.txt")
   openListFile = open("android/data/" + successPn + "/cache/" + whrubika + "/ru/listFile.txt")
   linewhile = "none"

   while linewhile == "none":
      line = openListFile.readline()
      if line == "":
         linewhile = ""
      else:
         openPost = open("android/data/" + successPn + "/cache/" + whrubika + "/ru/" + line[0:-1], "rb")
         post = openPost.read(20)

         if b'JFIF' in post:
            postArrayJPG.append(line)
         else:
            if "listFile.txt" in line:
               m = ""
            else:
               postArrayMP4.append(line)

   os.system("rm android/data/" + successPn + "/*/*/ru/listfile.txt")
   loopArray()
```

well, we must read posts; if "JFIF" in posts, it's file photo. and in last photo and video to array adding and we to **loopArray()** going.

#### loopArray()
```python
  global successPn, postArrayJPG, postArrayMP4

   locationSave1 = input("please enter your location for save rubino post (sdcard): ")

   for x in postArrayJPG:
      savePost(locationSave1, x, ".jpg")

   for y in postArrayMP4:
      savePost(locationSave1, y, ".mp4")

   beforePostQuestion = input("Are you delete before rubino posts? (y/n)")
   if "y" == beforePostQuestion or "Y" == beforePostQuestion:
      os.system("rm android/data/" + successPn + "/cache/" + whrubika + "/ru/*")
   elif "n" == beforePostQuestion or "N" == beforePostQuestion:
      print("Good Luck!")
   else:
      print("what?")

```

now, location save, file name and type for **savePost** sended.<br>
so from user question for delete before rubino post.

#### savePost(locationSave, post, type)
```python
   global successPn

   cpFormat = format(os.system("cd android/data/" + successPn + "/*/*/ru; cp " + post[0:-1] + " ../../../../.$

   if "0" in cpFormat:
      print(green + "---- saved in " + white + locationSave + green + " ----" + white)
   else:
      os.system("mkdir " + locationSave)
      print(red + "folder not found, " + white + locationSave + green + " created." + white)

      cpFormat = format(os.system("cd android/data/" + successPn + "/*/*/ru; cp " + post[0:-1] + " ../../../.$

      if "0" in cpFormat:
         print(green + "---- saved in " + white + locationSave + green + " ----" + white)
      else:
         print(red + "not saved ... -_-" + white)
```

This method saving post. if post not saved, create user folder and saving post.

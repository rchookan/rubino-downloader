# pn = package name
#methods: 1.checkPn / 2.deleteTemp / 3.checkPost / 4.loopArray / 5.savePost

import os
import random
import packageNames as pn

successPn = ""
whrubika = ""
postArrayJPG = []
postArrayMP4 = []
red = '\033[91m'
green = '\033[92m'
white = '\033[0m'

def savePost(locationSave, post, type):
   global successPn

   cpFormat = format(os.system("cd android/data/" + successPn + "/*/*/ru; cp " + post[0:-1] + " ../../../../../../" + locationSave +  "/" + str(random.randrange(100000000, 999999999)) + type))
   
   if "0" in cpFormat:
      print(green + "---- saved in " + white + locationSave + green + " ----" + white)
   else:
      os.system("mkdir " + locationSave)
      print(red + "folder not found, " + white + locationSave + green + " created." + white)
   
      cpFormat = format(os.system("cd android/data/" + successPn + "/*/*/ru; cp " + post[0:-1] + " ../../../../../../" + locationSave + "/" + str(random.randrange(100000000, 999999999)) + type))
   
      if "0" in cpFormat:
         print(green + "---- saved in " + white + locationSave + green + " ----" + white)
      else:
         print(red + "not saved ... -_-" + white)

def loopArray():
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

def checkPost():
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

def deleteTemp():
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

def checkPn():
   global successPn, whrubika

   print("check package name ...")

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

checkPn()

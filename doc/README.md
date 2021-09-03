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
      print("package names in your phone not found, you can add package name in$
   else:
      deleteTemp()

```
this method ...

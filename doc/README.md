## Document for developer
### What should we do?

well, rubino posts saving to ***android/data/ir.resaneh1.iptv/cache/Rubika/ru/***.<br>
they not format. we must copy posts from location to user location and convert to **.jpg** or **.mp4**.
also temp file in folder must deleting. (.perload and more)

so:

1. check package name for rubika, rubx and more rubika.
2. delete temp
3. check post for **.jpg** and **.mp4**
4. question from user for save rubino post
5. save rubino post

### Methods

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

```
this method ...

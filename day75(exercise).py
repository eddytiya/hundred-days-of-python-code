#day75(exercise)
#using operating system module
#os module
#clearing the clutter

'''
Write a program to clear the clutter inside a folder on your computer. 
You should use os module to rename all the png images from 1.png all the way till n.png 
where n is the number of png files in that folder. 
Do the same for other file formats. 
For example:

sfdsf.png --> 1.png
vfsf.png --> 2.png
this.png --> 3.png
design.png --> 4.png
name.png --> 5.png

'''

import os

files = os.listdir("day75")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"day75/{file}", f"day75/{i}.png")
    i = i + 1
#checking
#os.rename("day75/file.txt","day75/6.txt")


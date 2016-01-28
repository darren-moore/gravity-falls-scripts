#Splices new emotes into the spritesheet.

from PIL import Image, ImageDraw
import os

#Change Filepath
os.chdir('path/to/file')
f = Image.open("bsheet.png")
sprite = Image.open("1 - tB47sBF.png")
f.convert("RGBA")
emote = []
x = 0
while x < 4:
    y = 0
    while y < 10:
        box = (x*70, y*70, (x+1)*70, (y+1)*70)
        emote.append(f.crop(box))
        y+=1
    x+=1

emote.insert(7,sprite);
newSheet = Image.new('RGBA', (280,700))
x = 0
ctr = 0
while x < 4:
    y = 0
    while y < 10:
        newSheet.paste(emote[ctr],(x*70, y*70))
        emote.append(f.crop(box))
        y+=1
        ctr+=1
    x+=1

newSheet.save('newSheet.png')

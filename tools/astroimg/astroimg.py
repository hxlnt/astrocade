from PIL import Image
import statistics
import sys

def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

img = Image.open(sys.argv[1])
palette = {} 
palette = set()
blackxpos = {} 
blackxpos = set()
bluexpos = {} 
bluexpos = set()
cyanxpos = {} 
cyanxpos = set()
greenxpos = {} 
greenxpos = set()
magentaxpos = {} 
magentaxpos = set()
redxpos = {} 
redxpos = set()
whitexpos = {} 
whitexpos = set()
yellowxpos = {} 
yellowxpos = set()
paletteBoundary = 0
redcounter = magentacounter = bluecounter = cyancounter = yellowcounter = greencounter = blackcounter = whitecounter = 0
img.thumbnail((160,102))
pixelMap = img.load()

for y in range(img.size[1]):
    for x in range(img.size[0]):
        hsvpixel = rgb2hsv(pixelMap[x,y][0], pixelMap[x,y][1], pixelMap[x,y][2])
        if hsvpixel[1] >= .15 and hsvpixel[2] >= .4:
            if (hsvpixel[0] < 35 or hsvpixel[0] > 340):
                pixelMap[x,y] = (255,0,0)
                palette.add("#FF0000")
                redxpos.add(x)
                redcounter += 1
            elif (hsvpixel[0] >= 35 and hsvpixel[0] < 70):
                pixelMap[x,y] = (255,255,0)
                palette.add("#FFFF00")
                yellowxpos.add(x)
                yellowcounter += 1
            elif (hsvpixel[0] >= 70 and hsvpixel[0] < 155):
                pixelMap[x,y] = (0,255,0)
                palette.add("#00FF00")
                greenxpos.add(x)
                greencounter += 1
            elif (hsvpixel[0] >= 155 and hsvpixel[0] < 190):
                pixelMap[x,y] = (0,255,255)
                palette.add("#00FFFF")
                cyanxpos.add(x)
                cyancounter += 1
            elif (hsvpixel[0] >= 190 and hsvpixel[0] < 250):
                pixelMap[x,y] = (0,0,255)
                palette.add("#0000FF")
                bluexpos.add(x)
                bluecounter += 1
            elif (hsvpixel[0] >= 255 and hsvpixel[0] <= 340):
                pixelMap[x,y] = (255,0,255)
                palette.add("#FF00FF")
                magentaxpos.add(x)
                magentacounter += 1
        elif hsvpixel[1] < .15 and hsvpixel[2] >= .4:
            pixelMap[x,y] = (255,255,255)
            palette.add("#FFFFFF")
            whitexpos.add(x)
            whitecounter += 1
        else:
            pixelMap[x,y] = (0,0,0)
            palette.add("#000000")
            blackxpos.add(x)
            blackcounter += 1
minmax = []
if len(redxpos) > 0 and redcounter > 160:
    minmax.append(min(redxpos))
    minmax.append(max(redxpos))
if len(magentaxpos) > 0 and magentacounter > 160:
    minmax.append(min(magentaxpos))
    minmax.append(max(magentaxpos))
if len(bluexpos) > 0 and bluecounter > 160:
    minmax.append(min(bluexpos))
    minmax.append(max(bluexpos))
if len(cyanxpos) > 0 and cyancounter > 160:
    minmax.append(min(cyanxpos))
    minmax.append(max(cyanxpos))
if len(greenxpos) > 0 and greencounter > 160:
    minmax.append(min(greenxpos))
    minmax.append(max(greenxpos))
if len(yellowxpos) > 0 and yellowcounter > 160:
    minmax.append(min(yellowxpos))
    minmax.append(max(yellowxpos))
if len(blackxpos) > 0 and blackcounter > 160:
    minmax.append(min(blackxpos))
    minmax.append(max(blackxpos))
if len(whitexpos) > 0 and whitecounter > 160:
    minmax.append(min(whitexpos))
    minmax.append(max(whitexpos))
median = round(statistics.median(minmax))
adjustedmedian = median + (median % 4)
print(adjustedmedian)

imgleft = img.crop((0, 0, adjustedmedian, 102))
imgright = img.crop((adjustedmedian, 0, 160, 102))
imgleft.show()
#imgright.show()
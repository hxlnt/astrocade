from PIL import Image
import math
import statistics
import sys

palette = blackxpos = bluexpos = cyanxpos = greenxpos = magentaxpos = redxpos = whitexpos = yellowxpos = {} 
palette = set()
blackxpos = set()
bluexpos = set()
cyanxpos = set()
greenxpos = set()
magentaxpos = set()
redxpos = set()
whitexpos = set() 
yellowxpos = set()
adjustedmedian = paletteBoundary = 0
redcounter = magentacounter = cyancounter = bluecounter = yellowcounter = greencounter = blackcounter = whitecounter = 0
imgleft = None
imgright = None

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

def eightColorDownsample(img):
    global redcounter, yellowcounter, greencounter, cyancounter, bluecounter, magentacounter, whitecounter, blackcounter, redxpos, yellowxpos, greenxpos, cyanxpos, bluexpos, magentaxpos, whitexpos, blackxpos
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixelMap = img.load()
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
    img.show()

def colorBoundaryFinder(img):
    global redcounter, yellowcounter, greencounter, cyancounter, bluecounter, magentacounter, whitecounter, blackcounter, redxpos, yellowxpos, greenxpos, cyanxpos, bluexpos, magentaxpos, whitexpos, blackxpos, imgleft, imgright, adjustedmedian
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
    adjustedmedian = int(math.floor(median + (median % 4)))
    print(adjustedmedian)
    imgleft = img.crop((0, 0, adjustedmedian, 102))
    imgright = img.crop((adjustedmedian, 0, 160, 102))

def colorCounter(img):
    global redcounter, yellowcounter, greencounter, cyancounter, bluecounter, magentacounter, whitecounter, blackcounter
    redcounter = yellowcounter = greencounter = cyancounter = bluecounter = magentacounter = whitecounter = blackcounter = 0
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixelMap = img.load()
            if pixelMap[x,y] == (255,0,0):
                redcounter += 1
            elif pixelMap[x,y] == (255,255,0):
                yellowcounter += 1
            elif pixelMap[x,y] == (0,255,0):
                greencounter += 1
            elif pixelMap[x,y] == (0,255,255):
                cyancounter += 1
            elif pixelMap[x,y] == (0,0,255):
                bluecounter += 1
            elif pixelMap[x,y] == (255,0,255):
                magentacounter += 1
            elif pixelMap[x,y] == (0,0,0):
                blackcounter += 1
            else:
                whitecounter += 1


def colorRoller(colors_to_keep, colors_to_roll, img):
    if "red" in colors_to_roll:
        if "magenta" in colors_to_keep:
            colorSwapper((255,0,255), (255,0,0), img)
        elif "yellow" in colors_to_keep:
            colorSwapper((255,255,0), (255,0,0), img)
        elif "black" in colors_to_keep:
            colorSwapper((0,0,0), (255,0,0), img)
        elif "white" in colors_to_keep:
            colorSwapper((255,255,255), (255,0,0), img)
        colors_to_roll.remove("red")
        if len(colors_to_roll) == 0:
            return
    if "magenta" in colors_to_roll:
        if "red" in colors_to_keep:
            colorSwapper((255,0,0), (255,0,255), img)
        elif "blue" in colors_to_keep:
            colorSwapper((0,0,255), (255,0,255), img)
        elif "white" in colors_to_keep:
            colorSwapper((255,255,255), (255,0,255), img)
        elif "black" in colors_to_keep:
            colorSwapper((0,0,0), (255,0,255), img)
        colors_to_roll.remove("magenta")
        if len(colors_to_roll) == 0:
            return
    if "blue" in colors_to_roll:
        if "cyan" in colors_to_keep:
            colorSwapper((0,255,255), (0,0,255), img)
        elif "magenta" in colors_to_keep:
            colorSwapper((255,0,255), (0,0,255), img)
        elif "black" in colors_to_keep:
            colorSwapper((0,0,0), (0,0,255), img)
        elif "white" in colors_to_keep:
            colorSwapper((255,255,255), (0,0,255), img)
        colors_to_roll.remove("blue")
        if len(colors_to_roll) == 0:
            return
    if "cyan" in colors_to_roll:
        if "blue" in colors_to_keep:
            colorSwapper((0,0,255), (0,255,255), img)
        elif "green" in colors_to_keep:
            colorSwapper((0,255,0), (0,255,255), img)
        elif "white" in colors_to_keep:
            colorSwapper((255,255,255), (0,255,255), img)
        elif "yellow" in colors_to_keep:
            colorSwapper((255,255,0), (0,255,255), img)
        colors_to_roll.remove("cyan")
        if len(colors_to_roll) == 0:
            return
    if "green" in colors_to_roll:
        if "cyan" in colors_to_keep:
            colorSwapper((0,255,255), (0,255,0), img)
        elif "yellow" in colors_to_keep:
            colorSwapper((255,255,0), (0,255,0), img)
        elif "blue" in colors_to_keep:
            colorSwapper((0,0,255), (0,255,0), img)
        elif "black" in colors_to_keep:
            colorSwapper((0,0,0), (0,255,0), img)
        colors_to_roll.remove("green")
        if len(colors_to_roll) == 0:
            return
    if "yellow" in colors_to_roll:
        if "white" in colors_to_keep:
            colorSwapper((255,255,255), (255,255,0), img)
        elif "green" in colors_to_keep:
            colorSwapper((0,255,0), (255,255,0), img)  
        elif "red" in colors_to_keep:
            colorSwapper((255,0,0), (255,255,0), img)        
        elif "cyan" in colors_to_keep:
            colorSwapper((0,255,255), (255,255,0), img)
        colors_to_roll.remove("yellow")
        if len(colors_to_roll) == 0:
            return
    if "black" in colors_to_roll:
        if "blue" in colors_to_keep:
            colorSwapper((0,0,255), (0,0,0), img)
        elif "red" in colors_to_keep:
            colorSwapper((255,0,0), (0,0,0), img)  
        elif "green" in colors_to_keep:
            colorSwapper((0,0,255), (0,0,0), img)        
        elif "magenta" in colors_to_keep:
            colorSwapper((255,0,255), (0,0,0), img)
        colors_to_roll.remove("black")
        if len(colors_to_roll) == 0:
            return
    if "white" in colors_to_roll:
        if "yellow" in colors_to_keep:
            colorSwapper((255,255,0), (255,255,255), img)
        elif "cyan" in colors_to_keep:
            colorSwapper((0,255,255), (255,255,255), img)  
        elif "magenta" in colors_to_keep:
            colorSwapper((255,0,255), (255,255,255), img)        
        elif "green" in colors_to_keep:
            colorSwapper((0,255,0), (255,255,255), img)
        colors_to_roll.remove("white")
        if len(colors_to_roll) == 0:
            return

def colorSwapper(color_to_keep, color_to_roll, img):
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixelMap = img.load()
            if pixelMap[x,y] == color_to_roll:
                pixelMap[x,y] = color_to_keep


img = Image.open(sys.argv[1])
img = img.resize([160,102],Image.ANTIALIAS)
eightColorDownsample(img)
colorBoundaryFinder(img)

colorCounter(imgleft)
leftcolors = {"red":redcounter, "yellow":yellowcounter, "green":greencounter, "cyan":cyancounter, "blue":bluecounter, "magenta":magentacounter, "black":blackcounter, "white":whitecounter}
leftcolors = sorted(iter(leftcolors.items()), key=lambda k_v: (k_v[1],k_v[0]))
print("leftcolors: ", leftcolors)
colors_to_roll = [leftcolors[0][0], leftcolors[1][0], leftcolors[2][0], leftcolors[3][0]]
colors_to_keep = [leftcolors[4][0], leftcolors[5][0], leftcolors[6][0], leftcolors[7][0]]
colorRoller(colors_to_keep, colors_to_roll, imgleft)
colorCounter(imgright)
rightcolors = {"red":redcounter, "yellow":yellowcounter, "green":greencounter, "cyan":cyancounter, "blue":bluecounter, "magenta":magentacounter, "black":blackcounter, "white":whitecounter}
rightcolors = sorted(iter(rightcolors.items()), key=lambda k_v: (k_v[1],k_v[0]))
print("rightcolors: ", rightcolors)
colors_to_roll = [rightcolors[0][0], rightcolors[1][0], rightcolors[2][0], rightcolors[3][0]]
colors_to_keep = [rightcolors[4][0], rightcolors[5][0], rightcolors[6][0], rightcolors[7][0]]
colorRoller(colors_to_keep, colors_to_roll, imgright)
newimg = Image.new("RGB", (160,102))
newimg.paste(imgleft, (0,0))
newimg.paste(imgright, (adjustedmedian, 0))
newimg.show()
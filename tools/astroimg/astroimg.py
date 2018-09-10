import math
import os.path
from PIL import Image, ImageEnhance
import statistics
import sys

class Pixel:
    
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def toHSV(self):
        self.r, self.g, self.b = self.r / 255.0, self.g / 255.0, self.b / 255.0
        maxrgb = max(self.r, self.g, self.b)
        minrgb = min(self.r, self.g, self.b)
        df = maxrgb - minrgb
        if maxrgb == minrgb:
            h = 0
        elif maxrgb == self.r:
            h = (60 * ((self.g - self.b) / df) + 360) % 360
        elif maxrgb == self.g:
            h = (60 * ((self.b - self.r) / df) + 120) % 360
        elif maxrgb == self.b:
            h = (60 * ((self.r - self.g) / df) + 240) % 360
        if maxrgb == 0:
            s = 0
        else:
            s = df/maxrgb
        v = maxrgb
        return round(h, 3), round(s, 3), round(v, 3)

    def toHex(self):
        self.toEightColorRGB()
        if self.r == 255:
            if self.g == 255:
                if self.b == 255:
                    return 0x07
                else:
                    return 0x77
            elif self.b == 255:
                return 0x2F
            else:
                return 0x6C
        else:
            if self.g == 255:
                if self.b == 255:
                    return 0xD5
                else: 
                    return 0xAE
            elif self.b == 255:
                return 0xEC
            else:
                return 0x00

    def toAstroRGB(self):
        self.toEightColorRGB()
        if self.r == 0 and self.g == 255 and self.b == 255:
            return (5, 255, 255)
        elif self.r == 0 and self.g == 0 and self.b == 255:
            return (39, 168, 255)
        elif self.r == 255 and self.g == 0 and self.b == 255:
            return (255, 152, 255)
        elif self.r == 255 and self.g == 0 and self.b == 0:
            return (255, 85, 39)
        elif self.r == 255 and self.g == 255 and self.b == 0:
            return (255, 252, 78)
        else:
            return (59, 255, 112)

    def toEightColorRGB(self):
        hsv = self.toHSV()
        if hsv[1] >= .15 and hsv[2] >= .4:
            if (hsv[0] < 35 or hsv[0] > 340):
                self.r = 255
                self.g = 0 
                self.b = 0
            elif (hsv[0] >= 35 and hsv[0] < 70):
                self.r = 255
                self.g = 255
                self.b = 0
            elif (hsv[0] >= 70 and hsv[0] < 155):
                self.r = 0
                self.g = 255
                self.b = 0
            elif (hsv[0] >= 155 and hsv[0] < 190):
                self.r = 0
                self.g = 255
                self.b = 255
            elif (hsv[0] >= 190 and hsv[0] < 250):
                self.r = 0
                self.g = 0
                self.b = 255
            elif (hsv[0] >= 255 and hsv[0] <= 340):
                self.r = 255
                self.g = 0
                self.b = 255
        elif hsv[1] < .15 and hsv[2] >= .4:
            self.r = 255
            self.g = 255
            self.b = 255
        else:
            self.r = 0
            self.g = 0
            self.b = 0
        return self.r, self.g, self.b


class Img:
    
    def __init__(self, imgpath):
        self.imgpath = imgpath
        self.img = Image.open(imgpath)
        self.pixelMap = self.img.load()
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        self.colorcount = {}
        self.colorxpos = {}
        self.colorboundary = 0
    
    def eightColorCount(self):
        red = yellow = green = cyan = blue = magenta = black = white = 0
        for y in range(self.height):
            for x in range(self.width):
                thiscolor = Pixel(self.pixelMap[x,y][0], self.pixelMap[x,y][1], self.pixelMap[x,y][2]).toEightColorRGB()
                if thiscolor == (255,0,0):
                    red += 1
                elif thiscolor == (255,255,0):
                    yellow += 1
                elif thiscolor == (0,255,0):
                    green+= 1
                elif thiscolor == (0,255,255):
                    cyan += 1
                elif thiscolor == (0,0,255):
                    blue += 1
                elif thiscolor == (255,0,255):
                    magenta += 1
                elif thiscolor == (0,0,0):
                    black += 1
                else:
                    white += 1
        self.colorcount.update({
            'red': red,
            'yellow': yellow,
            'green': green,
            'cyan': cyan,
            'blue': blue,
            'magenta': magenta,
            'black': black,
            'white': white
            })
        print('colorcount: ', self.colorcount)
        return self.colorcount


#################################################################

# palette = blackxpos = bluexpos = cyanxpos = greenxpos = magentaxpos = redxpos = whitexpos = yellowxpos = {} 
# palette = set()
# blackxpos = set()
# bluexpos = set()
# cyanxpos = set()
# greenxpos = set()
# magentaxpos = set()
# redxpos = set()
# whitexpos = set()
# yellowxpos = set()
# adjustedmedian = 0
# paletteBoundary = 0
# redcounter = magentacounter = cyancounter = bluecounter = yellowcounter = greencounter = blackcounter = whitecounter = 0
# imgleft = None
# imgright = None


# def eightColorDownsample(img):
#     global redcounter, yellowcounter, greencounter, cyancounter, bluecounter, magentacounter, whitecounter, blackcounter, redxpos, yellowxpos, greenxpos, cyanxpos, bluexpos, magentaxpos, whitexpos, blackxpos
#     for y in range(img.size[1]):
#         for x in range(img.size[0]):
#             pixelMap = img.load()
#             hsvpixel = rgb2hsv(pixelMap[x,y][0], pixelMap[x,y][1], pixelMap[x,y][2])
#             if self.g >= .15 and self.b >= .4:
#                 if (self.r < 35 or self.r > 340):
#                     pixelMap[x,y] = (255,0,0)
#                     palette.add("#FF0000")
#                     redxpos.add(x)
#                     redcounter += 1
#                 elif (self.r >= 35 and self.r < 70):
#                     pixelMap[x,y] = (255,255,0)
#                     palette.add("#FFFF00")
#                     yellowxpos.add(x)
#                     yellowcounter += 1
#                 elif (self.r >= 70 and self.r < 155):
#                     pixelMap[x,y] = (0,255,0)
#                     palette.add("#00FF00")
#                     greenxpos.add(x)
#                     greencounter += 1
#                 elif (self.r >= 155 and self.r < 190):
#                     pixelMap[x,y] = (0,255,255)
#                     palette.add("#00FFFF")
#                     cyanxpos.add(x)
#                     cyancounter += 1
#                 elif (self.r >= 190 and self.r < 250):
#                     pixelMap[x,y] = (0,0,255)
#                     palette.add("#0000FF")
#                     bluexpos.add(x)
#                     bluecounter += 1
#                 elif (self.r >= 255 and self.r <= 340):
#                     pixelMap[x,y] = (255,0,255)
#                     palette.add("#FF00FF")
#                     magentaxpos.add(x)
#                     magentacounter += 1
#             elif self.g < .15 and self.b >= .4:
#                 pixelMap[x,y] = (255,255,255)
#                 palette.add("#FFFFFF")
#                 whitexpos.add(x)
#                 whitecounter += 1
#             else:
#                 pixelMap[x,y] = (0,0,0)
#                 palette.add("#000000")
#                 blackxpos.add(x)
#                 blackcounter += 1


# def colorBoundaryFinder(img):
#     global redcounter, yellowcounter, greencounter, cyancounter, bluecounter, magentacounter, whitecounter, blackcounter, redxpos, yellowxpos, greenxpos, cyanxpos, bluexpos, magentaxpos, whitexpos, blackxpos, imgleft, imgright, adjustedmedian
#     minmax = []
#     if len(redxpos) > 0 and redcounter > 160:
#         minmax.append(min(redxpos))
#         minmax.append(max(redxpos))
#     if len(magentaxpos) > 0 and magentacounter > 160:
#         minmax.append(min(magentaxpos))
#         minmax.append(max(magentaxpos))
#     if len(bluexpos) > 0 and bluecounter > 160:
#         minmax.append(min(bluexpos))
#         minmax.append(max(bluexpos))
#     if len(cyanxpos) > 0 and cyancounter > 160:
#         minmax.append(min(cyanxpos))
#         minmax.append(max(cyanxpos))
#     if len(greenxpos) > 0 and greencounter > 160:
#         minmax.append(min(greenxpos))
#         minmax.append(max(greenxpos))
#     if len(yellowxpos) > 0 and yellowcounter > 160:
#         minmax.append(min(yellowxpos))
#         minmax.append(max(yellowxpos))
#     if len(blackxpos) > 0 and blackcounter > 160:
#         minmax.append(min(blackxpos))
#         minmax.append(max(blackxpos))
#     if len(whitexpos) > 0 and whitecounter > 160:
#         minmax.append(min(whitexpos))
#         minmax.append(max(whitexpos))
#     median = round(statistics.median(minmax))
#     adjustedmedian = int(math.floor(median - (median % 4)))
#     imgleft = img.crop((0, 0, adjustedmedian, 102))
#     imgright = img.crop((adjustedmedian, 0, 160, 102))


# def colorCounter(img):
#     global redcounter, yellowcounter, greencounter, cyancounter, bluecounter, magentacounter, whitecounter, blackcounter
#     redcounter = yellowcounter = greencounter = cyancounter = bluecounter = magentacounter = whitecounter = blackcounter = 0
#     for y in range(img.size[1]):
#         for x in range(img.size[0]):
#             pixelMap = img.load()
#             if pixelMap[x,y] == (255,0,0):
#                 redcounter += 1
#             elif pixelMap[x,y] == (255,255,0):
#                 yellowcounter += 1
#             elif pixelMap[x,y] == (0,255,0):
#                 greencounter += 1
#             elif pixelMap[x,y] == (0,255,255):
#                 cyancounter += 1
#             elif pixelMap[x,y] == (0,0,255):
#                 bluecounter += 1
#             elif pixelMap[x,y] == (255,0,255):
#                 magentacounter += 1
#             elif pixelMap[x,y] == (0,0,0):
#                 blackcounter += 1
#             else:
#                 whitecounter += 1


# def colorRoller(colors_to_keep, colors_to_roll, img):
#     if "red" in colors_to_roll:
#         if "magenta" in colors_to_keep:
#             colorSwapper((255,0,255), (255,0,0), img)
#         elif "yellow" in colors_to_keep:
#             colorSwapper((255,255,0), (255,0,0), img)
#         elif "black" in colors_to_keep:
#             colorSwapper((0,0,0), (255,0,0), img)
#         elif "white" in colors_to_keep:
#             colorSwapper((255,255,255), (255,0,0), img)
#         colors_to_roll.remove("red")
#         if len(colors_to_roll) == 0:
#             return
#     if "magenta" in colors_to_roll:
#         if "red" in colors_to_keep:
#             colorSwapper((255,0,0), (255,0,255), img)
#         elif "blue" in colors_to_keep:
#             colorSwapper((0,0,255), (255,0,255), img)
#         elif "white" in colors_to_keep:
#             colorSwapper((255,255,255), (255,0,255), img)
#         elif "black" in colors_to_keep:
#             colorSwapper((0,0,0), (255,0,255), img)
#         colors_to_roll.remove("magenta")
#         if len(colors_to_roll) == 0:
#             return
#     if "blue" in colors_to_roll:
#         if "cyan" in colors_to_keep:
#             colorSwapper((0,255,255), (0,0,255), img)
#         elif "magenta" in colors_to_keep:
#             colorSwapper((255,0,255), (0,0,255), img)
#         elif "black" in colors_to_keep:
#             colorSwapper((0,0,0), (0,0,255), img)
#         elif "white" in colors_to_keep:
#             colorSwapper((255,255,255), (0,0,255), img)
#         colors_to_roll.remove("blue")
#         if len(colors_to_roll) == 0:
#             return
#     if "cyan" in colors_to_roll:
#         if "blue" in colors_to_keep:
#             colorSwapper((0,0,255), (0,255,255), img)
#         elif "green" in colors_to_keep:
#             colorSwapper((0,255,0), (0,255,255), img)
#         elif "white" in colors_to_keep:
#             colorSwapper((255,255,255), (0,255,255), img)
#         elif "yellow" in colors_to_keep:
#             colorSwapper((255,255,0), (0,255,255), img)
#         colors_to_roll.remove("cyan")
#         if len(colors_to_roll) == 0:
#             return
#     if "green" in colors_to_roll:
#         if "cyan" in colors_to_keep:
#             colorSwapper((0,255,255), (0,255,0), img)
#         elif "yellow" in colors_to_keep:
#             colorSwapper((255,255,0), (0,255,0), img)
#         elif "blue" in colors_to_keep:
#             colorSwapper((0,0,255), (0,255,0), img)
#         elif "black" in colors_to_keep:
#             colorSwapper((0,0,0), (0,255,0), img)
#         colors_to_roll.remove("green")
#         if len(colors_to_roll) == 0:
#             return
#     if "yellow" in colors_to_roll:
#         if "white" in colors_to_keep:
#             colorSwapper((255,255,255), (255,255,0), img)
#         elif "green" in colors_to_keep:
#             colorSwapper((0,255,0), (255,255,0), img)  
#         elif "red" in colors_to_keep:
#             colorSwapper((255,0,0), (255,255,0), img)        
#         elif "cyan" in colors_to_keep:
#             colorSwapper((0,255,255), (255,255,0), img)
#         colors_to_roll.remove("yellow")
#         if len(colors_to_roll) == 0:
#             return
#     if "black" in colors_to_roll:
#         if "blue" in colors_to_keep:
#             colorSwapper((0,0,255), (0,0,0), img)
#         elif "red" in colors_to_keep:
#             colorSwapper((255,0,0), (0,0,0), img)  
#         elif "green" in colors_to_keep:
#             colorSwapper((0,0,255), (0,0,0), img)        
#         elif "magenta" in colors_to_keep:
#             colorSwapper((255,0,255), (0,0,0), img)
#         colors_to_roll.remove("black")
#         if len(colors_to_roll) == 0:
#             return
#     if "white" in colors_to_roll:
#         if "yellow" in colors_to_keep:
#             colorSwapper((255,255,0), (255,255,255), img)
#         elif "cyan" in colors_to_keep:
#             colorSwapper((0,255,255), (255,255,255), img)  
#         elif "magenta" in colors_to_keep:
#             colorSwapper((255,0,255), (255,255,255), img)        
#         elif "green" in colors_to_keep:
#             colorSwapper((0,255,0), (255,255,255), img)
#         colors_to_roll.remove("white")
#         if len(colors_to_roll) == 0:
#             return


# def colorSwapper(color_to_keep, color_to_roll, img):
#     for y in range(img.size[1]):
#         for x in range(img.size[0]):
#             pixelMap = img.load()
#             if pixelMap[x,y] == color_to_roll:
#                 pixelMap[x,y] = color_to_keep


# def z80Exporter(newimg):
#     global palette
#     pixelMap = newimg.load()
#     currentbyte = 0x00
#     export = []
#     palette = [leftcolors[4][0], leftcolors[5][0], leftcolors[6][0], leftcolors[7][0], rightcolors[4][0], rightcolors[5][0], rightcolors[6][0], rightcolors[7][0]]
#     palette = [pal.replace('red', '(255, 0, 0)') for pal in palette]
#     palette = [pal.replace('magenta', '(255, 0, 255)') for pal in palette]
#     palette = [pal.replace('blue', '(0, 0, 255)') for pal in palette]
#     palette = [pal.replace('cyan', '(0, 255, 255)') for pal in palette]
#     palette = [pal.replace('green', '(0, 255, 0)') for pal in palette]
#     palette = [pal.replace('yellow', '(255, 255, 0)') for pal in palette]
#     palette = [pal.replace('black', '(0, 0, 0)') for pal in palette]
#     palette = [pal.replace('white', '(255, 255, 255)') for pal in palette]
#     for y in range(img.size[1]):
#         #for x in range(img.size[0]/4):
#         x=0
#         while x <= 156:
#             try:
#                 if x < adjustedmedian:
#                     if str(pixelMap[x,y]) == palette[1]:
#                         currentbyte = currentbyte + 0x40
#                     if str(pixelMap[x,y]) == palette[2]:
#                         currentbyte = currentbyte + 0x80
#                     if str(pixelMap[x,y]) == palette[3]:
#                         currentbyte = currentbyte + 0xC0
#                     if str(pixelMap[x+1,y]) == palette[1]:
#                         currentbyte = currentbyte + 0x10
#                     if str(pixelMap[x+1,y]) == palette[2]:
#                         currentbyte = currentbyte + 0x20
#                     if str(pixelMap[x+1,y]) == palette[3]:
#                         currentbyte = currentbyte + 0x30
#                     if str(pixelMap[x+2,y]) == palette[1]:
#                         currentbyte = currentbyte + 0x04
#                     if str(pixelMap[x+2,y]) == palette[2]:
#                         currentbyte = currentbyte + 0x08
#                     if str(pixelMap[x+2,y]) == palette[3]:
#                         currentbyte = currentbyte + 0x0C
#                     if str(pixelMap[x+3,y]) == palette[1]:
#                         currentbyte = currentbyte + 0x01
#                     if str(pixelMap[x+3,y]) == palette[2]:
#                         currentbyte = currentbyte + 0x02
#                     if str(pixelMap[x+3,y]) == palette[3]:
#                         currentbyte = currentbyte + 0x03
#                 else:
#                     if str(pixelMap[x,y]) == palette[5]:
#                         currentbyte = currentbyte + 0x40
#                     if str(pixelMap[x,y]) == palette[6]:
#                         currentbyte = currentbyte + 0x80
#                     if str(pixelMap[x,y]) == palette[7]:
#                         currentbyte = currentbyte + 0xC0
#                     if str(pixelMap[x+1,y]) == palette[5]:
#                         currentbyte = currentbyte + 0x10
#                     if str(pixelMap[x+1,y]) == palette[6]:
#                         currentbyte = currentbyte + 0x20
#                     if str(pixelMap[x+1,y]) == palette[7]:
#                         currentbyte = currentbyte + 0x30
#                     if str(pixelMap[x+2,y]) == palette[5]:
#                         currentbyte = currentbyte + 0x04
#                     if str(pixelMap[x+2,y]) == palette[6]:
#                         currentbyte = currentbyte + 0x08
#                     if str(pixelMap[x+2,y]) == palette[7]:
#                         currentbyte = currentbyte + 0x0C
#                     if str(pixelMap[x+3,y]) == palette[5]:
#                         currentbyte = currentbyte + 0x01
#                     if str(pixelMap[x+3,y]) == palette[6]:
#                         currentbyte = currentbyte + 0x02
#                     if str(pixelMap[x+3,y]) == palette[7]:
#                         currentbyte = currentbyte + 0x03
#             except:
#                 pass
#             finally:
#                 x = x+4
#                 export.append(currentbyte)
#                 currentbyte = 0x00
#     z80 = "; Graphics generated by astroimg <3"
#     x = 0
#     while x <= 4030:
#         z80 = z80 + "\nDB $" + str(hex(export[x]))[2:] + ", $" + str(hex(export[x+1]))[2:] + ", $" + str(hex(export[x+2]))[2:] + ", $" + str(hex(export[x+3]))[2:] + ", $" + str(hex(export[x+4]))[2:] + ", $" + str(hex(export[x+5]))[2:] + ", $" + str(hex(export[x+6]))[2:] + ", $" + str(hex(export[x+7]))[2:] + ", $" + str(hex(export[x+8]))[2:] + ", $" + str(hex(export[x+9]))[2:]
#         x = x+10
#     while x > 4030 and x <= 4070:
#         z80 = z80 + "\n; DB $" + str(hex(export[x]))[2:] + ", $" + str(hex(export[x+1]))[2:] + ", $" + str(hex(export[x+2]))[2:] + ", $" + str(hex(export[x+3]))[2:] + ", $" + str(hex(export[x+4]))[2:] + ", $" + str(hex(export[x+5]))[2:] + ", $" + str(hex(export[x+6]))[2:] + ", $" + str(hex(export[x+7]))[2:] + ", $" + str(hex(export[x+8]))[2:] + ", $" + str(hex(export[x+9]))[2:]
#         x = x+10
#     newFile = open(graphicsFilename, "w")
#     newFile.write(z80)
#     newFile.close()


# def asmExporter():
#     global palette
#     palette = [pal.replace('(255, 0, 0)', '$6C') for pal in palette]
#     palette = [pal.replace('(255, 0, 255)', '$2F') for pal in palette]
#     palette = [pal.replace('(0, 0, 255)', '$EC') for pal in palette]
#     palette = [pal.replace('(0, 255, 255)', '$D5') for pal in palette]
#     palette = [pal.replace('(0, 255, 0)', '$AE') for pal in palette]
#     palette = [pal.replace('(255, 255, 0)', '$77') for pal in palette]
#     palette = [pal.replace('(255, 255, 255)', '$07') for pal in palette]
#     palette = [pal.replace('(0, 0, 0)', '$00') for pal in palette]
#     paletteLeftString = palette[3] + "," + palette[2] + "," + palette[1] + "," + palette[0]
#     paletteRightString = palette[7] + "," + palette[6] + "," + palette[5] + "," + palette[4]
#     asmTitle = "                                    ; " + filename
#     asmHeader = """                                 
#                                     ; Generated by astroimg
#                                     ; https://github.com/hxlnt/astrocade
#                                     ; Assemble with Zmac 1.3

#             INCLUDE "HVGLIB.H"      ; Include HVGLIB library
#             ORG     FIRSTC          ; Initialize at beginning of cartridge ROM area
#             DB      $55             ; ... with the code for a normal menued cartridge
#             DW      MENUST          ; Initialize menu
#             DW      PrgName         ; ... with string at PrgName
#             DW      PrgStart        ; ... such that selecting the program enters PrgStart
# """
#     asmPrgName = 'PrgName:    DB      "' + filename + '"            ; String to be displayed on menu'
#     asmPrgStart = """
#             DB      0               ; ... which must be followed by 0
# PrgStart:   DI                      ; Disable interrupts
#             SYSTEM  INTPC           ; Begin interpreter mode
#             DO      SETOUT          ; Set output ports
#             DB      100*2           ; ... with VBLANK line set to line 100
# """
#     asmColorBoundary = "            DB      " + str(adjustedmedian) + "/4            ; ... with color boundary set to this value/4"
#     asmGameLoop = """
#             DB      00001000b       ; ... with screen interrupts reenabled 
#             DO      COLSET          ; Set color palettes
#             DW      Palettes        ; ... with the values at Palettes
#             DO      MOVE            ; Display graphic
#             DW      NORMEM          ; ... starting at the beginning of screen RAM
#             DW      100*BYTEPL      ; ... copy 100 lines
#             DW      Graphics        ; ... from data at location Graphics
#             DO      ACTINT          ; Activate subtimer interrupts
#             EXIT                    ; Exit interpreter mode
# Loop:       JP      Loop            ; Play infinite loop
# """
#     asmLeftPalette = "Palettes:   DB      " + paletteLeftString + " ; Left color palette (11b, 10b, 01b, 00b)"
#     asmRightPalette = "\n            DB      " + paletteRightString + " ; Right color palette (11b, 10b, 01b, 00b)"
#     asmGraphics = "\nGraphics:                           ; Graphics"
#     asmGraphicsInclude = '\n            INCLUDE "' + graphicsFilename + '"\n'
#     asmAll = asmTitle + asmHeader + asmPrgName + asmPrgStart + asmColorBoundary + asmGameLoop + asmLeftPalette + asmRightPalette + asmGraphics + asmGraphicsInclude 
#     newFile2 = open(asmFilename, "w")
#     newFile2.write(asmAll)
#     newFile2.close()

# def imgPreview(newimg):
#     pixelMap = newimg.load()
#     for y in range(newimg.size[1]):
#         for x in range(newimg.size[0]):
#             if pixelMap[x,y] == (255, 0, 0):
#                 pixelMap[x,y] = (255, 85, 39)
#             if pixelMap[x,y] == (255, 0, 255):
#                 pixelMap[x,y] = (255, 153, 255)
#             if pixelMap[x,y] == (0, 0, 255):
#                 pixelMap[x,y] = (39, 168, 255)
#             if pixelMap[x,y] == (0, 255, 255):
#                 pixelMap[x,y] = (5, 255, 255)
#             if pixelMap[x,y] == (0, 255, 0):
#                 pixelMap[x,y] = (59, 255, 112)
#             if pixelMap[x,y] == (255, 255, 0):
#                 pixelMap[x,y] = (255, 252, 78)
#     newimg.show()

# try:
#     img = Image.open(sys.argv[1])
# except:
#     print("Please specify a valid filepath for an image to convert. Ex: python astroimg.py ../myphoto.jpg\nAdd --dither after the image path to dither image.")
#     sys.exit(0)
# img = img.resize([160,102],Image.ANTIALIAS)
# if len(sys.argv) > 2:
#     if sys.argv[2] == "--dither":
#         img = img.convert("P", dither=Image.FLOYDSTEINBERG)
#     else:
#         print("Unknown argument ignored. Use --dither to dither image.\n")
# #img.show()
# img = img.convert("RGB")
# filename = os.path.basename(sys.argv[1])
# filename = os.path.splitext(filename)[0].upper()
# if len(filename) > 8:
#     filename = filename[:7]
# print("Building Z80 ASM for " + filename + "...\n")
# graphicsFilename = filename + ".gfx"
# asmFilename = filename + ".asm"
# eightColorDownsample(img)
# colorBoundaryFinder(img)
# colorCounter(imgleft)
# leftcolors = {"red":redcounter, "yellow":yellowcounter, "green":greencounter, "cyan":cyancounter, "blue":bluecounter, "magenta":magentacounter, "black":blackcounter, "white":whitecounter}
# leftcolors = sorted(iter(leftcolors.items()), key=lambda k_v: (k_v[1],k_v[0]))
# colors_to_roll = [leftcolors[0][0], leftcolors[1][0], leftcolors[2][0], leftcolors[3][0]]
# colors_to_keep = [leftcolors[4][0], leftcolors[5][0], leftcolors[6][0], leftcolors[7][0]]
# colorRoller(colors_to_keep, colors_to_roll, imgleft)
# colorCounter(imgright)
# rightcolors = {"red":redcounter, "yellow":yellowcounter, "green":greencounter, "cyan":cyancounter, "blue":bluecounter, "magenta":magentacounter, "black":blackcounter, "white":whitecounter}
# rightcolors = sorted(iter(rightcolors.items()), key=lambda k_v: (k_v[1],k_v[0]))
# colors_to_roll = [rightcolors[0][0], rightcolors[1][0], rightcolors[2][0], rightcolors[3][0]]
# colors_to_keep = [rightcolors[4][0], rightcolors[5][0], rightcolors[6][0], rightcolors[7][0]]
# colorRoller(colors_to_keep, colors_to_roll, imgright)
# newimg = Image.new("RGB", (160,102))
# newimg.paste(imgleft, (0,0))
# newimg.paste(imgright, (adjustedmedian, 0))
# z80Exporter(newimg)
# asmExporter()
# imgPreview(newimg)
# print("Successfully saved " + graphicsFilename + " and " + asmFilename)
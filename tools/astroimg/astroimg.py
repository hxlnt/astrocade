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
        r, g, b = self.r / 255.0, self.g / 255.0, self.b / 255.0
        maxrgb = max(r, g, b)
        minrgb = min(r, g, b)
        df = maxrgb - minrgb
        if maxrgb == minrgb:
            h = 0
        elif maxrgb == r:
            h = (60 * ((g - b) / df) + 360) % 360
        elif maxrgb == g:
            h = (60 * ((b - r) / df) + 120) % 360
        elif maxrgb == b:
            h = (60 * ((r - g) / df) + 240) % 360
        if maxrgb == 0:
            s = 0
        else:
            s = df/maxrgb
        v = maxrgb
        return (round(h, 3), round(s, 3), round(v, 3))

    def toHex(self):
        r = self.toEightColorRGB()[0]
        g = self.toEightColorRGB()[1]
        b = self.toEightColorRGB()[2]
        if r == 255 and g == 255 and b == 255:
            return 0x07
        elif r == 255 and g == 255 and b == 0:
            return 0x77
        elif r == 255 and g == 0 and b == 255:
            return 0x2F
        elif r == 255 and g == 0 and b == 0:
            return 0x6C
        elif r == 0 and g == 255 and b == 255:
            return 0xD5
        elif r == 0 and g == 255 and b == 0:
            return 0xAE
        elif r == 0 and g == 0 and b == 255:
            return 0xEC
        else:
            return 0x00

    def toAstroRGB(self):
        r = self.toEightColorRGB()[0]
        g = self.toEightColorRGB()[1]
        b = self.toEightColorRGB()[2]
        if r == 0 and g == 255 and b == 255:
            return (5, 255, 255)
        elif r == 0 and g == 0 and b == 255:
            return (39, 168, 255)
        elif r == 255 and g == 0 and b == 255:
            return (255, 152, 255)
        elif r == 255 and g == 0 and b == 0:
            return 255, 85, 39
        elif r == 255 and g == 255 and b == 0:
            return 255, 252, 78
        else:
            return 59, 255, 112

    def toEightColorRGB(self):
        hsv = self.toHSV()
        if hsv[1] >= .15 and hsv[2] >= .4:
            if (hsv[0] < 35 or hsv[0] > 340):
                return (255, 0 , 0)
            elif (hsv[0] >= 35 and hsv[0] < 70):
                return (255, 255, 0)
            elif (hsv[0] >= 70 and hsv[0] < 155):
                return (0, 255, 0)
            elif (hsv[0] >= 155 and hsv[0] < 190):
                return (0, 255, 255)
            elif (hsv[0] >= 190 and hsv[0] < 250):
                return (0, 0, 255)
            elif (hsv[0] >= 255 and hsv[0] <= 340):
                return (255, 0, 255)
        elif hsv[1] < .15 and hsv[2] >= .4:
            return (255, 255, 255)
        else:
            return (0, 0, 0)

class Img:
    
    def __init__(self, imgpath, ditherWanted=False):
        self.imgpath = imgpath
        if ditherWanted == True:
            self.img = Image.open(imgpath).resize([160,102],Image.ANTIALIAS).convert("P", dither=Image.FLOYDSTEINBERG).convert("RGB")
        else:
            self.img = Image.open(imgpath).resize([160,102],Image.ANTIALIAS).convert("RGB")
        self.pixelMap = self.img.load()
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        self.colorcount = {}
        self.colorboundary = 0
        self.redxpos = set()
        self.yellowxpos = set()
        self.greenxpos = set()
        self.cyanxpos = set()
        self.bluexpos = set()
        self.magentaxpos = set()
        self.blackxpos = set()
        self.whitexpos = set()
    
    def getColorCounts(self):
        red = yellow = green = cyan = blue = magenta = black = white = 0
        for y in range(self.height):
            for x in range(self.width):
                thiscolor = Pixel(self.pixelMap[x,y][0], self.pixelMap[x,y][1], self.pixelMap[x,y][2]).toEightColorRGB()
                if thiscolor == (255,0,0):
                    red += 1
                    self.redxpos.add(x)
                elif thiscolor == (255,255,0):
                    yellow += 1
                    self.yellowxpos.add(x)
                elif thiscolor == (0,255,0):
                    green+= 1
                    self.greenxpos.add(x)
                elif thiscolor == (0,255,255):
                    cyan += 1
                    self.cyanxpos.add(x)
                elif thiscolor == (0,0,255):
                    blue += 1
                    self.bluexpos.add(x)
                elif thiscolor == (255,0,255):
                    magenta += 1
                    self.magentaxpos.add(x)
                elif thiscolor == (0,0,0):
                    black += 1
                    self.blackxpos.add(x)
                else:
                    white += 1
                    self.whitexpos.add(x)
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

    def getColorBoundary(self):
        minmax = []
        if len(self.redxpos) > 0 and self.colorcount['red'] > 160:
            minmax.append(min(self.redxpos))
            minmax.append(max(self.redxpos))
        if len(self.magentaxpos) > 0 and self.colorcount['magenta'] > 160:
            minmax.append(min(self.magentaxpos))
            minmax.append(max(self.magentaxpos))
        if len(self.bluexpos) > 0 and self.colorcount['blue'] > 160:
            minmax.append(min(self.bluexpos))
            minmax.append(max(self.bluexpos))
        if len(self.cyanxpos) > 0 and self.colorcount['cyan'] > 160:
            minmax.append(min(self.cyanxpos))
            minmax.append(max(self.cyanxpos))
        if len(self.greenxpos) > 0 and self.colorcount['green'] > 160:
            minmax.append(min(self.greenxpos))
            minmax.append(max(self.greenxpos))
        if len(self.yellowxpos) > 0 and self.colorcount['yellow'] > 160:
            minmax.append(min(self.yellowxpos))
            minmax.append(max(self.yellowxpos))
        if len(self.blackxpos) > 0 and self.colorcount['black'] > 160:
            minmax.append(min(self.blackxpos))
            minmax.append(max(self.blackxpos))
        if len(self.whitexpos) > 0 and self.colorcount['white'] > 160:
            minmax.append(min(self.whitexpos))
            minmax.append(max(self.whitexpos))
        median = round(statistics.median(minmax))
        self.colorboundary = int(math.floor(median - (median % 4)))

   def getColorSplits(self):


        # leftcolors = {"red":redcounter, "yellow":yellowcounter, "green":greencounter, "cyan":cyancounter, "blue":bluecounter, "magenta":magentacounter, "black":blackcounter, "white":whitecounter}
# leftcolors = sorted(iter(leftcolors.items()), key=lambda k_v: (k_v[1],k_v[0]))
# colors_to_roll = [leftcolors[0][0], leftcolors[1][0], leftcolors[2][0], leftcolors[3][0]]
# colors_to_keep = [leftcolors[4][0], leftcolors[5][0], leftcolors[6][0], leftcolors[7][0]]



#################################################################

# palette = blackxpos = bluexpos = cyanxpos = greenxpos = magentaxpos = redxpos = whitexpos = yellowxpos = {} 
# palette = set()
# imgleft = None
# imgright = None


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
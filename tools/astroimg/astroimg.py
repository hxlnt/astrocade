from PIL import Image

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

img = Image.open("../../etc/paint900.jpeg")
img.thumbnail((160,102))
pixelMap = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        hsvpixel = rgb2hsv(pixelMap[x,y][0], pixelMap[x,y][1], pixelMap[x,y][2])
        if (hsvpixel[0] < 35 or hsvpixel[0] > 340):
            pixelMap[x,y] = (255,0,0)
        elif (hsvpixel[0] >= 35 and hsvpixel[0] < 70):
            pixelMap[x,y] = (255,255,0)
        elif (hsvpixel[0] >= 70 and hsvpixel[0] < 155):
            pixelMap[x,y] = (0,255,0)
        elif (hsvpixel[0] >= 155 and hsvpixel[0] < 190):
            pixelMap[x,y] = (0,255,255)
        elif (hsvpixel[0] >= 190 and hsvpixel[0] < 250):
            pixelMap[x,y] = (0,0,255)
        elif (hsvpixel[0] >= 255 and hsvpixel[0] <= 340):
            pixelMap[x,y] = (255,0,255)
        if hsvpixel[1] < .15:
            pixelMap[x,y] = (255,255,255)
        if hsvpixel[2] < .4:
            pixelMap[x,y] = (0,0,0)

img.show()
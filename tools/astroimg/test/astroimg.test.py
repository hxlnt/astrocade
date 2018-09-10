# Bring your packages onto the path
import sys, os
sys.path.append(os.path.abspath('..'))
import astroimg
import unittest

class TestPixelColor(unittest.TestCase):

    def test_rgb2hsv(self):
        mockcolor = astroimg.PixelColor(252, 1, 0)
        result = mockcolor.toHSV()
        self.assertEqual(result, (0.238, 1.000, 0.988))
    
    def test_rgb2hex(self):
        mockcolor = astroimg.PixelColor(1, 5, 250)
        result = mockcolor.toHex()
        self.assertEqual(result, 0xEC)

    def test_rgb2astrorgb(self):
        mockcolor = astroimg.PixelColor(235, 250, 1)
        result = mockcolor.toAstroRGB()
        self.assertEqual(result, (255, 252, 78))
    
    def test_rgb2eightcolor(self):
        mockcolor = astroimg.PixelColor(245, 252, 5)
        result = mockcolor.toEightColorRGB()
        self.assertEqual(result, (255, 255, 0))


if __name__ == '__main__':
    unittest.main()
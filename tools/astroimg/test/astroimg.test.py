# Bring your packages onto the path
import sys, os
sys.path.append(os.path.abspath('..'))
import astroimg
import unittest

class TestPixel(unittest.TestCase):

    # def test_rgb2hsv(self):
    #     mockcolor = astroimg.Pixel(252, 1, 0)
    #     result = mockcolor._toHSV()
    #     self.assertEqual(result, (0.238, 1.000, 0.988))
    
    def test_rgb2hex(self):
        mockcolor = astroimg.Pixel(1, 5, 250)
        result = mockcolor.toHex()
        self.assertEqual(result, 0xEC)

    def test_rgb2astrorgb(self):
        mockcolor = astroimg.Pixel(235, 250, 1)
        result = mockcolor.toAstroRGB()
        self.assertEqual(result, (255, 252, 78))
    
    def test_rgb2eightcolor(self):
        mockcolor = astroimg.Pixel(245, 252, 5)
        result = mockcolor._toEightColorRGB()
        self.assertEqual(result, (255, 255, 0))

class TestImg(unittest.TestCase):

    def test_getcolorcountsandboundary(self):
        mockimage = astroimg.Img('test.png')
        mockimage.getColorCounts()
        self.assertEqual(mockimage.colorcount['white'], 4 * 102)
        mockimage.getColorBoundary()
        self.assertEqual(mockimage.colorboundary, 16)
        mocknewimage = mockimage.splitAndRecombineImage()
        self.assertEqual(mocknewimage.width, 160)
        mocknewimage.show()
        
if __name__ == '__main__':
    unittest.main()
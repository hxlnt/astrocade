# Bring your packages onto the path
import sys, os
sys.path.append(os.path.abspath('..'))
import astroimg
import unittest

class TestPixelColor(unittest.TestCase):
    def test_rgb2hsv(self):
        mockcolor = astroimg.PixelColor(255, 0, 0)
        result = mockcolor.toHSV()
        self.assertEqual(result, (0, 1, 1))

if __name__ == '__main__':
    unittest.main()
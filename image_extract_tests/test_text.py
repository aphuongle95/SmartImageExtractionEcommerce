import unittest

from image_extract.text import TextUtils

class TestTextUtils(unittest.TestCase):
    def test_is_similar(self):
        a = "lazy	https://www.gadgets360.com/static/mobile/images/spacer.png"
        b = "lazy	https://www.gadgets360.com/static/mobile/images/spacer.png"
        res = TextUtils().is_similar(a, b)
        self.assertTrue(res)
        
if __name__ == "__main__":
    unittest.main()
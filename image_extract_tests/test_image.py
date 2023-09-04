import unittest

from image_extract.image import ImageUtils

class TestImageUtils(unittest.TestCase):
    def test_get_size(self):
        res = ImageUtils().get_size("https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/f3ae4f5c-d6cf-4b82-8e41-03842731bd22")
        res = ImageUtils().get_size("https://thumbs.static-thomann.de/thumb//thumb80x80/pics/prod/425179.jpg")
        
        self.assertEqual(res, (80, 80))
    
    def test_is_small(self):
        res = ImageUtils().is_small("https://photos-eu.bazaarvoice.com/photo/2/cGhvdG86YXR0cmlidXRpb25sb2dvMg/f3ae4f5c-d6cf-4b82-8e41-03842731bd22")
        self.assertTrue(res)
        res = ImageUtils().is_small("https://thumbs.static-thomann.de/thumb//thumb80x80/pics/prod/425179.jpg")
        self.assertFalse(res)
        res = ImageUtils().is_small("https://assets.mmsrg.com/isr/166325/c1/-/ASSET_MMS_89403710?x=70&format=png&papp=quant(quality=85)&sp=yes&strip=yes&trim=true")
        self.assertTrue(res)
        res = ImageUtils().is_small("https://rukminim2.flixcart.com/image/128/128/xif0q/toothpaste/6/e/l/-original-imagr7v56qqyajf2.jpeg?q=70")
        self.assertTrue(res)
        
        
        
if __name__ == "__main__":
    unittest.main()
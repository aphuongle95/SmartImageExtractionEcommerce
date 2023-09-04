import unittest

from image_extract.selenium import SeleniumUtils

site = "https://theartment.com/products/space-odyssey-the-astronaut-galaxy-light-projector"

class TestSeleniumUtils(unittest.TestCase):
    # def test__separate_number_unit(self):
        
    # def test_get_all_texts_font_sizes(self):
    #     sele_utils = SeleniumUtils(site)
    #     res = sele_utils.get_all_texts_font_sizes()
    #     print(res)
        
    def test_extract_big_text(self):
        sele_utils = SeleniumUtils(site)
        res = sele_utils.extract_big_text()
        print(res)
        sele_utils.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
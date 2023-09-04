import unittest

from pydantic import HttpUrl

from image_extract.prompt import ProductImage

from image_extract.file import FileUtils
from image_extract.main import _filter_product_images

PROMPT = "image_extract_tests/files/prompt3.txt"
LINKS = ["https://checkbox.live/uploads/images/product/multi-images/image-1685161725618681653.jpeg"]

class TestMain(unittest.TestCase):
    def test__filter_product_images(self):
        table = FileUtils.read_str_fr_file(PROMPT)
        links = LINKS
        res = _filter_product_images(table, links)
        print(res)
        expected_result = [ProductImage(class_names='slider_image', link='https://checkbox.live/uploads/images/product/multi-images/image-1685161725618681653.jpeg')]
        self.assertEqual(res, expected_result)
    
        
if __name__ == "__main__":
    unittest.main()
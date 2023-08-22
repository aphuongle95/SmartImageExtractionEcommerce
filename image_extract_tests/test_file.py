import unittest

from bs4 import BeautifulSoup
from image_extract.file import FileUtils

class TestFileUtils(unittest.TestCase):
    def test_get_all_links(self):
        res = FileUtils.get_all_links()
        print(res)

    def test_read_html(self) -> str:
        res = FileUtils("jumia").read_html()
        print(res)
        self.assertEqual(type(res), str)

if __name__ == "__main__":
    unittest.main()
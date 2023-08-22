from typing import List
import unittest

import pandas as pd
from bs4 import BeautifulSoup

from image_extract.file import FileUtils
from image_extract.soup import SoupUtils
from image_extract.prompt import ChatGPTUtils, ProductImage
import asyncio
import pytest

INIT_PROMPT = "image_extract_tests/files/prompt1.txt"
FINAL_PROMPT = "image_extract_tests/files/prompt2.txt"
GPT_OUTPUT = "image_extract_tests/files/out.txt"

class TestChatGPTUtils(unittest.TestCase):
        
    def test_prepare_prompt(self):
        
        inp = FileUtils.read_str_fr_file(INIT_PROMPT)
        res: str = ChatGPTUtils().prepare_prompt(inp)
        print(res)
        
        FileUtils.write_str_to_file(res, FINAL_PROMPT)
        self.assertTrue(len(res) < 500)
        
class TestChatGPTUtilsAsync(unittest.IsolatedAsyncioTestCase):        
    
    async def test_extract_product_images(self):
        table: str = FileUtils.read_str_fr_file(FINAL_PROMPT)
        images: List(ProductImage) = await ChatGPTUtils().extract_product_images(table)
        df = pd.DataFrame.from_dict([image.dict() for image in images])
        df.to_csv(GPT_OUTPUT)

        # self.assertEqual(res, expected_result)
        
if __name__ == "__main__":
    unittest.main()
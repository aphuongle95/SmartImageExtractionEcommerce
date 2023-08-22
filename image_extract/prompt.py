from ast import List
import json
import re

from pydantic import BaseModel, HttpUrl
from content.src.ml_components.utils.openai_caller import OpenAICaller
from bs4 import BeautifulSoup
import pandas as pd

from image_extract.text import TextUtils

class ProductImage(BaseModel):
    class_names: str
    link: HttpUrl
    
class ChatGPTUtils():
    INSTRUCTION = """Your task is to find the products' images from a table.
    This table is a sequence of texts and images appear in the html page.
    We keep only the class names and the texts / images.
    You should try to extract and return only the class names of the products' images.
    We don't want to extract images of similar products or logos. 
    Hint: in ecommerce website, the product's images' links often appear first in the page and have same class's name.
    Reject an image if it seems to be another product, based on the image's link or has different class name.
    Provide the output images' class name(s) as an array of string.
    For example:
    a-dynamic-image | https://m.media-amazon.com/images/I/61j3SEUjMJL._AC_SX679_.jpg
    Return a-dynamic-image
    """
    INSTRUCTION = """filter this information to keep only product's images. 
    ignore logos and banners. reject images under related or similar products.
    provide the product's image links as a valid JSON object with the following schema: {"images": ["", "", ...]}
    """
    async def _call_gpt(self, prompt: str, temp=0.5, max_tokens=200):
        parameters = dict(
            max_tokens=max_tokens,
            temperature=temp,
            # frequency_penalty=1.125,
            n=1,
        )
        
        candidates = await OpenAICaller.chat_completion(
            model="gpt-3.5-turbo",
            messages=[prompt],
            settings=parameters,
        )
        return candidates[0]

    async def extract_product_images(self, table: str) -> List(ProductImage):
        prompt = self.INSTRUCTION + table
        print(prompt)
        print(len(prompt))
        out: str = await self._call_gpt(self.INSTRUCTION + table)
        print(out)
        return self._get_images_from_output(out)
    
    def _get_images_from_output(self, out:str) -> List(ProductImage):
        images = []
        try:
            images = json.loads(out)["images"]
        except:
            URL_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            images = re.findall(URL_REGEX, out)
        # TODO get class from file
        return [ProductImage(class_names="",link= link) for link in images]
        
    def prepare_prompt(self, inp: str) -> str:
        """Prepare shorter and compressed prompt for chatgpt"""
        texts = inp.split("\n")
        cleaned_texts = [texts[0]]
        for i in range(1, len(texts)):
            if TextUtils().is_similar(texts[i], texts[i-1]):
                continue
            else:
                cleaned_texts.append(texts[i])
        out = "\n".join(cleaned_texts)
        return out
        
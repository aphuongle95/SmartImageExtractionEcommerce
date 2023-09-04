from ast import List
import json
import re

from pydantic import BaseModel, HttpUrl
from content.src.ml_components.utils.openai_caller import OpenAICaller
from bs4 import BeautifulSoup
import pandas as pd
from image_extract.image import ImageUtils

from image_extract.text import TextUtils

class ProductImage(BaseModel):
    class_names: str
    link: HttpUrl
    
class ChatGPTUtils():
    
    INSTRUCTION = """filter this information to keep only product's images. 
ignore logos and banners. 
don't return images under related or similar products.
reject cookie images.
also, the product's images often appear first in the list.
provide the product's image links as a valid JSON object with the following schema: {"images": ["", ...]}
you should provide at least one image but not more than 3 images.
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
        out: str = await self._call_gpt(prompt)
        print(out)
        return self._get_images_from_output(out)
    
    def _get_images_from_output(self, out:str) -> List(str):
        # Use prompt to find class name
        
        images = []
        try:
            images = json.loads(out)["images"]
        except:
            URL_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            images = re.findall(URL_REGEX, out)
        return images
        
    def prepare_prompt(self, inp: str) -> str:
        """Prepare shorter and compressed prompt for chatgpt"""
        texts = inp.split("\n")
        cleaned_texts = [texts[0]]
        
        for i in range(1, len(texts)):
            # reject small images
            cls_names, link = texts[i].split("\t")
            if link.startswith("http") and ImageUtils().is_small(link):
                continue
            if TextUtils().is_similar(texts[i], texts[i-1]):
                continue
            else:
                cleaned_texts.append(texts[i])
        out = "\n".join(cleaned_texts)
        return out
        

from dataclasses import asdict
from typing import List, Tuple
from anyio import Path
from matplotlib import pyplot as plt
import pandas as pd
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import re

SAVE_TO_FILE = "image_extract_files/text_font_size.csv"
SAVE_TO_FILE_FILTERED = "image_extract_files/text_font_size_filtered.csv"

def _separate_number_unit(txt: str) -> tuple:
    p = re.compile('(\d+)\s*(\w+)')
    number, unit = p.match(txt).groups()
    try:
        number = float(number)
    except:
        raise ValueError("Please input text like 20GB, 17ft, 12.8px")
    return(number, unit)

class TextCSS(BaseModel):

    text: str 
    font_size: float 
    font_size_unit: str
    
class SeleniumUtils():
    THRESHOLD = .8
    def __init__(self, link):
        
        # extract text
        options = webdriver.ChromeOptions();
        options.add_argument('headless');
        options.add_argument('window-size=1200x600')
        driver = webdriver.Chrome(options=options)
        driver.get(link)
        self.driver = driver

    def _get_all_texts_font_sizes(self):
        texts: List(TextCSS) = []
        element = self.driver.find_element(By.TAG_NAME, 'body')
        text = element.text
        for t in text.split("\n"):
            try:
                element: WebElement = self.driver.find_element(By.XPATH, f'//*[text() = "{t}"]')
                print(element)
                print(element.tag_name)
                text = element.text
                print(text)
                font_size = element.value_of_css_property("font-size")
                print(font_size)
                size, unit = _separate_number_unit(font_size)
                texts.append(TextCSS(text=text, font_size=size, font_size_unit=unit))
            except:
                continue
        df = pd.json_normalize(obj.dict() for obj in texts)
        df.to_csv(Path(SAVE_TO_FILE), sep="\t")
        print(df)
        return df
        
    def extract_big_text(self) -> List[str]:
        df = self._get_all_texts_font_sizes()
        df = pd.read_csv(SAVE_TO_FILE, sep="\t")
        df = df.drop(columns=["font_size_unit"])
        df = df[df.font_size > df.font_size.quantile(self.THRESHOLD)]
        print(df)
        df.to_csv(Path(SAVE_TO_FILE_FILTERED), sep="\t")
        return df["text"].to_list()
        
        # df["font_size"].plot(kind='kde')
        # plt.show()
"""
Extract product's image from site
"""

__author__ = "Anh Phuong Le"
__version__ = "0.0.1"

import argparse
from ast import List
import asyncio
import pandas as pd

from bs4 import BeautifulSoup

from image_extract.file import FileUtils
from image_extract.prompt import ChatGPTUtils, ProductImage
from image_extract.soup import SoupUtils

async def extract_product_image(name, link):
    file_utils = FileUtils(name, link)
    html: str = file_utils.read_html()
    soup1: BeautifulSoup = SoupUtils().get_soup(html)
    soup2: BeautifulSoup = SoupUtils().clean(soup1)
    table1: str = SoupUtils().construct_table(soup2)
    table2: str = ChatGPTUtils().prepare_prompt(table1)
    images: List(ProductImage) = await ChatGPTUtils().extract_product_images(table2)
    file_utils.write_str_to_file(soup1.prettify(), file_utils.html_file)
    file_utils.write_str_to_file(soup2.prettify(), file_utils.html_cleaned_file)
    file_utils.write_str_to_file(table1, file_utils.table_file)
    file_utils.write_str_to_file(table2, file_utils.prompt_file)
    df = pd.DataFrame.from_dict([image.dict() for image in images])
    df.to_csv(file_utils.output_file)
    

async def main(args):

    print("Running image extraction...")
    print(args)
    if args.all:
        names_links: dict = FileUtils.get_all_links()
        for name, link in names_links.enumerate():
            await extract_product_image(name, link)
    else:
        name = args.name
        link = FileUtils.get_all_links()[name]
        await extract_product_image(name, link)
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--all", action="store_true", default=False)
    parser.add_argument("-n", "--name", action="store", dest="name")
    parser.add_argument("-l", "--link", action="store", dest="name")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    
if __name__=='__main__':
    asyncio.run(main(args))
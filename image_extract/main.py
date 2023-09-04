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
from image_extract.image import ImageUtils
from image_extract.prompt import ChatGPTUtils, ProductImage
from image_extract.soup import SoupUtils

def _filter_product_images(table: str, links: List(str)) -> List(ProductImage):
    """From table get the correct link and class names
    Also, once a class is selected, all images related to this class is selected."""
    original_images: List(ProductImage) = []
    filter_images: List(ProductImage) = []
    class_names_to_original_images: dict = {}
    lines = table.split("\n")
    
    # create a dictionary of classnames and list of images
    for x in lines:
        try:
            class_names, link = x.split("\t")
            
            product_image = ProductImage(class_names=class_names, link=link)
            original_images.append(product_image)
            if class_names == "":
                continue
            if class_names not in class_names_to_original_images:
                class_names_to_original_images[class_names] = [product_image]
            else:
                class_names_to_original_images[class_names].append(product_image)
        except:
            continue
    
    # take all images that have the same class names 
    for link in links:
        for line in lines:
            if line.__contains__(link):
                class_names, real_link = line.split("\t")
                if class_names.strip() != "":
                    filter_images += class_names_to_original_images[class_names]
                else:
                    filter_images.append(ProductImage(class_names="", link=real_link))
    return filter_images
                

async def extract_product_image(name, link):
    file_utils = FileUtils(name, link)
    html: str = file_utils.read_html()
    soup1: BeautifulSoup = SoupUtils().get_soup(html)
    file_utils.write_str_to_file(soup1.prettify(), file_utils.html_file)
    soup2: BeautifulSoup = SoupUtils().clean(soup1)
    file_utils.write_str_to_file(soup2.prettify(), file_utils.html_cleaned_file)
    table1: str = SoupUtils().construct_table(soup2)
    file_utils.write_str_to_file(table1, file_utils.table_file)
    table2: str = ChatGPTUtils().prepare_prompt(table1)
    file_utils.write_str_to_file(table2, file_utils.prompt_file)
    if len(table2) < 10: 
        return
    images: List[str] = await ChatGPTUtils().extract_product_images(table2)
    product_images: List(ProductImage) = _filter_product_images(table1, images)
    df = pd.DataFrame.from_dict([image.dict() for image in product_images])
    df.to_csv(file_utils.output_file)
    

async def main(args):

    print("Running image extraction...")
    print(args)
    if args.all:
        names_links: dict = FileUtils.get_all_links()
        for name, link in names_links.items():
            print(f"Start processing {name}...")
            await extract_product_image(name, link)
            print(f"Processing {name} done")
    else:
        name = args.name
        # name = "flipkart"
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
from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd

from image_extract.soup import SoupUtils

class FileUtils():
    FOLDER: Path = Path("image_extract_files")
    ALL_LINKS = "links.csv"
    CLEANED_HTML_FILE_POSTFIX = "_clean.html"
    HTML_FILE_POSTFIX = ".html"
    TREE_FILE_POSTFIX = "_tree.txt"
    COMPRESS_FILE_POSTFIX = "_compress.txt"
    TABLE_FILE_POSTFIX = "_table.txt"
    PROMPT_POSTFIX = "_prompt.txt"
    OUTPUT_POSTFIX = "_out.txt"
    
    def __init__(self, name, link="") -> None:
        self.name = name
        if link == "":
            link = FileUtils.get_all_links()[name]
        self.link = link
        self.html_file = self.FOLDER / (name + self.HTML_FILE_POSTFIX)
        self.html_cleaned_file = self.FOLDER / (name + self.CLEANED_HTML_FILE_POSTFIX)
        self.tree_file = self.FOLDER / (name + self.TREE_FILE_POSTFIX)
        self.compressed_file = self.FOLDER / (name + self.COMPRESS_FILE_POSTFIX)
        self.table_file = self.FOLDER / (name + self.TABLE_FILE_POSTFIX)
        self.prompt_file = self.FOLDER / (name + self.PROMPT_POSTFIX)
        self.output_file = self.FOLDER / (name + self.OUTPUT_POSTFIX)
    
    @classmethod
    def get_all_links(cls) -> dict:
        df: pd.DataFrame = pd.read_csv(FileUtils.FOLDER / FileUtils.ALL_LINKS, sep=" ")
        return dict(zip(df.name, df.link))

    def read_html(self) -> str:
        """Read the HTML from link, if file exists, read from file"""
        name = self.name
        link = self.link
        file_path = self.html_file
        if file_path.exists():
            with open(file_path.absolute(), "r") as file:
                html_content = file.read()
                return html_content
        else:
            import requests
            try:
                headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
                response = requests.get(link, headers=headers)
                if response.status_code == 200:
                    html_content = response.text
                    return html_content
                else:
                    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")

    @classmethod
    def write_str_to_file(cls, txt: str, file: Path):
        """Write str to file"""
        with open(str(file), "w") as f:
            f.write(txt)
         
    @classmethod  
    def read_str_fr_file(cls, file: Path) -> str:
        """Read str from file"""
        with open(str(file), "r") as f:
            return f.read()

    
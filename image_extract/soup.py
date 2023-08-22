from ast import List
from bs4 import BeautifulSoup


class SoupUtils():
    IMG_TAG = "img"
    TO_CLEAN_TAGS = ["script", "noscript", "head", "header", "footer"]
    HEADER_TAGS = ["h1", "h2", "h3"]
    CLASS_ATTR = "class"
    SRC_ATTR = "src"
    
    def get_soup(self, html_content: str):
        """Get soup from html content"""
        html = BeautifulSoup(html_content, "html.parser")
        return html
    
    def _count_imgs(self, soup: BeautifulSoup):
        """Count number of images in soup"""
        count = 0
        if soup.name == self.IMG_TAG:
            count += 1
        count += len(soup.find_all(self.IMG_TAG))
        return count

    def _is_include(self, element: BeautifulSoup):
        """Check if we should include a soup element.
        Condition: the element contains some image or text"""
        return self._count_imgs(element) > 0 or element.text.strip() != ""
    
    def _get_class(self, soup:BeautifulSoup):
        """Get class of the soup and hash it"""
        try:
            return " ".join(soup["class"])
        except:
            return ""
    
    def _get_text(self, soup:BeautifulSoup):
        texts = soup.find_all(text=True, recursive=False)
        texts = [t.strip() for t in texts]
        texts = [t for t in texts if t]
        text = ", ".join(texts)
        return text
    
    def _clean_by_tag(self, html: BeautifulSoup, tag_name: str):
        for element in html(tag_name):
            element.decompose()
        return html

    def clean(self, soup: BeautifulSoup, tags_to_clean: List(str) = TO_CLEAN_TAGS) -> BeautifulSoup:
        for tag in tags_to_clean:
            soup = self._clean_by_tag(soup, tag)
        return soup
    
    def construct_table(self, soup: BeautifulSoup) -> str:
        """Construct a table from soup
        This table contains only important information"""
        if not self._is_include(soup):
            return ""
        else:
            return_str = ""
            # image source
            if soup.name == self.IMG_TAG and soup.has_attr(self.SRC_ATTR):
                if soup[self.SRC_ATTR].startswith("data:image/"): # skip small images (logos, banners, etc.)
                    return ""
                return_str += f"\n{self._get_class(soup)}\t{soup[self.SRC_ATTR]}" 
            # or text:
            text = self._get_text(soup)
            if text != "" and len(text) < 100 and soup.name in self.HEADER_TAGS: # taking non-empty, not-too-long text with header tag
                return_str += f"\n{self._get_class(soup)}\t{text}" 
                
            children =  soup.findChildren(recursive=False)
            for element in children:
                return_str += self.construct_table(element)
        return return_str

        
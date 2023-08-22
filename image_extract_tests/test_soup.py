import random
import unittest
from bs4 import BeautifulSoup

from image_extract.soup import SoupUtils

HTML_STR = """
    <div>Hello
        <script>abc</script>
        <noscript>def</noscript>
      <span>
       ABOUT JUMIA
      </span>
      <ul>
       <li>
        <h1 class="h1" href="https://www.jumia.com.ng/about_us/">
         About us
        </h1>
       </li>
       <li>
        <h2 class="h2" href="https://www.jumia.com.ng/careers/">
         Jumia careers
        </h2>
        <h3>
        </h3>
       </li>
       <img class="image" alt="" class="-fw -fh" data-src="https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/1.jpg?5797" src="https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/1.jpg?5797"/>
      </ul>
     </div>
     <div/>"""

HTML_STR_CLEANED = """
    <div>Hello
      <span>
       ABOUT JUMIA
      </span>
      <ul>
       <li>
        <h1 class="h1" href="https://www.jumia.com.ng/about_us/">
         About us
        </h1>
       </li>
       <li>
        <h2 class="h2" href="https://www.jumia.com.ng/careers/">
         Jumia careers
        </h2>
        <h3>
        </h3>
       </li>
       <img class="image" alt="" class="-fw -fh" data-src="https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/1.jpg?5797" src="https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/1.jpg?5797"/>
      </ul>
     </div>
     <div/>"""
TABLE = """h1 | About us
h2 | Jumia careers
-fw -fh | https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/1.jpg?5797"""

HTML_STR_2 = """<div class="_pdmimg __arModalBtn _flx" data-ajax-type="pdp-gallery">
           <img alt="Samsung Galaxy Z Fold 5" height="180" src="https://i.gadgets360cdn.com/products/large/samsung-galaxy-z-fold-5-671x800-1690370876.jpg?downsize=*:180" title="Samsung Galaxy Z Fold 5" width="180">
           </img>
          </div>"""

TABLE_2 = " | https://i.gadgets360cdn.com/products/large/samsung-galaxy-z-fold-5-671x800-1690370876.jpg?downsize=*:180"

class TestSoupUtils(unittest.TestCase):
    def test_get_soup(self):
        res = SoupUtils().get_soup("<div>test</div>")
        print(res)
        self.assertEqual(res.__class__, BeautifulSoup)
    
    def test_clean(self):
        soup = SoupUtils().get_soup(HTML_STR)
        res = SoupUtils().clean(soup)
        self.assertIsNone(res.find(random.choice(SoupUtils.TO_CLEAN_TAGS)))
        
    def test_construct_table(self):
        soup = SoupUtils().get_soup(HTML_STR_CLEANED)
        res = table = SoupUtils().construct_table(soup)
        print(res)
        self.assertEqual(table.strip(), TABLE.strip())
    
    def test_construct_table_keep_image(self):
        soup = SoupUtils().get_soup(HTML_STR_2)
        res = SoupUtils().construct_table(soup)
        print(res)
        self.assertEqual(res.strip(), TABLE_2.strip())
        
        
if __name__ == "__main__":
    unittest.main()
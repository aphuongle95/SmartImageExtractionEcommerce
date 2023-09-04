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
TABLE = """h1\tAbout us
h2\tJumia careers
-fw -fh\thttps://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/1.jpg?5797"""

HTML_STR_2 = """<div class="_pdmimg __arModalBtn _flx" data-ajax-type="pdp-gallery">
           <img alt="Samsung Galaxy Z Fold 5" height="180" src="https://i.gadgets360cdn.com/products/large/samsung-galaxy-z-fold-5-671x800-1690370876.jpg?downsize=*:180" title="Samsung Galaxy Z Fold 5" width="180">
           </img>
          </div>"""

TABLE_2 = " \thttps://i.gadgets360cdn.com/products/large/samsung-galaxy-z-fold-5-671x800-1690370876.jpg?downsize=*:180"

HTML_STR_3_CLEANED = """"<div class="sldr _img _prod -rad4 -oh -mbs" id="imgs">
          <input checked="" class="sld" id="imgs-sld-1" name="imgs-sld" type="radio"/>
          <a class="itm" data-pop-dyn-id="1" data-pop-open="imageZoom" data-pop-trig="lazy-img-zoom" href="https://ng.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/54/8889201/1.jpg?5797">
           <img alt="product_image_name-Binatone-Dry Iron (Di1255)-1" class="-fw -fh" data-lazy-slide="true" data-src="https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/1.jpg?5797" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
          </a>
          <input class="sld" id="imgs-sld-2" name="imgs-sld" type="radio"/>
          <a class="itm" data-pop-dyn-id="2" data-pop-open="imageZoom" data-pop-trig="lazy-img-zoom" href="https://ng.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/54/8889201/2.jpg?5796">
           <img alt="product_image_name-Binatone-Dry Iron (Di1255)-2" class="-fw -fh" data-lazy-slide="true" data-src="https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/2.jpg?5796" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
          </a>
          <input class="sld" id="imgs-sld-3" name="imgs-sld" type="radio"/>
          <a class="itm" data-pop-dyn-id="3" data-pop-open="imageZoom" data-pop-trig="lazy-img-zoom" href="https://ng.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/54/8889201/3.jpg?5792">
           <img alt="product_image_name-Binatone-Dry Iron (Di1255)-3" class="-fw -fh" data-lazy-slide="true" data-src="https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/3.jpg?5792" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
          </a>
          <input class="sld" id="imgs-sld-4" name="imgs-sld" type="radio"/>
          <a class="itm" data-pop-dyn-id="4" data-pop-open="imageZoom" data-pop-trig="lazy-img-zoom" href="https://ng.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/54/8889201/4.jpg?8427">
           <img alt="product_image_name-Binatone-Dry Iron (Di1255)-4" class="-fw -fh" data-lazy-slide="true" data-src="https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/54/8889201/4.jpg?8427" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"/>
          </a>
         </div>"""
# HTML_STR_3_CLEANED = ""
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
    
    def test_construct_table_str3(self):
        soup = SoupUtils().get_soup(HTML_STR_3_CLEANED)
        res = SoupUtils().construct_table(soup)
        print(res)
        # self.assertEqual(res.strip(), TABLE_2.strip())
    
    def test_construct_table_keep_image(self):
        soup = SoupUtils().get_soup(HTML_STR_2)
        res = SoupUtils().construct_table(soup)
        print(res)
        self.assertEqual(res.strip(), TABLE_2.strip())
        
        
if __name__ == "__main__":
    # unittest.main()
    TestSoupUtils().test_construct_table_str3()
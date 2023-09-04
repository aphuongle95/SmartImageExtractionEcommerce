import urllib.request
from PIL import ImageFile
import urllib.request
 
class ImageUtils():
    SMALL_SIZE = 80
    def is_small(self, uri, threshold=SMALL_SIZE):
        size = self.get_size(uri)
        # if the shorter edge is small
        if min(size) < threshold:
            return True
        return False
        
    def get_size(self, uri):
        # get file size *and* image size (None if not known)
        # req = Request(
        #     url='http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1', 
        #     headers={'User-Agent': 'Mozilla/5.0'}
        # )
        
        headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
        request = urllib.request.Request(url=uri, headers=headers)
        file = urllib.request.urlopen(request)
        size = file.headers.get("content-length")
        if size: 
            size = int(size)
        p = ImageFile.Parser()
        while True:
            data = file.read(1024)
            if not data:
                break
            p.feed(data)
            if p.image:
                return p.image.size
                break
        file.close()
        return (size, None)
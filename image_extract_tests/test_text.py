import unittest

from image_extract.text import TextUtils

class TestTextUtils(unittest.TestCase):
    def test_is_similar(self):
        a = "lazy	https://www.gadgets360.com/static/mobile/images/spacer.png"
        b = "lazy	https://www.gadgets360.com/static/mobile/images/spacer.png"
        res = TextUtils().is_similar(a, b)
        self.assertTrue(res)
    
    def test_is_similar_zalando(self):
        a = "KxHAYs lystZ1 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy	https://img01.ztat.net/article/spp-media-p1/656622d28fa44efdac393a8914b67b89/0f8e2d63071444298b15bc4609a38ea7.jpg?imwidth=300&filter=packshot"
        b = "KxHAYs lystZ1 FxZV-M _2Pvyxl JT3_zV EKabf7 mo6ZnF _1RurXL mo6ZnF _7ZONEy	https://img01.ztat.net/article/spp-media-p1/0dd0ed36a05c406c877bf5eed334d34f/d8d035d3eed44d0fad8c468c245ede2b.jpg?imwidth=300"
        res = TextUtils().is_similar(a, b)
        self.assertTrue(res)
        
if __name__ == "__main__":
    # unittest.main()
    TestTextUtils().test_is_similar_zalando()
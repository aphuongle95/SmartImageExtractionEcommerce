# HTMLMining

## Objective
The aim of this project is to extract images of a product from its product page in an ecommerce website.
The product page can includes different kinds of images, including the product images itself, as well as the images from similar products or logos.
We want to exclude all those irrelevant images.
Also, be aware that not all e-commerce sites are in English, so be careful when filtering by text content.

## Planned steps
- [x] be able to view the html in a clean manner (only tag name, text and image link) 
- [x] extract all headers
- [x] remove unrelevant tags, e.g. script, header, footer
- [ ] divide the page into separate elements, each element is represented as a Beautiful Soup. The element needs to satisfy these following requirements:
    - [ ] every element holds at least one header
    - [ ] if one element contains more than one header: it must be not separable
    - [ ] every image must be kept inside one element 
    - [ ] those elements (either a child or a parent) that don't contain any image or header can be deleted
- results of previous process:
[
    element1: {headers1, tree1 containing images1}
    element2: {headers2, tree2 containing images2}
    ...
]
- [ ] find element that might contain the product's image
    - [ ] classify a header as relevant or not relevant (e.g. Delivery & Returns is not relevant while product_name might be relevant)
    - [ ] keep only the first relevant element
- [ ] check images inside that element

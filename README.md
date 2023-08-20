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
- [x] clean the html to satisfy these following requirements:
    - [x] every image must be kept
    - [x] every header must be kept
    - [x] those elements that don't contain any image or header can be deleted
- [ ] find element that might contain the product's image
    - [ ] : group images by class, find product's title
    - [ ]: find the image class that contains the product's images
        - [-] idea: use openai, 
            - [x] first test: compress the tree further to minimize number of tokens(filter out tokens), recursively feed the api with the cleaned text, ask it return the image link as array >> seems quite successful
            - [ ] next step: 
                - [ ] test with other sites
                - [ ] clean code, batching of the text in a smarter way? check openai tokenizer
                - [ ] use way to identify image? regex or class of image
        - [ ] idea: find the biggest image in the website, it's class and the image near them (maybe make use of css as well)
    - extra step: maybe use image classification 
        - classify between logos and product images
        - classify if 2 product images belong to the similar products or complement products
- [ ] check images inside that element

# Extracting images from ecommerce sites

## Note
This is an ongoing research project so the code is not very clean.

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
    - [ ] find the image class that contains the product's images
        - [-] idea 1: use openai, 
            - first experiment: compress the tree further to minimize number of tokens(filter out tokens), recursively feed the api with the cleaned text, ask it return the image link as array >> seems quite succther essful
            - [x] restructure code: from website link > process with beautiful soup > clean to get a short prompt > return the links
            - [x] keep only important information like image links, header texts and class names
            - [x] remove duplicates if the class + text/link is similar to the last entry
            - [-] should not batch, keep short prompt
            - [-] might use get_image_url_alt to get more image information
            - [x] remove duplicated lines in prompt
            - [x] fix bug related to jumia (image https source doesn't appear in src but in data-src)
            - [x] test with other ecommerce sites
            - [x] reject small images from results (70)
            - [ ] use title and text before and after images in the prompt as well
        - [ ] idea 2: use selenium
            - [x] find the biggest image in the website, it's class and the image near them (maybe make use of css as well)
            - [ ] integrate in the prompt
        - [ ] try crawlbase to load the website correctly
        - [ ] reject images if it doesn't have same parents' div
        - [ ] compare old algorithm with chat-gpt based algorithm to see which ones has better precision
        - observations:
            - maybe we don't even need chatgpt
            - as we made the prompt so clean
            - that we can look at the prompt directly to get the images
    - extra step: maybe use image classification 
        - classify between logos and product images
        - classify if 2 product images belong to the similar products or complement products
- [ ] check images inside that element

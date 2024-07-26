# Extracting Images from Ecommerce Sites

## Note
This is an ongoing research project, so the code may not be very clean.

## Objective
The goal of this project is to extract product images from e-commerce product pages while excluding irrelevant images such as logos or similar product images. This requires handling various languages and filtering based on text content.

## Planned Steps

1. **Initial Setup**
    - [x] Display HTML cleanly (show only tag names, text, and image links)
    - [x] Extract all headers
    - [x] Remove irrelevant tags (e.g., script, header, footer)

2. **HTML Cleaning**
    - [x] Retain all images
    - [x] Retain all headers
    - [x] Delete elements without images or headers

3. **Identifying Product Images**
    - **OpenAI-based Approach**
        - [ ] Use OpenAI to identify the product image class:
            - [x] First experiment: compress the tree to minimize tokens, recursively feed the API with cleaned text, and return image links as an array
            - [x] Restructure code: from website link to BeautifulSoup processing to prompt generation and link extraction
            - [x] Retain only crucial information (image links, header texts, class names)
            - [x] Remove duplicates (if class + text/link is similar to the previous entry)
            - [x] Avoid batching, keep prompts short
            - [x] Fix issues (e.g., image source in data-src attribute on Jumia)
            - [x] Test with other e-commerce sites
            - [x] Reject small images (<70 pixels)
            - [ ] Use title and surrounding text in the prompt
        - **Selenium-based Approach**
            - [x] Identify the largest image, its class, and adjacent images (consider CSS)
            - [ ] Integrate findings into the prompt
        - [ ] Use Crawlbase for proper website loading
        - [ ] Reject images without the same parent div
        - [ ] Compare OpenAI and non-OpenAI algorithms for precision
            - Observations:
                - Direct inspection of cleaned prompts may suffice without ChatGPT
                - Simplified prompts might directly yield images
    - **Extra Step**: Implement image classification to:
        - Differentiate between logos and product images
        - Determine if product images belong to similar or complementary products

4. **Final Steps**
    - [ ] Verify images within identified elements

This project emphasizes leveraging LLMs and ChatGPT for effective prompting to enhance image extraction precision.

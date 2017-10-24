# 99labs-img-processing
Script to generate formatted images from labs' provided main picture and logo.

Input folder: img/
Output folder: output/

## What it does
 
 - Resizes and crops main image to 800x600
 - Adds logo to 150x150 white background 
 - Saves a version of main picture with boxed logo on the right bottom corner

## Usage

	./get_formatted_images.py img/main.* img/logo.* labcet

First argument refers to original main image. Second, original logo. And the third is the lab. name.

If permission is denied, you might run `chmod +x get_formatted_images.py` to make the Python script executable.
# 99labs-img-processing
Script to generate formatted images from labs' provided main picture and logo.

## What it does:
 
 - Resizes and crops main image to 800x600
 - Adds logo to 150x150 white background 
 - Saves a version of main picture with boxed logo on the right bottom corner.

## Usage

	./get_formatted_images.py main.png logo.png labmassa

If permission is denied, you might run `chmod +x get_formatted_images.py`
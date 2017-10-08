#!/usr/bin/env python
import argparse
from PIL import Image

def format_img(filein, width=800, height=600):
	
	#pdb.set_trace()
	img = Image.open(filein)
	w,h = img.size
	w_scale = width / w
	h_scale = height / h
	

	scale = max(w_scale, h_scale)
	img2 = img.resize((int(w*scale), int(h*scale)), Image.BICUBIC)

	box = (0,0,width,height)
	img3 = img2.crop(box)

	#img3.save(fileout)
	return img3

def format_logo(filein):
	
	img = Image.open(filein)
	w,h = img.size

	w_scale = 140 / w
	h_scale = 140 / h
	scale = min(w_scale, h_scale)

	img2 = img.resize((int(w*scale), int(h*scale)), Image.BICUBIC)
	w2,h2 = img2.size

	bg = Image.new('RGB', (150,150), 'white')  # Creates 150x150 white image
	
	# Calculates positions to paste resized logo at the center
	pw = int((150-w2) / 2)
	ph = int((150-h2) / 2)

	box = (pw,ph,pw+w2,ph+h2)  # (left, upper, right, lower)
	bg.paste(img2, box)

	#img3.save(fileout)

	return bg
	

def get_formated_images(input_main, input_logo, lab_name):

	main_img = 		format_img(input_main)
	logo_img = 		format_logo(input_logo)
	
	# Saves separate before pasting together
	main_img.save(lab_name+'_main.png')
	logo_img.save(lab_name+'_logo.png')

	box = (800-150, 600-150, 800, 600)
	main_img.paste(logo_img, box)
	main_img.save(lab_name+'_main-logo.png')

if __name__ == '__main__':
	"""Usage example: ./get_formatted_images.py main.png labtucal-logo.png labtucal """

	parser = argparse.ArgumentParser()
	parser.add_argument('input_main', help='The main image to be resized and cropped.')
	parser.add_argument('input_logo', help='The logo image to be used.', default=0)
	parser.add_argument('lab_name', help='Laboratory name.', default='lab')
	args = parser.parse_args()

	parser = argparse.ArgumentParser()
	get_formated_images(args.input_main, args.input_logo, args.lab_name)


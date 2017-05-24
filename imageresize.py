import os
import sys
from PIL import Image
import glob

def resize(im,width,height):
	img=Image.open(im)
	img_width, img_height = img.size
	img_ratio = img_width/img_height
	comp = (width*img_height)/height
	if((img_width) < comp):
		new_height = height
		new_width = (height * img_width)/img_height
		
		
	else:
		new_width = width
		new_height = (width * img_height)/img_width
	img = img.resize((new_width, new_height), Image.ANTIALIAS)
	return img

def update_canvas(img,width,height,x_off,y_off):
	re_width,re_height = img.size
	if(re_width<width):
		x=(width-re_width)/2
		x_off = x + x_off 
	if(re_height<height):
		y=(height-re_height)/2
		y_off = y + y_off
	new_img.paste(resized,(x_off,y_off))
	
	

width = int(sys.argv[1])
height = int(sys.argv[2])
path = '/home/harsha/Pictures/icons'
os.chdir(path)
file_names = glob.glob(path+"/*.*")
number = len(file_names)
canvas_width = width
canvas_height = number * height
new_img = Image.new('RGB',(canvas_width,canvas_height),(255,255,255,0))
y_offset = 0
x_offset = 0

for each in file_names:
	resized = resize(each,width,height)
	#update canvas
	update_canvas(resized,width,height,x_offset,y_offset)
	y_offset = y_offset + height
	
new_img.save("join.jpg")


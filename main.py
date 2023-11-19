#if the image is bigger than 64x64, there are chance that the code will be too long and it does not work.

scale = 4 #adjust the number to make the image bigger. 1 is normal size.

from PIL import Image
from pyperclip import copy

image = Image.open("image.png") #the name of the image file.
pixels = list(image.getdata())

width = image.size[0]

x = 0
y = 0
ret = 'print("'

for r, g, b in pixels:
    ret += f'<size={2 * scale}><pos={x * scale}><voffset=-{y * scale}><sprite=0 color=#{r:02x}{g:02x}{b:02x}>'
    x += 1
    if x == width:
        y += 1
        x = 0

ret += '</voffset></pos></size>")'

print(len(ret))
copy(ret)

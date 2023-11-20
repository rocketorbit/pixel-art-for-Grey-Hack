#if the image is bigger than 6500 pixels, there are chance that the code will not work.

from PIL import Image
from pyperclip import copy

image = Image.open("image.png") #the name of the image file.
print(f"image mode: {image.mode}. Any mode that is not RGB will convert to RGB.")
image = image.convert("RGB")
pixels = list(image.getdata())

width = image.size[0]
height = image.size[1]

ret = 'hexs = "'

for r, g, b in pixels:
    ret += f'{r:02x}{g:02x}{b:02x}'

ret += '"'

ret += f"""
if params and to_int(params[0]) > 0 then scale = to_int(params[0]) else scale = 1
image = []
x = 0
y = 0
for i in range(0, len(hexs) - 1, 6)
    if x == {width} then
        x = 0
        y = y + 1
    end if
    if x % 256 == 0 then image.push("<size=" + 2 * scale + "><voffset=" + y * -scale + "><pos=0><mspace=" + scale + ">")
    image.push("<sprite=0 color=#" + hexs[i:i + 6] + ">")
    x = x + 1
end for
//for i in range(0, {width - 1}) //this loop is used to put a black line at last row, use if needed
//    if i % 256 == 0 then image.push("<size=" + 2 * scale + "><voffset=" + {height} * -scale + "><pos=0><mspace=" + scale + ">")
//    image.push("<sprite=0 color=#000000>")
//end for
image.push("</pos></voffset></size>")
print(image.join(""))"""

print("code size: " + str(len(ret)))
copy(ret)
print("code copied to clipboard.")
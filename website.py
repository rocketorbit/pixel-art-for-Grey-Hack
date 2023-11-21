scale = 1 #adjust this number to change the size of the image, MUST BE INTEGER BIGGER THAN 0.
imageId = "app"

from PIL import Image
from pyperclip import copy

image = Image.open("ksm.png") #the name of the image file.
print(f"image mode: {image.mode}. Any mode that is not RGB will convert to RGB.")
image = image.convert("RGB")
pixels = list(image.getdata())

width = image.size[0]
height = image.size[1]

ret = f"""<!DOCTYPE html><html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>rocketorbit's proof-of-concept website.</title>
  </head>
  <body>
    <canvas id="{imageId}" width="{width * scale}" height="{height * scale}"></canvas>
    <h1>Made By rocketorbit</h1>
    <script>
      const canvas = document.getElementById('{imageId}')
      const ctx = canvas.context2D
      const scale = {scale}, data = '"""

for r, g, b in pixels:
    ret += f'{r:02x}{g:02x}{b:02x}'

ret += """'
      let x = 0, y = 0, i = 0
      while (i < data.length) {
        let color = '#'
        for (let j = 0; j < 6; ++j) color += data[i++]
        ctx.fillStyle = color
        ctx.fillRect(x * scale, y * scale, scale, scale)
        if (++x >= (canvas.width / scale)) x = ++y - y
      }
    </script>
  </body>
</html>"""

print(f"code size: {len(ret)}")
copy(ret)
print("code copied to clipboard.")
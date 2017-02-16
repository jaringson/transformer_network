from PIL import Image

img = Image.open('e.jpg')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] >= 230 and item[1] >= 230 and item[2] >= 230:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("tra_E.png", "PNG")

# img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
from PIL import Image
from random import randint


all_back = ['grass_0.jpg','grass_1.jpg','grass_2.jpg','grass_3.jpg']
# all_back = ['grass_3.jpg']

background = Image.open(all_back[randint(0,len(all_back)-1)])
width, height = background.size
print width, height


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

foregrounds = []

# for i in range(0,5, 1):
#     foregrounds.append(image.rotate(randint(0,360)))

foregrounds.append(img.rotate(randint(0,360)))



for foreground in foregrounds:
    background.paste(foreground, (randint(100,width-100), randint(100,height-100)), foreground)

background.show()

# img.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
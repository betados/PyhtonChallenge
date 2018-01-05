from PIL import Image
import numpy as np
image = 'text/cave.jpg'
salida= 'text/salida.jpg'
try:
    im = Image.open(image)
except:
    print("No such image", image)
    exit()

px = im.load()
print(im.width, im.height)
print(px[0, 0])
odd = np.zeros((im.height//2, im.width//2, 3), dtype=np.uint8)
even = np.zeros((im.height//2, im.width//2, 3), dtype=np.uint8)

for x in range(im.height):
    try:
        for y in range(im.width):
            if (x+y) % 2 == 0:
                odd[x//2, y//2] = \
                    px[y, x]
            else:
                even[x//2, y//2] = \
                    px[y, x]
    except Exception as e:
        print(e)

oddImg = Image.fromarray(odd, 'RGB')
evenImg = Image.fromarray(even, 'RGB')
oddImg.save('text/oddImg.png')
oddImg.show()
evenImg.save('text/evenImg.png')
evenImg.show()
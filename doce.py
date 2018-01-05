from PIL import Image
import numpy as np
image = 'text/evil1.jpg'
try:
    im = Image.open(image)
except:
    print("No such image", image)
    exit()

px = im.load()
print(im.width, im.height)
print(str(px[0, 0]) + '\n')
init = 210, 20
ancho = 15
odd = np.zeros((im.height, im.width, 3), dtype=np.uint8)
even = np.zeros((im.height, im.width, 3), dtype=np.uint8)

# odd = [p for px[x, y] in px]

# for y in range(im.height):
for y in range(init[1], init[1]+ancho):
    try:
        # for x in range(im.width):
        for x in range(init[0], init[0]+ancho):
            print(px[x, y])
            if x % 2 == 0:
                odd[y, x] = px[x, y]
            else:
                even[y, x] = px[x, y]
        print()
    except Exception as e:
        print(e)

oddImg = Image.fromarray(odd, 'RGB')
evenImg = Image.fromarray(even, 'RGB')
oddImg.save('text/oddEvil.png')
# oddImg.show()
evenImg.save('text/evenEvil.png')
# evenImg.show()
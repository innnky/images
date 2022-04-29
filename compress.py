# from PIL import Image
# im = Image.open("ignore/aaa.png")
# w,h = im.size
# im = im.resize(((int)(w/2), (int)(h/2)))
# im.save('ignore/pico-ouo.png',quality = 100)
import cv2
import os

def compress(name):
    print(name)
    imgs = cv2.imread('ignore/sor/'+name)
    resize_img = cv2.resize(imgs, (0, 0), fx=0.66, fy=0.66, interpolation=cv2.INTER_NEAREST)
    cv2.imwrite('ignore/res/'+name, resize_img)


def filterImg(imgpath):
    if imgpath.endswith(".md.png"):
        return True
    elif imgpath.endswith(".th.png"):
        return True
    elif imgpath.endswith(".th.jpg"):
        return True
    elif imgpath.endswith(".md.jpg"):
        return True
    elif imgpath.endswith("jpg"):
        return False
    elif imgpath.endswith("png"):
        return False
    else:
        return True
for imgpath in os.listdir("ignore/sor"):
    if imgpath!='image-20220425193710847.png':
        continue
    if filterImg(imgpath):
        continue
    compress(imgpath)

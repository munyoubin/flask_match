import cv2
import numpy as np
from pathlib import Path
import os

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def make_crop(img_folder_path):
    for file in Path(img_folder_path).glob('*.jpg'):
        o_f = Path(file.parent/'output')
        o_f.mkdir(exist_ok=True)
        output_path = str(file.parent/'output'/(file.stem+".jpg"))
        print(output_path)

        template = cv2.imread("template.jpg", 0)
        
        img_array = np.fromfile(str(file), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
        #img = cv2.imread(str(file), 0)
        #print(img.shape)

        real_img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        #real_img = cv2.imread(str(file), -1)

        try:
            res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            threshold = .7

            loc = np.where(res >= threshold)

            width = template.shape[0]
            height = template.shape[1]
            #print(width, height)

            x_pos = round(loc[1][0])
            y_pos = round(loc[0][0])+200
            #print(x_pos, y_pos)

            cropped = real_img[y_pos:y_pos+height, x_pos:x_pos+width]
            #print(cropped_image.shape)
            #cv2.imwrite(output_path, cropped_image)
            #a, b = cv2.imencode('.jpg', cropped_image)
            #print(a,b)
            #c = output_path

            imwrite(output_path, cropped)
        except:
            print(output_path, "template과 매치 안됨~~ 딴 사진 쓰삼")
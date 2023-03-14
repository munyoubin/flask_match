import cv2
import numpy as np
from pathlib import Path
    

for file in Path('C:\img2').glob('*.jpg'):
        o_f = Path(file.parent/'output')
        o_f.mkdir(exist_ok=True)
        output_path = str(file.parent/'output'/(file.stem+".jpg"))

        img = cv2.imread(str(file), 0)
        real_img = cv2.imread(str(file), -1)

        template = cv2.imread('template.jpg', 0)
        
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        threshold = .5

        loc = np.where(res >= threshold)

        width = template.shape[0]
        height = template.shape[1]
        #print(width, height)

        x_pos = round(loc[1][0])
        y_pos = round(loc[1][0])

        cropped_image = real_img[y_pos:y_pos+width, x_pos:x_pos+height]
        #print(cropped_image.shape)
        cv2.imwrite(output_path, cropped_image)

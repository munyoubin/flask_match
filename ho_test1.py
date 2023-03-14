import cv2
import numpy as np
from pathlib import Path
from rembg import remove, new_session

session = new_session()

def make_nukki(img_folder_path):

    for file in Path(img_folder_path).glob('*.jpg'):

        o_f = Path(file.parent/'output')
        o_f.mkdir(exist_ok=True)

        input_path = str(file)
        output_path = str(file.parent /'output'/ (file.stem + ".out.png"))
        print(output_path)

        with open(input_path, 'rb') as i:
            with open(output_path, 'wb') as o:
                input = i.read()
                output = remove(input, session=session)
                o.write(output)

print('누끼 작업 진행중')




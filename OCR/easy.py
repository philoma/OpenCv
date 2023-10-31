import easyocr
import numpy as np
from PIL import Image, ImageDraw

reader = easyocr.Reader(['en'])


def detect_text_blocks(img_path):
    detection_result = reader.detect(img_path,
                                 width_ths=0.7, 
                                 mag_ratio=1.5
                                 )
    text_coordinates = detection_result[0][0]
    return text_coordinates


img_path = "bill3.png"
text_coordinates = detect_text_blocks(img_path)
# print(text_coordinates)



def draw_bounds(img_path, bbox):
    image = Image.open(img_path)  
    draw = ImageDraw.Draw(image)
    for b in bbox:
        p0, p1, p2, p3 = [b[0], b[2]], [b[1], b[2]], \
                         [b[1], b[3]], [b[0], b[3]]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill='red', width=2)
    return np.asarray(image)


import cv2
img = cv2.imread('bill3.png')
def draw_boxes(cordinates):
    for i in cordinates:
        x1=i[0]
        x2=i[1]
        y1=i[2]
        y2=i[3]
        global img
        img=cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
            # print("the cordinates are: ",x1, x2, y1, y2)

    
draw_boxes(text_coordinates)
text_blocks_in_image = draw_bounds(img_path, text_coordinates)

recognition_results = reader.recognize(img_path,
                                 horizontal_list=text_coordinates,
                                 free_list=[]
                                 )


res_easyocr=''
for txt in recognition_results:
    # print("{}: {}".format(txt[0],txt[1]))
    res_easyocr+=txt[1]
    # print(txt[1])

# print(res)






# PPOCR recognition Popularly known as PaddleOCR



# Text Recognition using PyTesseract

import pytesseract
res_pytesseract=''
for coord in text_coordinates:
    x_min, y_min, x_max, y_max = coord[0], coord[2], \
                                 coord[1], coord[3]
    
    if x_min >= 0 and x_max >= 0 and \
       y_min >= 0 and y_max >= 0:
        im2 = cv2.imread(img_path)
        cropped = im2[y_min: y_max, x_min: x_max]
        text = pytesseract.image_to_string(cropped)
        # print("{}: {}".format(coord, text))
        res_pytesseract+=text





print(res_pytesseract)
print('<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

print(res_easyocr)


cv2.imshow('Window1', img)
cv2.imshow('Window2', text_blocks_in_image)

cv2.waitKey(0)
cv2.destroyAllWindows()












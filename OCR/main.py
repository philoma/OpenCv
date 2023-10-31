# 1. pytesseract>>>>>>>

# import pytesseract
# from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\Mohd Faisal\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# # Open an image using PIL (Pillow)
# image = Image.open('bill3.png')
# # Perform OCR using Tesseract
# text = pytesseract.image_to_string(image, lang='eng')

# # Print the extracted text
# print(text)

''' Ying Thai Kitchen
2220 Queen Anne AVE N
Seattle WA 98109
« (206) 285-8424 Fax. (206) 285-8427
‘uw .yingthaikitchen.com
Welcome to Ying Thai Kitchen Restaurant.

Order#:17 Table 2
Date: 7/4/2013 7:28 PM

Server: Jack (1.4)
44 Ginger Lover $9.50
[Pork] [24#]

Brown Rice $2.00
Total 2 iten(s) $11.50
Sales Tax $1.09
Grand Total $12.59
Tip Guide

TEK=$1.89, 18%=$2.27, 20%=82.52
Thank you very much,
Cone back again '''





# 2. OCRopus>>>>>>>
# pip install ocrd-anybaseocr
# import ocrolib

# # Load an image
# image = ocrolib.read_image("bill3.png")

# # Perform OCRopus preprocessing, layout analysis, and text recognition
# pages = ocrolib.segment(image)
# for page in pages:
#     text = ocrolib.recognize_page(page)
#     print(text)





# 3.ocr using GOCR

# import subprocess

# input_image = "bill3.png"
# output_text = "output.txt"

# subprocess.call(["gocr", "-i", input_image, "-o", output_text])
# print(output_text)



# 4. Easyocr
# import easyocr

# # Initialize the EasyOCR reader for the desired language(s)
# reader = easyocr.Reader(['en'])  # 'en' stands for English; you can specify multiple languages

# # Perform OCR on an image
# results = reader.readtext('bill3.png')

# # Process the results
# for (bbox, text, prob) in results:
#     # print(f"Text: {text}, Probability: {prob}")
#     print(text)


'''
Ying Thai Kitchen
2220 Queen Anne AVE
Seattle WA 98109
Tel ,
(206) 285-8424 Fax_
(206 ) 285-8427
WWW . y ingthaikitchen,com
come
to Ying Thai Kitchen Restaurant _
Order#
17
Table
Date:
1/4/2013 7:28 PM
Server : Jack
(T.4)
44 Ginger Lover
59.50
[Pork] [2*+]
Brown Rice
82,00
Tota]
item(s)
811,50
Sales Tax
81,09
Grand
Total
$12
59
Lip Guide
158-51, 89 ,
18K-52.27 _
208-82.52
Thank you very much
Come back again
'''




# 5. calamari
# pip install calamari_ocr

# from calamari_ocr.ocr import Infer
# from calamari_ocr.ocr import DataSetType

# # Load a pre-trained model
# model_path = 'path_to_your_model.ckpt'
# ocr_engine = Infer(model_path)

# # Perform OCR on an image
# image_path = 'bill3.png'

# # Specify the image as a list
# image_data = [{"image_path": image_path}]

# # Recognize text in the image
# recognized_text = ocr_engine.recognize(image_data, DataSetType.PREDICT)

# # Print the recognized text
# print(recognized_text[0].texts[0])







# 6. keras-ocr
# pip install keras-ocr
# import keras_ocr

# # Initialize the detector and recognizer

# pipeline = keras_ocr.pipeline.Pipeline()

# # Load and process an image
# images = [keras_ocr.tools.read('bill3.png')]
# predictions = pipeline.recognize(images)

# # Print the recognized text
# for prediction in predictions:
#     for text in prediction:
#         print(text[0])  # The recognized text


'''
ying
thai
kitchen
2220
queen
ave
anne
n
seattle
98109
wa
tel
2064
2658
8424
faxs
1206
2851
8427
yingtha
ikitchen
haw
com
icome
ying
we
to
thai
kitchen
restaurants
ordert
17
table
z
5
dater
71412015
7128
pm
servers
jack
ta
ginger
44
5950
lover
porki
i2t1
brown
rice
sz
o0
total
2
itemis
51150
sa
les
tax
s109
grand
tota
t
512159
tip
guide
154s189
1xs2
21
204s252
thank
mucha
you
very
come
back
in
aga
'''


#7 CuneiForm

# import subprocess

# # Specify the full path to the CuneiForm executable
# cuneiform_executable = 'C:\\path\\to\\cuneiform.exe'  # Replace with your actual path

# # Specify the input image and output text file
# input_image = 'bill3.png'
# output_text = 'output.txt'

# # Run CuneiForm for OCR
# cmd = [cuneiform_executable, input_image, '-o', output_text]
# try:
#     subprocess.run(cmd, check=True)
#     print("OCR complete. Extracted text saved to output.txt.")
# except subprocess.CalledProcessError:
#     print("Error running CuneiForm. Check the path to the CuneiForm executable.")





# 8. Ocrad

# import _winapi

# executable = "C:\\path\\to\\ocrad.exe"  # Replace with the actual path to Ocrad executable
# input_image = "bill3.png"
# output_text = "output.txt"

# # Build the command to run Ocrad
# command = f'{executable} {input_image} -o {output_text}'

# # Run Ocrad using _winapi.CreateProcess
# startup = _winapi.STARTUPINFO()
# process_information = _winapi.PROCESS_INFORMATION()
# _winapi.CreateProcess(None, command, None, None, True, 0, None, None, startup, process_information)

# # Check for process termination
# _winapi.WaitForSingleObject(process_information[0], -1)







import cv2
import pytesseract
from pytesseract import Output
img=cv2.imread('/home/ubaid/Videos/dl/ocr/data/WhatsApp Image 2024-01-04 at 8.12.25 AM.jpeg')
text=pytesseract.image_to_string(img)
cv2.imshow('image',img)
cv2.waitKey()
cv2.destroyAllWindows()
print(text)
data=pytesseract.image_to_data(img,output_type=Output.DICT)
data.keys()
data['text']
data['conf']
n_boxes=len(data['text'])
n_boxes
img=cv2.imread('/home/ubaid/Videos/dl/ocr/data/WhatsApp Image 2024-01-04 at 8.12.25 AM.jpeg')
for i in range(n_boxes):
    if data['conf'][i]>70:
     x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=3)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
import re
date_pattern="^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19|20)\d{2}"
email_pattern="^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
img=cv2.imread('/home/ubaid/Videos/dl/ocr/data/WhatsApp Image 2024-01-04 at 8.12.25 AM.jpeg')
for i in range(n_boxes):
    if data['conf'][i]>70:
      if re.match(date_pattern,data['text'][i]):
        x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=3)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
img=cv2.imread('/home/ubaid/Videos/dl/ocr/data/WhatsApp Image 2024-01-04 at 8.12.25 AM.jpeg')
for i in range(n_boxes):
    if data['conf'][i]>70:
      if re.match(email_pattern,data['text'][i]):
        x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=3)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
img=cv2.imread('/home/ubaid/Videos/dl/ocr/data/WhatsApp Image 2024-01-04 at 8.12.25 AM.jpeg')
for i in range(n_boxes):
    if data['conf'][i]>60:
      if re.match(date_pattern,data['text'][i]) or re.match(email_pattern,data['text'][i]):
        x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=3)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()

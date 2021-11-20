#detection and recognition code should be applied here


from .models import CardImage
import cv2 
import pytesseract
import numpy as np 

x = 1
h = 444
w = 800
dim = (w,h)

def resizedImg():
    return cv2.resize(CardImage.front_img, dim, interpolation=cv2.INTER_AREA)

resized_image = resizedImg()

def grayscale():
    return cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

gray_image = grayscale()

thresh, im_bw = cv2.threshold(gray_image, 127, 230, cv2.THRESH_BINARY)

def thick_font_Dialation(image):
    image = cv2.bitwise_not(image)
    kernel = np.ones((2, 2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image)
    return (image)

dialated_image = thick_font_Dialation(im_bw)

def blur_image():
    return cv2.GaussianBlur(dialated_image, (7, 7), 0)

blured_image = blur_image()

# #front Rectangle
cv2.rectangle(resized_image, (265, 171), (537, 201 ), (0, 255, 0), thickness=2) # ID Number
cv2.rectangle(resized_image, (112, 324), (549, 361), (0, 255, 0), thickness=2) # Name
cv2.rectangle(resized_image, (173, 390), (549, 428), (0, 255, 0), thickness=2) # Nationality

# # Front Crop
ID_Number = dialated_image[171:201, 265:537]
Name = blured_image[324: 361, 112:549]
Nationality = blured_image[390: 428, 173:549]

all_id_card_details_list = []

# # tesseract Front
id_num = pytesseract.image_to_string(ID_Number, lang='eng', config='--psm 6')
name = pytesseract.image_to_string(Name, lang='eng', config='--psm 6')
nationality = pytesseract.image_to_string(Nationality, lang='eng', config='--psm 6')

# # object tesseract front
id_card_details_obj = {
     "id number": id_num.strip(),
    "Name": name.strip(),
    "Nationality": nationality.strip(),
}

all_id_card_details_list.append(id_card_details_obj)
print(all_id_card_details_list)
    

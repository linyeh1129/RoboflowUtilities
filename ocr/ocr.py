import cv2
import pytesseract

x = str(pytesseract.image_to_string('zz.jpg', config='--psm 4'))
print
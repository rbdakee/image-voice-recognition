import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
import cv2


def photo_text():
    img = 'photo/image.jpg'
    image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    if f"{pytesseract.image_to_string(image, lang='rus')}"!="":
        return f"{pytesseract.image_to_string(image, lang='rus')}"
    else:
        return f"В этой фотографии отсутствует какой-либо текст"



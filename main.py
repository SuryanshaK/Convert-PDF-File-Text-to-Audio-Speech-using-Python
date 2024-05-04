import pyttsx3
from PyPDF2 import PdfReader

path = '/Users/suryanshakushwaha/Desktop/startups_IPRFacilitation_22April2016.pdf'
with open(path, 'rb') as file:
    pdfReader = PdfReader(file)
    from_page = pdfReader.pages[20]
    text = from_page.extract_text()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()

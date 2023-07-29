import pyttsx3  
import PyPDF2 
book = open('oop.pdf', 'rb') 
pdfReader = PyPDF2.PdfReader(book) 
pages = len(pdfReader.pages) 
print(pages)
speaker = pyttsx3.init()  
page = pdfReader.pages[7] 
text = page.extract_text()
speaker.say(text)
speaker.runAndWait() 
import PyPDF2
import pyttsx3

book = open("CTCI.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
 
engine = pyttsx3.init()

engine.say("Hello World")
engine.runAndWait()
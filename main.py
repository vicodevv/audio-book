import PyPDF2
import pyttsx3

book = open("CTCI.pdf", "rb").read()
pdfReader = PyPDF2.PdfFileReader(book)

engine = pyttsx3.init()

engine.say(book)
engine.runAndWait()
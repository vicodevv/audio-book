import PyPDF2
import pyttsx3

book = open("CTCI.pdf", "rb") # Open the book ("bookName.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book) 

 
engine = pyttsx3.init()
engine.setProperty('rate', 150)    # Adjust the speed rate (can go over 100)
engine.setProperty('volume', 0.9)  # Adjust the Volume (0-1)

for num in range(100, 200): # Set the Page number to be read (startPage, endPage)
    page = pdfReader.pages[num]
    text = page.extract_text() 

    engine.say(text) 
    engine.runAndWait()

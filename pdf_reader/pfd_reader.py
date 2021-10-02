import pyttsx3
import PyPDF2
book = open('Ch-8 study material.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()
page = pdfReader.getPage(0)
text = page.extractText()
speak(text)
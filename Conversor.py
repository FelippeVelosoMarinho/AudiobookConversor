#pip install PYPDF2
import PyPDF2
import pyttsx3

file = r"test.pdf" #caminho do arquivo
pdf = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdf)
pageObj = pdfReader.getPage(0)


speaker = pyttsx3.init()
voices = speaker.getProperty('voices')

#for voice in voices:
#    print(voice, voice.id)

speaker.setProperty('voice', 'brazil')
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate+200) #velocidade da fala -200,-100,-15, +100, +200

cont = 0
while cont < pdfReader.numPages:
    pageObj = pdfReader.getPage(cont)
    text = pageObj.extractText()
    text2 = 'teste de velocidade da voz'
    speaker.say(text)
    speaker.runAndWait()
    cont += 1

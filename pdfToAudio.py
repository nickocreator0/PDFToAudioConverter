import pyttsx3
import PyPDF2

def pdf_to_speech(path_to_pdf, rate=150, volume=1.0):

    pdf_reader = PyPDF2.PdfReader(open(path_to_pdf, 'rb'))
    engine = pyttsx3.init()

    # Set word per minute
    engine.setProperty('rate', rate)

    # Set the volume
    engine.setProperty('volume', volume)

    clean_txt = ''

    for page_num in range(len(pdf_reader.pages)):
        txt = pdf_reader.pages[page_num].extract_text()
        clean_txt = txt.strip().replace('\n', ' ')

    engine.save_to_file(clean_txt, 'PalpableVoice.wav')
    engine.runAndWait()

    engine.stop()


# Paste the path to your pdf file here
path_to_pdf = './PalpableVoice.pdf'
pdf_to_speech(path_to_pdf)

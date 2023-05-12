# Reading the PDF text and converting it into audio

import pyttsx3
import PyPDF2
from fpdf import FPDF

# msg = "Hii, I am Shyam Goli, A python Developer and AI/ML enthusiatic. \
#     Always want to put my skills for the new innovations and learn new technologies. \
#         This is just my basic intro!"


# pdf = FPDF()
# pdf.add_page()

# pdf.image('C:\\Users\\SPURUSHO\\Desktop\\Machine Learning\\MachineLearning_Daily\\Python_Warmup\\Shyam-design-sketch-name.png', 10, 30, type='png')
# pdf.set_font('Arial', 'B', 16)
# pdf.multi_cell(180, 20, msg)
# pdf.output('output.pdf', 'F')

################################################################
import PyPDF2

# Open the PDF file in read binary mode
with open('C:\\Users\\SPURUSHO\\Desktop\\Machine Learning\\MachineLearning_Daily\\output.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)

    # Get the number of pages in the PDF
    num_pages = len(pdf_reader.pages)

    # Read the content of each page
    for page_number in range(num_pages):
        # Get the page object
        page = pdf_reader.pages[page_number]

        # Extract the text from the page
        page_text = page.extract_text()
        # print(type(page_text))
        # Print the page number and content
        # print(f"Page {page_number + 1}:")
        print(page_text)
        # print('---')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# speed =  engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.say(page_text)
engine.runAndWait()



# pyttsx3.speak(page_text)


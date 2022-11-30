#!/usr/bin/python3

from PyPDF2 import PdfFileReader

from pathlib import Path
pdf_path = (
    Path.home() /
    "python-basics-exercises" /
    "ch14-interact-with-pdf-files" /
    "practice_files" /
    "Pride_and_Prejudice.pdf" 
    #"python_for_web_design" /
    #"python" 
)

# creat an object of pdfFileReader and path for the output file

pdf_reader = PdfFileReader(str(pdf_path))
output_file_path = Path.home() / "Pride_and_Prejudice.txt"

with output_file_path.open(mode="w") as output_file:
    title = pdf_reader.documentInfo.title
    num_pages = pdf_reader.getNumPages()
    output_file.write(f"{title}\nNumber of pages: {num_pages}\n\n")

    # read pages of the pdf

    for page in pdf_reader.pages:
        text = page.extract_text()
        output_file.write(text)
import PyPDF2
import sys

input = sys.argv[1]
output = sys.argv[2]
watermark = sys.argv[3]


# def watermark(pdf_file, output, watermark):
with open(input, "rb") as pdf_file, open(watermark, "rb") as watermark_file:
    pdf = PyPDF2.PdfFileReader(pdf_file)
    watermark = PyPDF2.PdfFileReader(watermark_file)
    watermark_page = watermark.getPage(0)

    writer = PyPDF2.PdfFileWriter()

    for i in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(i)
        pdf_page.mergePage(watermark_page)
        writer.addPage(pdf_page)

    with open(output, "wb") as watermarked:
        writer.write(watermarked)

#watermark(input, output, watermark)

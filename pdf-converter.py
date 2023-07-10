import ebooklib
from ebooklib import epub
from fpdf import FPDF

def epub_to_pdf(epub_file, pdf_file):
    # Open the EPUB file
    book = epub.read_epub(epub_file, 'rb')

    # Create a new PDF object
    pdf = FPDF()

    # Iterate through each chapter in the EPUB book
    for item in book.get_items():
        # Check if the item is an HTML file (chapter)
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Get the chapter content
            content = item.get_content()

            # Add a new page to the PDF
            pdf.add_page()

            # Set the font and size
            pdf.set_font("Arial", size=12)

            # Write the chapter content to the PDF
            pdf.multi_cell(0, 10, content)

    # Save the PDF file
    pdf.output(pdf_file)

# Usage example
epub_file = "./socialism-epub/Capital Volume I - Karl Marx.epub"
pdf_file = "./socialism-pdf/Capital Volume I - Karl Marx.pdf"

epub_to_pdf(epub_file, pdf_file)

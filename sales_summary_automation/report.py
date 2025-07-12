#!/usr/bin/env python3

# Import the base reportlab module (needed for PDF generation)
import reportlab

# Import PDF building components from reportlab's platypus module
from reportlab.platypus import SimpleDocTemplate  # Handles document structure
from reportlab.platypus import Paragraph, Spacer, Table, Image  # Elements used in the document
from reportlab.lib.styles import getSampleStyleSheet  # Provides predefined styles for formatting text
from reportlab.lib import colors  # Allows for color formatting in tables and text

# Function to generate a PDF report
def generate(filename, title, additional_info, table_data):
    # Load a basic set of paragraph styles (for titles, body text, etc.)
    styles = getSampleStyleSheet()

    # Create a new PDF file with the given filename
    report = SimpleDocTemplate(filename)

    # Define the title of the PDF using header style (h1)
    report_title = Paragraph(title, styles["h1"])

    # Define an additional text block (e.g., summary or description)
    report_info = Paragraph(additional_info, styles["BodyText"])

    # Define table style rules:
    # - Add a black grid around all cells
    # - Make the header row bold
    # - Center-align all text in the table
    table_style = [
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    ]

    # Create the table with provided data and apply styling
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

    # Add some vertical space (20 pts) between elements
    empty_line = Spacer(1, 20)

    # Build the final PDF with all components in order
    report.build([
        report_title,
        empty_line,
        report_info,
        empty_line,
        report_table
    ])

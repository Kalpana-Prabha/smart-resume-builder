# PDF export functionality using ReportLab

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class PDFExporter:
    def __init__(self, filename):
        self.filename = filename

    def export(self, data):
        pdf = canvas.Canvas(self.filename, pagesize=letter)
        pdf.drawString(100, 750, "PDF Export")
        # Write your data to the PDF here
        pdf.save()


if __name__ == '__main__':
    exporter = PDFExporter('resume_export.pdf')
    exporter.export({'name': 'John Doe', 'skills': ['Python', 'API Development']})
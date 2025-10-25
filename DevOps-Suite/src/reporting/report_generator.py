from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

class ReportGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.styles = getSampleStyleSheet()

    def generate_report(self, data):
        doc = SimpleDocTemplate(self.filename)
        story = []

        title = Paragraph("Reporte de Métricas del Sistema", self.styles['h1'])
        story.append(title)

        for key, value in data.items():
            p = Paragraph(f"{key}: {value}", self.styles['bodytext'])
            story.append(p)

        doc.build(story)

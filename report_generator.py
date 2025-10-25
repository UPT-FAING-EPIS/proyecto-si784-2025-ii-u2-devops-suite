from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from openpyxl import Workbook

# Este módulo contiene funciones para generar informes en formato PDF y Excel.

# Exporta una lista de casos de prueba a un archivo PDF.
def export_to_pdf(test_cases, filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    data = [["ID", "Nombre", "Prioridad", "Estado", "Resultado"]]
    for tc in test_cases:
        data.append(list(tc))
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    table.setStyle(style)
    doc.build([table])

# Exporta una lista de casos de prueba a un archivo de Excel.
def export_to_excel(test_cases, filename):
    wb = Workbook()
    ws = wb.active
    ws.append(["ID", "Nombre", "Prioridad", "Estado", "Resultado"])
    for tc in test_cases:
        ws.append(list(tc))
    wb.save(filename)
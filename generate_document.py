import webbrowser
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# Create PDF document
pdf = SimpleDocTemplate("calibration_certificate.pdf", pagesize=letter)
styles = getSampleStyleSheet()

# Title
title = Paragraph("<b>Certificado de Calibração</b>", styles["Title"])
subtitle = Paragraph("<b>Serviço nº:</b> CACV215/24", styles["Normal"])

# Table Data
data = [
    ["Frequência de análise", "Valor de referência",
        "Valor do equipamento", "Erro", "Incerteza expandida"],
    ["1000 Hz", "92.0 dB SPL", "92.0 dB SPL", "0.0 dB", "± 0.12 dB"],
    ["63 Hz", "91.9 dB SPL", "91.8 dB SPL", "-0.1 dB", "± 0.12 dB"],
    ["125 Hz", "91.9 dB SPL", "91.8 dB SPL", "-0.2 dB", "± 0.12 dB"],
    ["250 Hz", "91.9 dB SPL", "91.8 dB SPL", "-0.1 dB", "± 0.12 dB"],
    ["500 Hz", "92.0 dB SPL", "91.9 dB SPL", "-0.1 dB", "± 0.12 dB"],
    ["1000 Hz", "92.0 dB SPL", "91.8 dB SPL", "-0.2 dB", "± 0.12 dB"],
    ["2000 Hz", "92.0 dB SPL", "91.8 dB SPL", "-0.2 dB", "± 0.12 dB"],
    ["4000 Hz", "92.0 dB SPL", "91.7 dB SPL", "-0.3 dB", "± 0.12 dB"],
    ["8000 Hz", "92.0 dB SPL", "91.6 dB SPL", "-0.4 dB", "± 0.12 dB"],
    ["16000 Hz", "92.0 dB SPL", "86.7 dB SPL", "-5.3 dB", "± 0.12 dB"],
]

# Create Table (without grid)
table = Table(data, colWidths=[100, 100, 100, 80, 100])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),  # Header row
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),  # Header text color
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Header font bold
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Center align all text
    ("BOTTOMPADDING", (0, 0), (-1, 0), 6),  # Padding for header
    ("TOPPADDING", (0, 1), (-1, -1), 4),  # Padding for data rows
]))

# Build PDF
elements = [title, Spacer(1, 10), subtitle, Spacer(1, 20), table]
pdf.build(elements)

webbrowser.open("calibration_certificate.pdf")
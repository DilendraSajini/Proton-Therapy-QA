from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def build_report(path):
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    doc.build([Paragraph("Giraffe QA Report", styles["Title"])])

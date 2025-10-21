from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path

REPORT_PATH = Path("data/processed/people_report.pdf")

def generate_report(data):
    """
    Generate a PDF report summarizing SWAPI data.
    """
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(REPORT_PATH), pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("Star Wars People Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Table data
    table_data = [["Name", "Birth Year"]]  # Header
    for person in data:
        table_data.append([person["name"], person["birth_year"]])

    table = Table(table_data, hAlign='LEFT')
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("ALIGN", (0, 0), (-1, -1), "LEFT"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ]))

    elements.append(table)
    doc.build(elements)

    print(f"PDF report generated at: {REPORT_PATH}")
    return REPORT_PATH

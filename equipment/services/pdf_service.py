from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from io import BytesIO

def generate_pdf(dataset):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    summary = dataset.summary

    elements.append(Paragraph("Chemical Equipment Parameter Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"<b>File Name:</b> {dataset.file_name}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Uploaded At:</b> {dataset.uploaded_at}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Total Equipment: {summary['total_equipment']}", styles["Normal"]))

    elements.append(Spacer(1, 8))
    elements.append(Paragraph(
        f"Averages — Flowrate: {summary['averages']['flowrate']}, "
        f"Pressure: {summary['averages']['pressure']}, "
        f"Temperature: {summary['averages']['temperature']}",
        styles["Normal"]
    ))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Equipment Type Distribution</b>", styles["Heading2"]))

    table_data = [["Type", "Count"]]
    for k, v in summary["type_distribution"].items():
        table_data.append([k, v])

    table = Table(table_data)
    elements.append(table)

    doc.build(elements)
    buffer.seek(0)

    return buffer

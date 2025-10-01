from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# File path
file_path = "/mnt/data/BotiumToys_Security_Audit_Checklist_2025.pdf"

# Document setup
doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Heading1", fontSize=16, leading=20, spaceAfter=10, textColor=colors.HexColor("#1a5276"), bold=True))
styles.add(ParagraphStyle(name="Heading2", fontSize=13, leading=16, spaceAfter=8, textColor=colors.HexColor("#154360"), bold=True))
styles.add(ParagraphStyle(name="NormalBold", fontSize=11, leading=14, spaceAfter=6, textColor=colors.black, bold=True))

# Content
elements = []

# Title
elements.append(Paragraph("Botium Toys Security Audit Checklist - 2025", styles["Heading1"]))
elements.append(Spacer(1, 12))

# Intro
elements.append(Paragraph("This document presents a comprehensive security audit for Botium Toys, "
                          "evaluating the company’s security controls, compliance alignment, and "
                          "providing actionable recommendations to strengthen its cybersecurity posture.", styles["Normal"]))
elements.append(Spacer(1, 12))

# Section 1: Control Assessment
elements.append(Paragraph("1. Control Assessment", styles["Heading2"]))
controls = [
    ["Control", "Status", "Notes"],
    ["Least Privilege", "Needs Improvement", "Users have excessive permissions in several departments."],
    ["Firewalls & IDS", "Partially Implemented", "Perimeter firewalls exist, but IDS/IPS coverage is limited."],
    ["Encryption", "Insufficient", "Sensitive customer payment info not encrypted at rest."],
    ["Logging & Monitoring", "Needs Improvement", "Critical system logs not centralized or regularly reviewed."],
]
table1 = Table(controls, colWidths=[150, 120, 250])
table1.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a5276")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("ALIGN", (1, 1), (-1, -1), "CENTER"),
]))
elements.append(table1)
elements.append(Spacer(1, 12))

# Section 2: Compliance Review
elements.append(Paragraph("2. Compliance Review", styles["Heading2"]))
compliance = [
    ["Standard", "Compliance Status", "Notes"],
    ["PCI DSS", "Partially Compliant", "Cardholder data not fully encrypted or segmented."],
    ["GDPR", "Non-Compliant", "No formal data subject rights request handling process."],
    ["SOC 1 & 2", "Not Certified", "Internal controls require significant improvement before audit."],
]
table2 = Table(compliance, colWidths=[150, 120, 250])
table2.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#154360")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("ALIGN", (1, 1), (-1, -1), "CENTER"),
]))
elements.append(table2)
elements.append(Spacer(1, 12))

# Section 3: Recommendations
elements.append(Paragraph("3. Key Recommendations", styles["Heading2"]))
recommendations = [
    "Implement least privilege and enforce separation of duties.",
    "Introduce multi-factor authentication (MFA) across all critical systems.",
    "Establish regular maintenance and patching for legacy systems.",
    "Encrypt sensitive data, including customer payment information, at rest and in transit.",
    "Create and test disaster recovery and incident response plans.",
    "Introduce secure password policies and deploy a password manager.",
    "Centralize log collection and implement continuous monitoring with alerting.",
]
for rec in recommendations:
    elements.append(Paragraph(f"• {rec}", styles["Normal"]))

elements.append(Spacer(1, 12))

# Section 4: Risk Ratings
elements.append(Paragraph("4. Risk Ratings", styles["Heading2"]))
risk_ratings = [
    ["Issue", "Risk Level", "Impact"],
    ["Excessive Permissions", "High", "Potential insider threats and privilege misuse."],
    ["Lack of Encryption", "Critical", "Customer payment data at risk of compromise."],
    ["Legacy Systems", "Medium", "Unpatched systems vulnerable to known exploits."],
    ["Weak Logging", "Medium", "Delayed detection of breaches or anomalies."],
]
table3 = Table(risk_ratings, colWidths=[200, 100, 220])
table3.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#21618c")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("ALIGN", (1, 1), (-1, -1), "CENTER"),
]))
elements.append(table3)
elements.append(Spacer(1, 12))

# Closing
elements.append(Paragraph("✅ This audit document is intended to guide Botium Toys in strengthening its cybersecurity posture for 2025 and beyond. "
                          "Implementing the above recommendations will significantly reduce the risk of security incidents and compliance failures.",
                          styles["Normal"]))

# Build PDF
doc.build(elements)

file_path

from docxtpl import DocxTemplate
from pathlib import Path
import tempfile
import subprocess

class CertificatePDFGenerator:
    def __init__(self, output_dir: str = "generated_pdfs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def generate_pdf(self, template_path: str, context: dict, filename: str) -> Path:
        # Load template and render
        doc = DocxTemplate(template_path)
        doc.render(context)

        # Save temporary docx
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp_docx:
            doc.save(tmp_docx.name)

            # Define final pdf path
            pdf_path = self.output_dir / f"{filename}.pdf"

            # Convert to PDF using LibreOffice (make sure it's installed on the system)
            subprocess.run([
                "libreoffice",
                "--headless",
                "--convert-to", "pdf",
                "--outdir", str(self.output_dir),
                tmp_docx.name
            ], check=True)

        return pdf_path

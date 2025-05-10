import zipfile
from pathlib import Path

class ZipManager:
    def __init__(self, output_dir: str = "generated_pdfs"):
        self.output_dir = Path(output_dir)
    
    def create_zip(self, pdf_paths: list[Path], zip_filename: str) -> Path:
        # Define output ZIP file path
        zip_path = self.output_dir / f"{zip_filename}.zip"
        
        # Create a ZIP file and add PDFs to it
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for pdf in pdf_paths:
                zipf.write(pdf, pdf.name)  # Add file with its name
        
        return zip_path

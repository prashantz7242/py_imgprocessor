from py_imgprocessor.pdf.utils import PDFTool
from pathlib import Path


if __name__ == "__main__":
    current_path = Path(__file__).resolve(strict=True).parent.parent
    pdf_tool = PDFTool()
    MEDIA_FILE_PATH = str(current_path / "media")
    status_fn = pdf_tool.convert_to_image(
        output_path=MEDIA_FILE_PATH
    )
    print(f"status_fn: {status_fn}")

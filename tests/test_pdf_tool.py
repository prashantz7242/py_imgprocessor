import os
import unittest
from pathlib import Path

from py_imgprocessor.pdf.utils import PDFTool


class TestPDFTool(unittest.TestCase):
    """
        Testing PDFTool object methods

    Args:
        unittest (_type_): Base class for creating test cases
    """

    def test_folder_creation(self):
        """ testing create_folder method
        """
        pdf_tool = PDFTool()

        current_path = Path(__file__).resolve(strict=True).parent

        media_folder2_file_path = str(current_path / "media")

        # Call the method
        result = pdf_tool.create_folder(media_folder2_file_path)

        # Assert that the folder was created
        self.assertTrue(result)
        self.assertTrue(os.path.exists(media_folder2_file_path))

        # Clean up after the test
        os.rmdir(media_folder2_file_path)
    
    def test_convert_to_image(self):
        """ testing convert to image method
        """
        pdf_tool = PDFTool()
        current_path = Path(__file__).resolve(strict=True).parent
        media_folder_test_file_path = str(current_path / "media_test")
        result = pdf_tool.convert_to_image(media_folder_test_file_path)

        # Assert that the folder was created
        self.assertTrue(result)
        self.assertTrue(os.path.exists(media_folder_test_file_path))

        # Clean up after the test
        os.rmdir(media_folder_test_file_path)


if __name__ == "__main__":
    unittest.main()

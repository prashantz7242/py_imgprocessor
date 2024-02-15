import os


class PDFTool(object):
    """
    TODO: How to convert the pdf to image

    Args:
        object (_type_): _description_
    """

    def create_folder(self, folder_path: str) -> bool:
        """
        ensure that folder is created

        Args:
            folder_path (str): full path eg. /home/doc/media/pdf/

        Returns:
            bool: status of folder creation
        """
        is_folder_created = False
        try:
            os.makedirs(folder_path)
            is_folder_created = True
        except FileExistsError:
            # it ensure that dir is already exists
            is_folder_created = True
        return is_folder_created

    def convert_to_image(self, output_path: str) -> bool:
        """
        convert pdf to img & store every img in particular given folder

        Args:
            output_path (str): _description_

        Returns:
            bool: status of is pdf pages converted to img
        """
        is_folder_created = self.create_folder(output_path)
        return is_folder_created

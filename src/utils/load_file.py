import pandas as pd
from src.logger import ProjectLogger

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.logger = ProjectLogger().get_logger()
    
    def get_extension(self):
        """
        Get the file extension from the provided file name.

        Returns:
            str: File extension.
        """
        self.logger.info(f"Getting file extension for {self.filename}")
        try:
            name_split = self.filename.split('.')
            return name_split[-1]
        except Exception as e:
            self.logger.error(f"Error getting file extension: {e}")

    def load_file(self):
        """
        Load the file based on its extension.

        Returns:
            pd.DataFrame: Loaded data.
        """
        self.logger.info(f"Loading file {self.filename}")
        try:
            ext = self.get_extension()
            if ext == 'csv':
                return pd.read_csv(self.filename)
            elif ext == 'json':
                return pd.read_json(self.filename)
            elif ext == 'xlsx':
                return pd.read_excel(self.filename)
            else:
                self.logger.error(f"Unsupported file extension: {ext}")
                return None
        except Exception as e:
            self.logger.error(f"Error loading file: {e}")
            return None

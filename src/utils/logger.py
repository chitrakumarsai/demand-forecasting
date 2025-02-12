# src/utils/logger.py

import os
import logging

class ProjectLogger:
    """
    Class to manage logging for the project and writing logs to a file
    """

    LOG_FILE_PATH = "../logs/project.log"

    def __init__(self) -> None:
        """
        Initialize the ProjectLogger class
        """
        # Ensure logs directory exists
        os.makedirs(os.path.dirname(self.LOG_FILE_PATH), exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,
            format = "%(asctime)s [%(levelname)s] %(message)s",
            handlers= [
                logging.FileHandler(self.LOG_FILE_PATH),
                logging.StreamHandler()
            ])
        
        self.logger = logging.getLogger(__name__)

    def get_logger(self):
        """
        Get the logger instance
        """
        return self.logger

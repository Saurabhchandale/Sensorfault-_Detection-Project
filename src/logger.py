# it's help in debugging and monitering when the application run

# --------------------------------------------
# Logging Configuration Script with Explanations
# --------------------------------------------

import logging      # Import the logging module to record runtime events
import os           # For creating directories and handling file paths
from datetime import datetime   # To generate timestamps for log file names

# Generate a unique log file name using the current date and time
# Example: "10_21_2025_21_1734836785.log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log"

# Define the path for storing logs inside a 'logs' folder in the current working directory
logs_path = os.path.join(os.getcwd(), "logs")

# Create the 'logs' folder if it doesn't already exist
os.makedirs(logs_path, exist_ok=True)

# Combine the folder path and log file name to get the full file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging system
logging.basicConfig(
    filename=LOG_FILE_PATH,   # Log file path
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Log message format
    level=logging.INFO        # Logging level (INFO captures general runtime information)
)

# Example usage (uncomment to test):
# logging.info("Logging system has been initialized successfully.")



"""
import logging
import os
from datetime import datetime

LOG_FILE =f"{datetime.now().strftime('%m_%d_%Y_%H_%s')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH= os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(massage)s",
    level=logging.INFO
)
"""
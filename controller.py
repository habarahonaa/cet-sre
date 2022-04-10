import datetime
import sys
import os
from importlib.resources import path
from create_file import create_compressed_backup
from dotenv import load_dotenv
from gdrive_authentication import google_drive_auth
from gdrive_upload import gdrive_upload

def controller():
    ''' Runs archive compression, Google Authentication and Drive upload tasks in order.
    
    Executes backup tasks in order.
    '''
    load_dotenv()
    # Sets folder path to be backed up, reads from .env file
    path = os.getenv('BACKUP_PATH')
    # Gets current date and time to be used as file name
    now = datetime.datetime.now()
    # Creates the backup file name by joining the provided path and current date and time
    file_name = "cisco_backups" + now.strftime("%Y-%m-%d_%H-%M-%S").replace('/', '-')
    # Attempts zip compression of the provided path. If not successful, prints error message and exits
    if not create_compressed_backup(path, file_name):
        print("Error: Unable to create backup file.")
        sys.exit(0)
    # Else, starts Google authentication process calling the gdrive_auth() function
    auth, drive = google_drive_auth()
    # Attempts to upload the compressed file to Google Drive. If not successful, prints error message and exits
    if not gdrive_upload(drive, file_name):
        print("Error: Unable to upload backup file.")
        sys.exit(0)
    # Else, prints success message and exits
    else:
        print("Success: Backup file uploaded to Google Drive.")
        sys.exit(0)
import schedule
import sys
import time
from controller import controller
from gdrive_authentication import google_drive_auth
from gdrive_list_files import gdrive_listing

if __name__ == "__main__":
    # Runs the controller function inmediately
    gdrive_listing(google_drive_auth())
    # Runs the controller function every sunday at 10:00
    '''
    schedule.every().sunday.at("10:00").do(controller)
    while True:
        schedule.run_pending()
        time.sleep(1)
        sys.stdout.flush()
    '''
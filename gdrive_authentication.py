from os import environ as env
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build


def google_drive_auth():
    ''' Authenticates desired Google account and returns a service object.

    Using the service account credentials, the function authenticates to the desired Google account and returns a service object that can be used to call methods on the Google Drive API.

    Returns:
           service: Authenticated Google Drive service object.
    '''
    load_dotenv()
    # Sets authentication scope
    print("Authenticating to Google Drive...")
    SCOPES = ['https://www.googleapis.com/auth/drive']
    # Gets credentials path from environment variable 'GOOGLE_APPLICATION_CREDENTIALS' using dotenv
    SERVICE_ACCOUNT_FILE = env['GOOGLE_APPLICATION_CREDENTIALS']
    # Creates a credentials object from the service account file
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        # Authenticates to Google Drive using the credentials object
        service = build('drive', 'v3', credentials=credentials)
        print("Authentication successful!")
        return service

    except Exception as e:
        print("Authentication failed!")
        print(e)
        return None

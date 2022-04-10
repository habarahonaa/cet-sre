from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def google_drive_auth():
    ''' Authenticates desired Google account.

    Uses PyDrive's OAuth 2.0 wrapper to authenticate to Google Driveaccount where backups will be
    stored. It uses a built-in method that sets up a local web server for authentication purposes.
    This allows automatic reception of authentication codes from the user and local auth.

    Returns:
            gauth: an instance of the GoogleAuth class that has an approved or rejected token.
            drive: an instance of the GoogleDrive class and associated methods (receives an authorized GoogleAuth instance to do so)
    '''
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    print('Succesfully Authenticated to Google Drive')
    return gauth, drive
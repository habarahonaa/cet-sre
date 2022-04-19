from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

def gdrive_upload(service, file_name):
    ''' Uploads a file to Google Drive.
    
    Using the provided service object, the function uploads the provided file to Google Drive by creating a new file in the root folder.
    
    Args:
        service: Authenticated Google Drive service object.
        file_name: the name of the file to be uploaded
    Returns:
        bool: True if file is uploaded. False if failed upload
    '''
    # HEADS UP: The file path is currently hardcoded because the file is always going to be inside the archive directory.
    file_path = "archive/" + file_name + ".zip"
    try:
        # Attempts to upload the file to Google Drive. If not successful, prints error message and exits
        print("Uploading backup file to Google Drive...")
        file_metadata = {'name': file_name + '.zip'}
        media = MediaFileUpload(file_path,
                                mimetype='application/zip')
        file = service.files().create(body=file_metadata, media_body=media, fields="id").execute()
        print(F'File ID: {file.get("id")}')
        print("Success: Backup file uploaded to Google Drive.")
        return True
    except HttpError as e:
        print("Error: Unable to upload backup file.")
        print(e)
        return False
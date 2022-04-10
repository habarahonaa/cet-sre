def gdrive_upload(drive, file_name):
    ''' Uploads a file to Google Drive.
    
    Uses PyDrive's GoogleDrive class to upload a file to Google Drive.
    This function is called by the main function.
    
    Args:
        drive: an instance of the GoogleDrive class and associated methods (receives an authorized GoogleAuth instance to do so)
        path: the path to the file to be uploaded
        file_name: the name of the file to be uploaded
    Returns:
        bool: True if file is uploaded. False if failed upload
    '''
    # HEADS UP: The file path is currently hardcoded because the file is always going to be inside the archive directory.
    file_path = "archive/" + file_name + ".zip"
    # Creates a metadata attribute for the file to be uploaded
    file1 = drive.CreateFile({'title': file_name})
    # Sets the content of the file to be uploaded from the provided path
    file1.SetContentFile(file_path)
    # Uploads the file to Google Drive
    file1.Upload()
    print('Uploaded %s to Google Drive' % file_name)
    return True
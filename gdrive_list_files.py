from googleapiclient.errors import HttpError
 
def gdrive_listing(service):
    ''' Lists all files in the user's Google Drive.

    Using the provided service object, the function lists all files in the user's Google Drive. More specifically, it lists all files in the root folder belonging to the service account, so the function will not list files in subfolders or files that belong to other users.
    TODO: add folder delegation to share files in service account with other users.

    Args:
        service: Authenticated Google Drive service object.
    Returns:
        none
    
    '''
    try:
        results = service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        print(f'An error occurred: {error}')
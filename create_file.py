import shutil

def create_compressed_backup(path, file_name):
    '''Creates a compressed file from the provided path.

    Returns true if file is found and creates a compressed file
    from the backup folder in ZIP format using shutil

    Args:
        path (string): folder path to be compressed
        file_name (string): archive name to be saved as
            
    Returns:
        bool: True if folder to be compressed exists. False if failed compression
    '''
    try:
        shutil.make_archive(f"archive/{file_name}", 'zip', path)
        print(f"Created compressed backup: {file_name}")
        return True
    except FileNotFoundError:
        return False
# GDrive Uploader

> Author: Brian Tomlinson <brian@smartm.no>


## Description

> Uploads a file to the specified folder in Google Drive


## Usage Example 1 (as Lib)

    
    from libdriveuploader import upload
    
    
    config = {'email': 'gmailaddr', 'password': 'gmail password'}
    filename = 'path/to/file'
    foldername = 'folder in GDrive'  # Can be subfolder, no parent needed
    mimetype = 'type'  # 'text/csv', 'application/pdf', etc...
    
    result = upload(config, filename, foldername, mimetype)
    
    >>> result
    >>> <gdata.docs.data.Resource object>  # See Google Dev Docs for methods on this resource
    


## Usage Example 2 (CLI)

    
    $ python2 /path/to/libdriveuploader.py /path/to/config.json /path/to/file DriveFolderName mimetype
    $ result  # One of None, Error, Success
    

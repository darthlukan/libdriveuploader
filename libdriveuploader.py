# ~*~ coding: utf-8 ~*~
import sys
import json
import gdata.data
import gdata.docs.data
import gdata.docs.client


def make_client(config):
    email = config['email']
    password = config['password']
    client = gdata.docs.client.DocsClient(source='libdriveuploader')
    client.http_client.debug = True
    client.client_login(email, password, source=client.source, service=client.auth_service)
    return client


def get_folder(client, foldername):
    folder = None
    for resource in client.GetAllResources(uri='/feeds/default/private/full/-/folder'):
        if resource.title.text == foldername:
            folder = resource
            break
    return folder


def upload(config, filename, foldername):
    client = make_client(config)
    folder = get_folder(client, foldername)
    if folder is not None:
        if "/" in filename:
            name = filename.split('/')[-1]
        else:
            name = filename
        doc = gdata.docs.data.Resource(type='text/csv', title=name)
        media = gdata.data.MediaSource()
        media.set_file_handle(filename, 'text/csv')
        result = client.CreateResource(doc, media=media, collection=folder)
        return result
    return None


def main():
    config = json.load(sys.argv[1])
    filename = sys.argv[2]
    foldername = sys.argv[3]
    client = make_client(config)
    folder = get_folder(client, foldername)
    if folder is not None:
        result = upload(config, filename, foldername)
    else:
        result = None
    return result


if __name__ == '__main__':
    main()

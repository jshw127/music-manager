import os, requests

try:
    CLIENTID = os.environ['CLIENTID']
except KeyError:
    from spotify.secrets import CLIENTID

def get_album(album_id, client_id):
    '''Query spotify api for album using album id'''
    
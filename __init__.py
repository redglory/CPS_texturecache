from .main import Texturecache

def autoload():
    return Texturecache()

config = [{
    'name': 'texturecache',
    'groups': [
        {
            'tab': 'notifications',
            'list': 'notification_providers',
            'name': 'texturecache',
            'label': 'Texturecache',
            'description': 'Set movie local artwork on XBMC Media library and cache it!',
            'options': [
                {
                    'name': 'enabled',
                    'default': 0,
                    'type': 'enabler',
                },
                {
                    'name': 'texturecache_path',
                    'label': 'TextureCache.py script path',
                    'type': 'directory',
                    'description': 'Choose texturecache.py script path',
                },
                {
                    'name': 'mklocal_path',
                    'label': 'Mklocal.py script path',
                    'type': 'directory',
                    'description': 'Choose mklocal.py script path',
                },
                {
                    'name': 'config_file',
                    'label': 'Configurations file',
                    'type': 'directory',
                    'description': 'Choose TextureCache configuration file (texturecache.cfg) path',
                },
                {
                    'name': 'local_path',
                    'label': 'Path to local artwork',
                    'type': 'directory',
                    'description': 'Choose your local artwork path',
                },
                {
                    'name': 'prefix_path',
                    'label': 'Path to prefix artwork',
                    'default': 'ftp://192.168.1.77:60666/Movies/',
                    'description': 'Choose your prefix artwork path',
                },
                {
                    'name': 'custom_artwork',
                    'label': 'Custom Artwork',
                    'advanced': True,
                    'default': 'poster fanart clearlogo:logo clearart discart:disc banner landscape',
                    'description': 'Choose your custom custom artwork to download/set separated by space',
                },
                {
                    'name': 'readonly',
                    'label': 'Readonly',
                    'advanced': True,
                    'type': 'bool',
                    'default': 1,
                    'description': 'Check this if you don\'t want to download any artwork using only local files',
                },
                {
                    'name': 'nokeep',
                    'label': 'No keep',
                    'advanced': True,
                    'type': 'bool',
                    'default': 1,
                    'description': 'Check this if you don\'t want to keep media library artwork if local files no longer exist',
                },
            ],
        }
    ],
}]

'''
A tool plugin for Plover to open configuration related paths.
'''

from plover.engine import StenoEngine
from plover.config import CONFIG_DIR, CONFIG_FILE

from open_path.dialog import OpenPathDialog


class OpenConfigFolder(OpenPathDialog):
    ''' Open the configuration folder. '''

    TITLE = 'Config Folder'
    ICON = ':/open_path/folder.svg'
    ROLE = 'configfolder'
    SHORTCUT = None

    def __init__(self, engine: StenoEngine):
        super().__init__(engine)

        self.path = CONFIG_DIR

class OpenConfigFile(OpenPathDialog):
    ''' Open the configuration file. '''

    TITLE = 'Config File'
    ICON = ':/open_path/file.svg'
    ROLE = 'configfile'
    SHORTCUT = None

    def __init__(self, engine: StenoEngine):
        super().__init__(engine)

        self.path = CONFIG_FILE

'''
A generic tool plugin base for Plover to open paths. 
'''

import webbrowser

from PyQt5 import QtCore, QtGui
from plover.gui_qt.tool import Tool
from plover.engine import StenoEngine

from open_path import resources_rc


class OpenPathDialog(Tool):
    '''
    Hidden dialog for opening a path.
    '''

    path = ''

    def __init__(self, engine: StenoEngine):
        super().__init__(engine)
        # Intentionally skip this as it causes this from Tool:
        # AttributeError: 'super' object has no attribute 'setupUi'
        # self.setupUi(self)

        self.setObjectName('OpenConfigFolder')
        # setVisible does not seem to work, so just make ourselves really small
        self.resize(0, 0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def showEvent(self, event: QtGui.QShowEvent):
        '''
        Overriden showEvent for the QDialog.
        Closes automatically after opening a path.

        :param event: The show event.
        '''

        # Best crossplatform way to open a path?
        webbrowser.open(self.path)

        self.close()

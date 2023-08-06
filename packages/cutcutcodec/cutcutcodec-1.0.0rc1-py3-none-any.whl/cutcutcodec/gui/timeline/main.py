#!/usr/bin/env python3

"""
** Allows video and audio cronological previews and editing. **
---------------------------------------------------------------
"""

from PyQt6 import QtWidgets

from cutcutcodec.gui.base import CutcutcodecWidget
from cutcutcodec.gui.timeline.slider import Slider
from cutcutcodec.gui.timeline.tracks import Tracks



class Timeline(CutcutcodecWidget, QtWidgets.QWidget):
    """
    ** Time slider and tracks. **
    """

    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent

        self.slider = Slider(self)
        self.tracks = Tracks(self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.tracks)
        self.setLayout(layout)

    def refresh(self):
        self.slider.refresh()
        self.tracks.refresh()

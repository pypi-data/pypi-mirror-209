#!/usr/bin/env python3

"""
** The widget that contains all the elements for the video edition. **
----------------------------------------------------------------------
"""

from PyQt6 import QtWidgets

from cutcutcodec.gui.base import CutcutcodecWidget
from cutcutcodec.gui.graph.graph_editor import GraphEditor
from cutcutcodec.gui.timeline.main import Timeline



class EditionTabs(CutcutcodecWidget, QtWidgets.QWidget):
    """
    ** Contains the different selection windows. **
    """

    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent

        # declaration
        self.graph_editor = GraphEditor(self)
        self.timeline = Timeline(self)

        # location
        tabs = QtWidgets.QTabWidget()
        tabs.addTab(self.timeline, "Timeline")
        tabs.addTab(self.graph_editor, "Graph")
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(tabs)
        self.setLayout(layout)

    def refresh(self):
        """
        ** Updates the elements of this widget and child widgets. **
        """
        self.graph_editor.refresh()
        self.timeline.refresh()

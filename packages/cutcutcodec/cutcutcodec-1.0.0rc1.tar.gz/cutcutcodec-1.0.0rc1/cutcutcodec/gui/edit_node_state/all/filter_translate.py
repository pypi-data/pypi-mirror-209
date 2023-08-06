#!/usr/bin/env python3

"""
** Properties of a ``cutcutcodec.core.filter.basic.translate.FilterTranslate``. **
----------------------------------------------------------------------------------
"""

import math

from PyQt6 import QtWidgets

from cutcutcodec.gui.edit_node_state.base import EditBase
from cutcutcodec.gui.edit_node_state.interface import Numberable



class EditFilterTranslate(EditBase):
    """
    ** Allows to view and modify the properties of a filter of type ``FilterTranslate``.
    """

    def __init__(self, parent, node_name):
        super().__init__(parent, node_name)
        grid_layout = QtWidgets.QGridLayout()
        Numberable(self, "delay", (-math.inf, math.inf), isfinite=True)(grid_layout)
        self.setLayout(grid_layout)

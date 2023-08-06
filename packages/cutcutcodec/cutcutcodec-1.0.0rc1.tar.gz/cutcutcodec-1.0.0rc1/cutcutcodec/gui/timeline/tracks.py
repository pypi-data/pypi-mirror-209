#!/usr/bin/env python3

"""
** Allows drawing the tracks in the timeline. **
------------------------------------------------
"""

from fractions import Fraction
import math

from PyQt6 import QtCore
import pyqtgraph

from cutcutcodec.gui.base import CutcutcodecWidget



class TimeAxisItem(pyqtgraph.AxisItem):
    """
    ** Internal timestamp for x-axis. **
    """

    def tickStrings(self, values, scale, spacing):
        """
        ** Function overloading the weak default version to provide timestamp. **
        """
        if spacing >= 1e-1:
            return [f"{int(value)//60:02d}:{value%60:04.1f}" for value in values]
        return [f"{int(value)//60:02d}:{value%60:06.3f}" for value in values]


class Tracks(CutcutcodecWidget, pyqtgraph.PlotWidget):
    """
    ** Canva with tracks and time rules. **

    self.viewRange() -> [[xmin, xmax], [ymin, ymax]]
    """

    def __init__(self, parent):
        super().__init__(parent)
        self._parent = parent

        self.setLimits(xMin=0, minYRange=0.5, maxYRange=2)
        self.invertY(True)
        self.setAxisItems({"bottom": TimeAxisItem(orientation="bottom")})
        self.showAxis("left", False)
        self.sigRangeChanged.connect(Tracks.event_range_changed)

        self.cursor = pyqtgraph.InfiniteLine(angle=90, movable=True)
        self.cursor.addMarker("<|>", 0, 20)
        self.cursor.sigDragged.connect(self.event_position_changed) # sigPositionChangeFinished
        self.addItem(self.cursor)

    def event_position_changed(self, cursor):
        """
        ** Called when the cursor is moved. **
        """
        timestamp = Fraction(cursor.x())
        self.main_window.sub_windows["video_preview"].frame_extractor.set_position(timestamp)

    def event_range_changed(self, box):
        """
        ** Called when the range is changed. **
        """
        (t_min, t_max), _ = box
        self.parent.slider.update_range(t_min, t_max)

    def refresh(self):
        duration = (
            max((s.beginning+s.duration for s in self.app.tree().in_streams), default=math.inf)
        )
        if duration == math.inf:
            self.setLimits(xMax=None)
        else:
            self.setLimits(xMax=duration) # duration + 10%

    @QtCore.pyqtSlot(Fraction)
    def update_pos(self, timestamp):
        """
        ** Set the cursor at the write position. **
        """
        self.cursor.setPos(timestamp)

    def update_range(self, t_min: Fraction, t_max: Fraction):
        """
        ** Updates the position from slice. **
        """
        self.setXRange(t_min, t_max, padding=0) # E1124 (redundant-keyword-arg) in pylint 2.17.2

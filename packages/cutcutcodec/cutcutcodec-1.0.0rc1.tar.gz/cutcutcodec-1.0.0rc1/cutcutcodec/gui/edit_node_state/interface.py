#!/usr/bin/env python3

"""
** Allows you to avoid redundancy in the node editing windows. **
-----------------------------------------------------------------

Defines several accessors that allow to lighten the code of child classes.
This is also where methods common to several classes are implemented to avoid data redundancy.
"""

from fractions import Fraction
import math
import numbers

from PyQt6 import QtWidgets

from cutcutcodec.gui.edit_node_state.base import EditBase



class Numberable:
    """
    ** Allows to manage a number field to extract a fraction or or inf. **
    """

    def __init__(self,
        edit: EditBase,
        state: str,
        bounds: tuple[numbers.Real, numbers.Real]=(-math.inf, math.inf),
        isfinite: bool=False,
    ):
        assert isinstance(edit, EditBase), edit.__class__.__name__
        assert isinstance(state, str), state.__class__.__name__
        assert state in edit.state, f"{state} not in {sorted(edit.state)}"
        assert isinstance(bounds, tuple), bounds.__class__.__name__
        assert len(bounds) == 2, bounds
        assert isinstance(bounds[0], numbers.Real), bounds[0].__class__.__name__
        assert isinstance(bounds[1], numbers.Real), bounds[1].__class__.__name__
        assert bounds[0] < bounds[1], bounds
        assert isinstance(isfinite, bool), isfinite.__class__.__name__
        self.edit = edit
        self.edit.ref.append(self)
        self.state = state
        self.bounds = bounds
        self.isfinite = isfinite
        self.textbox = QtWidgets.QLineEdit(edit)

    def __call__(self, grid_layout: QtWidgets.QGridLayout, ref_span=0):
        """
        ** Displays and allows to modify the number field. **
        """
        assert isinstance(grid_layout, QtWidgets.QGridLayout), grid_layout.__class__.__name__
        grid_layout.addWidget(
            QtWidgets.QLabel(
                f"{self.state.replace('_', ' ').title()} "
                f"({self.bounds[0]} {'<=' if math.isfinite(self.bounds[0]) else '<'} "
                "number "
                f"{'<=' if math.isfinite(self.bounds[1]) else '<'} {self.bounds[1]}):",
                self.edit,
            )
        )
        self.textbox.setText(str(self.edit.state[self.state]))
        self.textbox.textChanged.connect(self.validate)
        grid_layout.addWidget(self.textbox, ref_span, 1)
        return ref_span + 1

    def validate(self, text):
        """
        ** Check that the seed is a float in [0, 1[. **,
        """
        try:
            val = Fraction(text)
        except ZeroDivisionError:
            self.textbox.setStyleSheet("background:red;")
            return
        except ValueError:
            try:
                val = float(text)
            except ValueError:
                self.textbox.setStyleSheet("background:red;")
                return
        if val < self.bounds[0] or val > self.bounds[1]:
            self.textbox.setStyleSheet("background:red;")
            return
        if self.isfinite and not math.isfinite(val):
            self.textbox.setStyleSheet("background:red;")
            return

        self.edit.try_set_state(self.edit.get_new_state({self.state: val}), self.textbox)


class Seedable:
    """
    ** Allows to manage a `seed` field. **

    It is a float between [0, 1[.
    """

    def __init__(self, edit: EditBase):
        assert isinstance(edit, EditBase), edit.__class__.__name__
        assert "seed" in edit.state, sorted(edit.state)
        self.edit = edit
        self.edit.ref.append(self)
        self.textbox = QtWidgets.QLineEdit(edit)

    def __call__(self, grid_layout: QtWidgets.QGridLayout, ref_span=0):
        """
        ** Displays and allows to modify the seed field. **
        """
        assert isinstance(grid_layout, QtWidgets.QGridLayout), grid_layout.__class__.__name__
        grid_layout.addWidget(QtWidgets.QLabel("Seed (0 <= float < 1):", self.edit))
        self.textbox.setText(str(self.edit.state["seed"]))
        self.textbox.textChanged.connect(self.validate)
        grid_layout.addWidget(self.textbox, ref_span, 1)
        return ref_span + 1

    def validate(self, text):
        """
        ** Check that the seed is a float in [0, 1[. **,
        """
        try:
            seed = float(text)
        except ValueError:
            self.textbox.setStyleSheet("background:red;")
            return
        if seed < 0 or seed >= 1:
            self.textbox.setStyleSheet("background:red;")
            return

        self.edit.try_set_state(self.edit.get_new_state({"seed": seed}), self.textbox)

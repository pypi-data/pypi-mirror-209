# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`rotary_slider`
================================================================================

Displayio Layout Rotary Slider Widget


* Author(s): Jose D. Montoya


"""

import math
import displayio
from adafruit_display_shapes.roundrect import RoundRect
from bitmaptools import draw_circle
from vectorio import Circle
from adafruit_displayio_layout.widgets.widget import Widget
from adafruit_displayio_layout.widgets.control import Control

try:
    from typing import Tuple
except ImportError:
    pass


__version__ = "0.1.0"
__repo__ = "https://github.com/jposada202020/CircuitPython_Rotary_Slider.git"


class Slider(Widget, Control):
    """

    :param int x: pixel position, defaults to 0
    :param int y: pixel position, defaults to 0

    :param int radius: radius of the rotary slider in pixels. It is recommended to use 100

    :param int touch_padding: the width of an additional border surrounding the switch
     that extends the touch response boundary. Defaults to :const:`0`

    :param anchor_point: starting point for the annotation line, where ``anchor_point`` is
     an (A,B) tuple in relative units of the size of the widget, for example (0.0, 0.0) is
     the upper left corner, and (1.0, 1.0) is the lower right corner of the widget.
     If :attr:`anchor_point` is `None`, then :attr:`anchored_position` is used to set the
     annotation line starting point, in widget size relative units.
     Defaults to :const:`(0.0, 0.0)`
    :type anchor_point: Tuple[float, float]

    :param anchored_position: pixel position starting point for the annotation line
     where :attr:`anchored_position` is an (x,y) tuple in pixel units relative to the
     upper left corner of the widget, in pixel units (default is None).
    :type anchored_position: Tuple[int, int]


    **Quickstart: Importing and using RotarySlider**

    Here is one way of importing the `Slider` class so you can use it as
    the name ``Slider``:

    .. code-block:: python

        from rotary_slider import Slider

    Now you can create a Rotary Slider at pixel position x=20, y=30 using:

    .. code-block:: python

        my_slider=Slider(x=20, y=30)

    Once your setup your display, you can now add ``my_slider`` to your display using:

    .. code-block:: python

        display.show(my_slider) # add the group to the display

    If you want to have multiple display elements, you can create a group and then
    append the slider and the other elements to the group.  Then, you can add the full
    group to the display as in this example:

    .. code-block:: python

        my_slider= Slider(20, 30)
        my_group = displayio.Group() # make a group
        my_group.append(my_slider) # Add my_slider to the group

        #
        # Append other display elements to the group
        #

        display.show(my_group) # add the group to the display


    **Summary: Slider Features and input variables**

    The ``Slider`` widget has some options for controlling its position, visible appearance,
    and value through a collection of input variables:

        - **position**: :const:`x`, ``y`` or ``anchor_point`` and ``anchored_position``

        - **size**: :const:`radius`

        - **knob color**: :const:`fill_color`, :const:`outline_color`

        - **background color**: :const:`background_color`

        - **touch boundaries**: :attr:`touch_padding` defines the number of additional pixels
          surrounding the switch that should respond to a touch.  (Note: The ``touch_padding``
          variable updates the ``touch_boundary`` Control class variable.  The definition of
          the ``touch_boundary`` is used to determine the region on the Widget that returns
          `True` in the `when_inside` function.)



    """

    # pylint: disable=too-many-instance-attributes, too-many-arguments, too-many-locals
    # pylint: disable=too-many-branches, too-many-statements
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        radius: int = 50,
        touch_padding: int = 0,
        anchor_point: Tuple[int, int] = None,
        anchored_position: Tuple[int, int] = None,
        fill_color: Tuple[int, int, int] = (66, 44, 66),
        outline_color: Tuple[int, int, int] = (30, 30, 30),
        background_color: Tuple[int, int, int] = (255, 0, 0),
        line_color: Tuple[int, int, int] = (255, 255, 255),
    ):

        Widget.__init__(self, x=x, y=y, height=radius * 2, width=radius * 2)
        Control.__init__(self)
        self._x = x
        self._y = y
        self.radius = radius
        self._knob_width = 15
        self._knob_height = 15

        self._height = self.height

        self._fill_color = fill_color
        self._outline_color = outline_color
        self._background_color = background_color
        self._line_color = line_color

        self._switch_stroke = 2

        self._touch_padding = touch_padding

        self._anchor_point = anchor_point
        self._anchored_position = anchored_position

        self._create_slider()

    def _create_slider(self):

        self._palette = displayio.Palette(3)
        self._palette.make_transparent(0)
        self._palette[1] = self._line_color
        self._palette[2] = self._background_color

        self.dial_bitmap = displayio.Bitmap(2 * self.radius + 1, 2 * self.radius + 1, 3)
        self._frame = displayio.TileGrid(
            self.dial_bitmap,
            pixel_shader=self._palette,
            x=0,
            y=0,
        )
        draw_circle(self.dial_bitmap, self.radius, self.radius, self.radius, 1)
        self._circle_inside = Circle(
            pixel_shader=self._palette,
            radius=self.radius - 1,
            x=self.radius,
            y=self.radius,
            color_index=2,
        )

        self._knob_handle = RoundRect(
            x=-self._knob_width // 2,
            y=self.radius - self._knob_height // 2,
            width=self._knob_width,
            height=self._knob_height,
            r=4,
            fill=self._fill_color,
            outline=self._outline_color,
            stroke=self._switch_stroke,
        )

        self._bounding_box = [
            0,
            0,
            2 * self.radius,
            2 * self.radius,
        ]

        self.touch_boundary = [
            self._bounding_box[0] - self._touch_padding,
            self._bounding_box[1] - self._touch_padding,
            self._bounding_box[2] + 2 * self._touch_padding,
            self._bounding_box[3] + 2 * self._touch_padding,
        ]

        for _ in range(len(self)):
            self.pop()

        self.append(self._frame)
        self.append(self._circle_inside)
        self.append(self._knob_handle)

    def when_selected(self, touch_point):
        """
        Manages internal logic when widget is selected
        """

        if touch_point[0] <= self.x + self._knob_width:
            touch_x = touch_point[0] - self.x
        else:
            touch_x = touch_point[0] - self.x - self._knob_width

        touch_y = touch_point[1] - self.y

        self.selected((touch_x, touch_y, 0))

        angle = math.atan2((touch_y - self.radius), (touch_x - self.radius))

        self._knob_handle.x = (
            self.radius
            + math.ceil(self.radius * math.cos(angle))
            - self._knob_width // 2
        )
        self._knob_handle.y = (
            self.radius
            + math.ceil(self.radius * math.sin(angle))
            - self._knob_height // 2
        )

        return self._knob_handle.x, self._knob_handle.y

    def when_inside(self, touch_point):
        """Checks if the Widget was touched.

        :param touch_point: x,y location of the screen, in absolute display coordinates.
        :return: Boolean

        """
        touch_x = (
            touch_point[0] - self.x
        )  # adjust touch position for the local position
        touch_y = touch_point[1] - self.y

        return self.contains((touch_x, touch_y, 0))

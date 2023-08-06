# SPDX-FileCopyrightText: Copyright (c) 2021, 2023 Jose David M.
#
# SPDX-License-Identifier: MIT
"""

`scales`
================================================================================

Allows display data in a graduated level


* Author(s): Jose David M.

Implementation Notes
--------------------

Scales version in CircuitPython

"""

################################
# A scales library for CircuitPython, using `displayio`` and `vectorio``
#
# Features:
#  - Vertical and Horizontal direction
#  - Animation to use with different sensor

try:
    from typing import Union, Tuple, Optional
except ImportError:
    pass

import displayio
import terminalio
from adafruit_display_text.bitmap_label import Label
from vectorio import Polygon, Rectangle
import ulab.numpy as np

try:
    from typing import Tuple
except ImportError:
    pass

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/jposada202020/CircuitPython_scales.git"

# pylint: disable=too-many-arguments, too-few-public-methods,too-many-instance-attributes
# pylint: disable=invalid-unary-operand-type
class Axes(displayio.Group):
    """
    :param int x: pixel position. Defaults to :const:`0`
    :param int y: pixel position. Defaults to :const:`0`

    :param int,int limits: tuple of value range for the scale. Defaults to (0, 100)
    :param list ticks: list to ticks to display. If this is not enter a equally spaced scale
     will be created between the given limits.

    :param str direction: direction of the scale either :attr:`horizontal` or :attr:`vertical`
     defaults to :attr:`horizontal`

    :param int stroke: width in pixels of the scale axes. Defaults to :const:`3`

    :param int length: scale length in pixels. Defaults to :const:`100`

    :param int color: 24-bit hex value axes line color, Defaults to Purple :const:`0x990099`

    """

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        limits: Tuple[int, int] = (0, 100),
        ticks: Optional[Union[np.array, list]] = None,
        direction: str = "horizontal",
        stroke: int = 3,
        length: int = 100,
        color: int = 0x990099,
    ):

        super().__init__()

        if direction == "horizontal":
            self.direction = True
        else:
            self.direction = False

        self.x = x
        self.y = y
        self.limits = limits

        self._valuemin = limits[0]
        self._valuemax = limits[1]
        self._newvalmin = length
        self._newvalmax = 0

        self.stroke = stroke
        self.length = length

        if ticks:
            self.ticks = np.array(ticks)
        else:
            self.ticks = np.array(list(range(self._valuemin, self._valuemax, 10)))

        self.ticksynorm = np.array(
            transform(
                self._valuemin,
                self._valuemax,
                self._newvalmax,
                self._newvalmin,
                self.ticks,
            ),
            dtype=np.int16,
        )

        self._palette = displayio.Palette(2)
        self._palette.make_transparent(0)
        self._palette[1] = color

        self._tick_length = None
        self._tick_stroke = None

        self.text_ticks = []

    def _draw_line(self) -> None:
        """Private function to draw the Axe.
        :return: None
        """
        if self.direction:
            self.append(rectangle_draw(0, 0, self.stroke, self.length, self._palette))
        else:
            self.append(
                rectangle_draw(0, -self.length, self.length, self.stroke, self._palette)
            )

    def _draw_ticks(self, tick_length: int = 10, tick_stroke: int = 4) -> None:
        """Private function to draw the ticks
        :param int tick_length: tick length in pixels
        :param int tick_stroke: tick thickness in pixels
        :return: None
        """

        self._tick_length = tick_length
        self._tick_stroke = tick_stroke

        if self.direction:
            for val in self.ticksynorm[:-1]:
                self.append(
                    rectangle_draw(
                        int(val) - 1,
                        -self._tick_length,
                        self._tick_length,
                        3,
                        self._palette,
                    )
                )
        else:
            for val in self.ticksynorm[:-1]:
                self.append(
                    rectangle_draw(0, -int(val), 3, self._tick_length, self._palette)
                )

    def _draw_text(self) -> None:
        """Private function to draw the text, uses values found in ``_conversion``
        :return: None
        """
        index = 0
        separation = 20
        font_width = 12
        if self.direction:
            print("aca")
            for tick_text in self.ticks[:-1]:
                dist_x = self.ticksynorm[index] - font_width // 2
                dist_y = separation // 2
                text = str(int(tick_text))
                tick_label = Label(terminalio.FONT, text=text, x=dist_x, y=dist_y)
                self.append(tick_label)
                index = index + 1
        else:
            for tick_text in self.ticks[:-1]:
                dist_x = -separation
                dist_y = -self.ticksynorm[index]
                text = str(int(tick_text))
                tick_label = Label(terminalio.FONT, text=text, x=dist_x, y=dist_y)
                self.append(tick_label)
                index = index + 1


class Scale(Axes):
    """
    :param int x: pixel position. Defaults to :const:`0`
    :param int y: pixel position. Defaults to :const:`0`

    :param str direction: direction of the scale either :attr:`horizontal` or :attr:`vertical`
     defaults to :attr:`horizontal`

    :param int stroke: width in pixels of the axes line. Defaults to :const:`3` pixels

    :param int length: scale length in pixels. Defaults to :const:`100` pixels

    :param int color: 24-bit hex value axes line color, Defaults to Purple :const:`0x990099`

    :param int width: scale width in pixels. Defaults to :const:`50` pixels

    :param limits: tuple of value range for the scale. Defaults to :const:`(0, 100)`
    :param list ticks: list to ticks to display. If this is not enter a equally spaced scale
     will be created between the given limits.

    :param int back_color: 24-bit hex value axes line color.
     Defaults to Light Blue :const:`0x9FFFFF`

    :param int tick_length: Scale tick length in pixels. Defaults to :const:`10`
    :param int tick_stroke: Scale tick width in pixels. Defaults to :const:`4`

    :param int pointer_length: length in pixels for the point. Defaults to :const:`20` pixels
    :param int pointer_stroke: pointer thickness in pixels. Defaults to :const:`6` pixels


    **Quickstart: Importing and using Scales**

    Here is one way of importing the `Scale` class, so you can use it as
    the name ``my_scale``:

    .. code-block::

        from scale import Scale

    Now you can create a vertical Scale at pixel position x=50, y=180 and a range
    of 0 to 80 using:

    .. code-block::

        my_scale = Scale(x=50, y=180, direction="vertical", limits=(0, 80))

    Once you setup your display, you can now add ``my_scale`` to your display using:

    .. code-block::

        display.show(my_scale)

    If you want to have multiple display elements, you can create a group and then
    append the scale and the other elements to the group. Then, you can add the full
    group to the display as in this example:

    .. code-block:: python

        my_scale= Scale(x=20, y=30)
        my_group = displayio.Group() # make a group
        my_group.append(my_scale) # Add my_slider to the group

        #
        # Append other display elements to the group
        #

        display.show(my_group) # add the group to the display


    **Summary: Slider Features and input variables**

    The `Scale` class has some options for controlling its position, visible appearance,
    and value through a collection of input variables:

        - **position**: :attr:`x``, :attr:`y`

        - **size**: :attr:`length` and :attr:`width`

        - **color**: :attr:`color`, :attr:`back_color`

        - **linewidths**: :attr:`stroke` and :attr:`tick_stroke`

        - **range**: :attr:`limits`


    .. figure:: scales.png
      :scale: 100 %
      :align: center
      :alt: Diagram of scales

      Diagram showing a simple scale.


    """

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        direction: str = "horizontal",
        stroke: int = 3,
        length: int = 100,
        color: int = 0x990099,
        width: int = 50,
        limits: Tuple[int, int] = (0, 100),
        back_color: int = 0x9FFFFF,
        ticks: Optional[Union[np.array, list]] = None,
        tick_length: int = 5,
        tick_stroke: int = 4,
        pointer_length: int = 20,
        pointer_stroke: int = 6,
    ):

        super().__init__(
            x=x,
            y=y,
            direction=direction,
            stroke=stroke,
            length=length,
            limits=limits,
            ticks=ticks,
            color=color,
        )

        self._width = width
        self._back_color = back_color
        self._draw_background()
        self._draw_line()
        self._draw_ticks()
        self.value = 0

        self._tick_length = tick_length
        self._tick_stroke = tick_stroke
        self._pointer_length = pointer_length
        self._pointer_stroke = pointer_stroke

        # Pointer Definitions
        self._x0 = 0
        self._y0 = 0

        if self.direction:
            self.center = width // 2
            self._x1 = pointer_stroke
            self._y1 = pointer_length
            self._posx = 0
            self._posy = -self.center - self._pointer_length // 2
        else:
            self.center = width // 2
            self._x1 = pointer_length
            self._y1 = pointer_stroke
            self._posx = self.center - self._pointer_length // 2
            self._posy = -10
        self.pointer = None

        self._draw_text()
        self._draw_pointer()

    def _draw_background(self):
        """Private function to draw the background for the scale
        :return: None
        """
        back_palette = displayio.Palette(2)
        back_palette.make_transparent(0)
        back_palette[1] = self._back_color

        if self.direction:
            self.append(
                rectangle_draw(0, -self._width, self._width, self.length, back_palette)
            )
        else:
            self.append(
                rectangle_draw(0, -self.length, self.length, self._width, back_palette)
            )

    def _draw_pointer(
        self,
        color: int = 0xFF0000,
    ):
        """Private function to initial draw the pointer.

        :param int color: 24-bit hex value axes line color. Defaults to red :const:`0xFF0000`
        :param int val_ini: initial value to draw the pointer


        :return: None

        """

        pointer_palette = displayio.Palette(2)
        pointer_palette.make_transparent(0)
        pointer_palette[1] = color

        points = [
            (self._x0, self._y0),
            (self._x1, self._y0),
            (self._x1, self._y1),
            (self._x0, self._y1),
        ]
        self.pointer = Polygon(
            pixel_shader=pointer_palette,
            points=points,
            x=self._posx,
            y=self._posy,
            color_index=1,
        )

        self.append(self.pointer)

    def animate_pointer(self, new_value):
        """Public function to animate the pointer

        :param new_value: value to draw the pointer
        :return: None

        """
        value = int(
            transform(
                self._valuemin,
                self._valuemax,
                self._newvalmax,
                self._newvalmin,
                new_value,
            )
        )
        if self.direction:
            self.pointer.x = value - self._pointer_stroke // 2
        else:
            self.pointer.y = -value - self._pointer_stroke // 2


# pylint: disable=invalid-name
def rectangle_draw(x0: int, y0: int, height: int, width: int, palette):
    """rectangle_draw function

    Draws a rectangle using or `vectorio.Rectangle`

    :param int x0: rectangle lower corner x position
    :param int y0: rectangle lower corner y position

    :param int width: rectangle upper corner x position
    :param int height: rectangle upper corner y position

    :param `~displayio.Palette` palette: palette object to be used to draw the rectangle

    """

    return Rectangle(
        pixel_shader=palette, width=width, height=height, x=x0, y=y0, color_index=1
    )


def transform(
    oldrangemin: Union[float, int],
    oldrangemax: Union[float, int],
    newrangemin: Union[float, int],
    newrangemax: Union[float, int],
    value: Union[float, int],
) -> Union[float, int]:
    """
    This function converts the original value into a new defined value in the new range

    :param int|float oldrangemin: minimum of the original range
    :param int|float oldrangemax: maximum of the original range
    :param int|float newrangemin: minimum of the new range
    :param int|float newrangemax: maximum of the new range
    :param int|float value: value to be converted

    :return int|float: converted value

    """

    return (
        ((value - oldrangemin) * (newrangemax - newrangemin))
        / (oldrangemax - oldrangemin)
    ) + newrangemin

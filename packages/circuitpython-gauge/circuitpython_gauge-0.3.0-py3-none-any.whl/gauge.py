# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya for Jose D.
#
# SPDX-License-Identifier: MIT
"""
`gauge`
================================================================================

CircuitPython Gauge


* Author(s): Jose D. Montoya

Implementation Notes
--------------------


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads


"""

try:
    from typing import Union, Tuple, Optional
except ImportError:
    pass

from bitmaptools import draw_polygon, draw_line
import displayio
import terminalio
from vectorio import Polygon
from ulab import numpy as np

__version__ = "0.3.0"
__repo__ = "https://github.com/jposada202020/CircuitPython_Gauge.git"

# pylint: disable=too-many-arguments, too-many-instance-attributes, too-many-locals
# pylint: disable=too-many-statements, unnecessary-comprehension
# pylint: disable=unused-import, import-outside-toplevel, undefined-variable
# pylint: disable=invalid-name, dangerous-default-value


class gauge(displayio.Group):
    """
    scales Class to add different elements to the screen.
    The origin point set by ``x`` and ``y`` properties

    :param int x: origin x coordinate. Defaults to 0.
    :param int y: origin y coordinate. Defaults to 0.
    :param int width: plot box width in pixels. Defaults to 100.
    :param int length: plot box height in pixels. Defaults to 100.
    :param int padding: padding for the scale box in all directions
    :param list|None scale_range: x range limits. Defaults to None

    :param int background_color: background color in HEX. Defaults to black ``0x000000``
    :param int box_color: allows to choose the box line color. Defaults to white ''0xFFFFFF``

    :param np.array|list ticks: axis ticks values
    :param int tick_lenght: x axes tick height in pixels. Defaults to 28.
    :param int tick_color: x axes tick height in pixels. Defaults to 0xFFFFFF.
    :param str|None tick_pos: Argument to locate the ticks. Left, center or all
    :param int pointer_lenght: width of the bar. Defaults to 10.
    :param int scale: scale of the widget

    :param str direction: direction of the scale either :attr:`horizontal` or :attr:`Vertical`
     defaults to :attr:`Vertical`

    """

    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 100,
        length: int = 100,
        padding: int = 0,
        scale_range: Optional[list] = [0, 150],
        background_color: int = 0x000000,
        box_color: int = 0xFF8500,
        ticks: Optional[Union[np.array, list]] = None,
        tick_lenght: int = 28,
        tick_color: int = 0xFFFFFF,
        tick_color_threshold: int = 0xFF0000,
        tick_pos: Optional[str] = None,
        pointer_lenght: int = 10,
        scale: int = 1,
        show_text: bool = False,
        text_format: Optional[str] = None,
        direction: str = "Vertical",
    ) -> None:
        super().__init__(x=x, y=y, scale=scale)
        self.padding = padding
        if direction == "Vertical":
            self.direction = True
            self._width = width
            self._length = length
            self._newvaluemin = self._length - self.padding
            self._newvaluemax = self.padding
            self._newxmin = self.padding
            self._newxmax = self._width - self.padding
        else:
            self.direction = False
            self._width = length
            self._length = width
            self._newvaluemin = self.padding
            self._newvaluemax = self._width - self.padding
            self._newxmin = self.padding
            self._newxmax = self._length - self.padding

        self._plotbitmap = displayio.Bitmap(self._width + 1, self._length + 1, 6)

        # Box Points
        self._boxpos_x0 = self.padding
        self._boxpos_y0 = self.padding
        self._boxpos_x1 = self._width - self.padding
        self._boxpos_y1 = self._length - self.padding

        self._valuemin = scale_range[0]
        self._valuemax = scale_range[1]

        if ticks:
            self.ticks = np.array(ticks)
        else:
            self.ticks = np.array(list(range(self._valuemin, self._valuemax, 10)))

        self._showtext = show_text

        self._tickcolor = tick_color
        self._tick_color_threshold = tick_color_threshold
        self._pointer_palette = displayio.Palette(3)
        self._pointer_palette.make_transparent(0)
        self._pointer_palette[1] = self._tickcolor
        self._pointer_palette[2] = self._tick_color_threshold
        self.pointer = None
        self._pointer_length = pointer_lenght
        self._tick_length = tick_lenght

        self.value = 0
        self.threshold = 0

        self._showticks = True

        if text_format == "float":
            self._text_format = True
        else:
            self._text_format = False

        self._plot_palette = displayio.Palette(6)
        self._plot_palette[0] = background_color
        self._plot_palette[1] = box_color
        self._plot_palette[2] = self._tickcolor

        self.points = None

        if self.direction:
            self._center = (self._newxmax - self._newxmin) // 2
            self.x0 = self._center - self._pointer_length // 2 + 2 * self.padding
            self.y0 = self._newvaluemin
            self.x1 = self._center + self._pointer_length // 2
            self.y1 = self._newvaluemin - self.value
        else:
            self._center = (self._newxmax - self._newxmin) // 2
            self.x0 = self._boxpos_x0 + self.padding
            self.y0 = self._center - self._pointer_length // 2
            self.x1 = self._boxpos_x0 + self.value
            self.y1 = self._center + self._pointer_length // 2

        if tick_pos == "left":
            self._tickpos = self._newxmin
        elif tick_pos == "center":
            self._tickpos = self._center - self._tick_length // 2
        else:
            self._tickpos = self._newxmin
            self._tick_length = self._width

        self.append(
            displayio.TileGrid(
                self._plotbitmap, pixel_shader=self._plot_palette, x=0, y=0
            )
        )
        self._draw_ticks()
        self._draw_pointer()
        self._drawbox()

    def _drawbox(self) -> None:
        """
        Draw the plot box

        :return: None

        """
        xs = bytes([self._boxpos_x0, self._boxpos_x0, self._boxpos_x1, self._boxpos_x1])
        ys = bytes([self._boxpos_y0, self._boxpos_y1, self._boxpos_y1, self._boxpos_y0])
        draw_polygon(self._plotbitmap, xs, ys, 1)

    @staticmethod
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

    def _draw_ticks(self) -> None:
        """
        Draw ticks in the plot area

        """

        ticksnorm = np.array(
            self.transform(
                self._valuemin,
                self._valuemax,
                self._newvaluemin,
                self._newvaluemax,
                self.ticks,
            ),
            dtype=np.int16,
        )
        if self.direction:
            for i, tick in enumerate(ticksnorm):
                draw_line(
                    self._plotbitmap,
                    self._newxmin + self._tickpos,
                    tick,
                    self._newxmin + self._tick_length + self._tickpos,
                    tick,
                    2,
                )
                if self._showtext:
                    if self._text_format:
                        self.show_text(
                            "{:.2f}".format(self.ticks[i]),
                            self._newxmin,
                            tick,
                            (1.0, 0.5),
                        )
                    else:
                        self.show_text(
                            "{:d}".format(int(self.ticks[i])),
                            self._newxmin,
                            tick,
                            (1.0, 0.5),
                        )
        else:
            for i, tick in enumerate(ticksnorm):
                draw_line(
                    self._plotbitmap,
                    self._boxpos_x0 + tick,
                    self._boxpos_y0 + self._tickpos,
                    self._boxpos_x0 + tick,
                    self._boxpos_y0 + self._tick_length + self._tickpos,
                    2,
                )
                if self._showtext:
                    if self._text_format:
                        self.show_text(
                            "{:.2f}".format(self.ticks[i]),
                            tick,
                            self._boxpos_y1,
                            (0.5, 0.0),
                        )
                    else:
                        self.show_text(
                            "{:d}".format(int(self.ticks[i])),
                            tick,
                            self._boxpos_y1,
                            (0.5, 0.0),
                        )

    def show_text(
        self, text: str, x: int, y: int, anchorpoint: Tuple = (0.5, 0.0)
    ) -> None:
        """

        Show desired text in the screen
        :param str text: text to be displayed
        :param int x: x coordinate
        :param int y: y coordinate
        :param Tuple anchorpoint: Display_text anchor point. Defaults to (0.5, 0.0)
        :return: None
        """
        if self._showtext:
            from adafruit_display_text import bitmap_label

            text_toplot = bitmap_label.Label(terminalio.FONT, text=text, x=x, y=y)
            text_toplot.anchor_point = anchorpoint
            text_toplot.anchored_position = (x, y)
            self.append(text_toplot)

    def _draw_pointer(self):
        self.points = [
            (self.x0, self.y0),
            (self.x1, self.y0),
            (self.x1, self.y1),
            (self.x0, self.y1),
        ]

        self.pointer = Polygon(
            pixel_shader=self._pointer_palette,
            points=self.points,
            x=0,
            y=0,
            color_index=1,
        )
        self.append(self.pointer)

    def update(self, new_value):
        """
        Function to update gauge value

        :param new_value: value to be updated
        :return: None

        """

        if self.direction:
            self.value = int(
                self.transform(
                    self._valuemin,
                    self._valuemax,
                    self._newvaluemax,
                    self._newvaluemin,
                    new_value,
                )
            )
            if self.value >= self._newvaluemin:
                self.value = self._newvaluemin
            self.y1 = self._newvaluemin - self.value
        else:
            self.value = int(
                self.transform(
                    self._valuemin,
                    self._valuemax,
                    self._newvaluemin,
                    self._newvaluemax,
                    new_value,
                )
            )
            self.x1 = self._newvaluemin + self.value
        self.points = [
            (self.x0, self.y0),
            (self.x1, self.y0),
            (self.x1, self.y1),
            (self.x0, self.y1),
        ]

        if self.value > self.threshold:
            self.pointer.color_index = 2
        else:
            self.pointer.color_index = 1
        self.pointer.points = self.points

    def set_threshold(self, value: int, color: int = 0xFF0000) -> None:
        """
        Defines the threshold for the gage to change color
        :param value: value that will trigger the change
        :param color: color to change into. Defaults to red :const:`0xFF0000`
        :return: None
        """
        self._pointer_palette[2] = color
        self.threshold = value

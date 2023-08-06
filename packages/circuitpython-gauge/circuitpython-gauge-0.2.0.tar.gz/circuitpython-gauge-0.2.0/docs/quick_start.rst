A small tour around gauge.

Gauge Usage
=============
We start importing some fundamental libraries for gauge to operate

.. code-block:: python

    import board
    import displayio
    from gauge import gauge

For reference, screen in CircuitPython are defined from left to right and up to bottom. This means
that our (x=0, y=0) will be in the left upper corner of the screen.
For boards or feather with a integrated screen the following statement will initiate the screen

.. code-block:: python

    display = board.DISPLAY

For other displays please consult the right support library

.. code-block:: python

    my_gauge = gauge(0, 0, 28, 50)

The position and the size of the gauge area
could vary. This allows us to have more than 1 gauge at the same time in the screen.
Every one of them with different characteristics or graphs.

Size and Location
=================

Options available are:
    * x, y : coordinates in the display to locate the gauge.
    * width: width of the plot area
    * height: height of the plot area


Range
=================

scale_range allows you to select the gauge range. The gauge library will automatically calculate the correct spacing according to the
gauge dimensions given.

.. code-block:: python

    my_gauge = gauge(0, 0, 28, 50, scale_range=[0, 120])

scale range argument take a list of ints as input. In the code above, 0 will be the lower limit and 120 the upper limit.
There are no special verifications in the library for wrong ranges, so the user is responsible to put the right numbers.


Gauge Box
=================
The gauge has some parameters that can be change:

    * box_color: changes the color of the box
    * background_color: changes the box background color


.. code-block:: python

    my_gauge = gauge(0, 0, 28, 50, box_color=0x00FF00, background_color=0xFF00FF)


Ticks
=================
Ticks are easily customisable. you ahve the following options

    * ticks: if needed, you could use your own ticks to display. If this value is not given, tha library will calculate this for you.
    * tick_position: tick position in the box. Ticks could be ``left``, ``center`` or from left to right
    * tick_lenght: tick length. This option is only avalaible for tick_position ``left`` and ``center``
    * tick_color: tick color

.. code-block:: python

    my_gauge = gauge(0, 0, 28, 50, ticks=[10, 25, 75, 90], tick_pos="left", tick_lenght=10, tick_color=0x440044)

Text
=================
Is easy to use text in your gauges. The library uses the bitmap_label to save memory. And it is onnly loaded if the option to show text is selected.

    * Show text: allows to show tick text in the gauge
    * text_format: indicates to the library if the numbers are to be shown as integers or floats. Integer is the default behaviour.


.. code-block:: python

    my_gauge = gauge(0, 0, 28, 50, show_text=True, text_format="float")

Other Parameters
=================

        * pointer_lenght: width of the central bar.
        * scale: scale of the gauge.

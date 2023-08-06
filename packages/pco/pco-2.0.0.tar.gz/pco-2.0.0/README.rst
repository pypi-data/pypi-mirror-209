
.. image:: https://www.pco.de/fileadmin/user_upload/company/pco_logo.png
   :width: 100pt

|PyPI-Versions| |LICENCE| |Platform| |PyPI-Status|

The Python package **pco** offers all functions for working with pco cameras that are based
on the current SDK. All shared libraries for the communication with the
camera and subsequent image processing are included.

- Easy to use camera class
- Powerful API to `pco.software development kit <https://www.pco.de/fileadmin/user_upload/pco-manuals/pco.sdk_manual.pdf>`_
- Image recording and processing with `pco.recorder <https://www.pco.de/fileadmin/fileadmin/user_upload/pco-manuals/pco.recorder_manual.pdf>`_

Installation
============
Install from pypi (recommended)::

    $ pip install pco

Basic Usage
===========
.. code-block:: python

    import pco
    import matplotlib.pyplot as plt

    with pco.Camera() as cam:

        cam.record()
        image, meta = cam.image()

        plt.imshow(image, cmap='gray')
        plt.show()

.. image:: https://www.pco.de/fileadmin/user_upload/company/screen.png

Logging
=======

Logging is implemented according to the python logging package (https://docs.python.org/3/library/logging.html).
Supported logging levels are:
- `ERROR`
- `WARNING`
- `INFO`
- `DEBUG`


.. code-block:: python

    logger = logging.getLogger("pco")
    logger.setLevel(logging.INFO)
    logger.addHandler(pco.stream_handler)



.. code-block:: python

    ...
    [][sdk] get_camera_type: OK.
    ...
    [2019-11-25 15:54:15.317855 / 0.016 s] [][sdk] get_camera_type: OK.


Documentation
=============

The pco.Camera class offers the following methods:

- ``__init()__`` Opens and initializes a camera with its default configuration
- ``__exit()__`` Closes the camera and cleans up everything (e.g. end of with-statement)
- ``default_configuration()`` Set default configuration to the camera
- `record()`_ Initialize and start the recording of images
- `stop()`_ Stop the current recording
- `close()`_ Closes the camera and cleans up everything
- `wait_for_first_image()`_ Wait until the first image has been recorded
- `wait_for_new_image()`_ Wait until a new image has been recorded
- ``get_convert_control()`` Get current color convert settings
- ``set_convert_control()`` Set new color convert settings
- ``load_lut()`` Set the lut file for the convert control setting
- ``adapt_white_balance()`` Do a white-balance according to a transferred image
- `image()`_ Read a recorded image as numpy array
- `images()`_ Read a series of recorded images as a list of numpy arrays.
- `image_average()`_ Read an averaged image (averaged over all recorded images) as numpy array.

The pco.Camera class has the following properties:

- ``camera_name`` gets the camera name
- ``camera_serial`` gets the serial number of the camera
- ``is_recording`` gets a flag to indicate if the camera is currently recording
- ``is_color`` gets a flag to indicate if the camera is a color camera
- ``recorded_image_count`` gets the number of currently recorded images
- ``configuration`` gets/sets the camera configuration
- ``description`` gets the (static) camera description parameters
- ``exposure_time`` gets/sets the exposure time (in seconds)
- ``delay_time`` gets/sets the delay time (in seconds)

The pco.Camera class holds the following objects:

- `sdk`_ offers direct access to all underlying functions of the pco.sdk.
- `rec`_ offers direct access to all underlying functions of the pco.recorder.
- `conv`_ offers direct access to all underlying functions of the pco.convert according to the selected data_format.

.. ---------------------------------------------------------------------------

record()
--------

Creates, configures and starts a new recorder instance.

.. code-block:: python

    def record(self, number_of_images=1, mode='sequence', file_path=None):

- ``number_of_images`` sets the number of images allocated in the driver. The RAM of the PC is limiting the maximum value.

- ``mode`` sets the type of recorder.

.. list-table:: record modes
  :widths: 20 10 10 60
  :header-rows: 1

  * - Mode
    - Storage
    - Blocking
    - Description
  
  * - ``sequence``
    - Memory
    - yes
    - Record a sequence of images
  
  * - ``sequence non blocking``
    - Memory
    - no 
    - Record a sequence of images, do not wait until record is finished
  
  * - ``ring buffer``
    - Memory
    - no 
    - Continuously record images in a ringbuffer, once the buffer is full, old images are overwritten
  
  * - ``fifo``
    - Memory
    - no 
    - Record images in fifo mode, i.e. you will always read images sequentially and once the buffer is full, recording will pause until older images have been read
  
  * - ``sequence dpcore``
    - Memory
    - yes
    - Same as ``sequence``, but with DotPhoton preparation enabled
  
  * - ``sequence non blocking dpcore``
    - Memory
    - no 
    - Same as ``sequence_non_blocking``, but with DotPhoton preparation enabled
  
  * - ``ring buffer dpcore``
    - Memory
    - no 
    - Same as ``ring_buffer``, but with DotPhoton preparation enabled
  
  * - ``fifo dpcore``
    - Memory
    - no 
    - Same as ``fifo``, but with DotPhoton preparation enabled
  
  * - ``tif``
    - File  
    - no 
    - Record images directly as tif files  
  
  * - ``multitif``
    - File  
    - no 
    - Record images directly as one or more multitiff file()s 
  
  * - ``pcoraw``
    - File  
    - no 
    - Record images directly as one pcoraw file  
  
  * - ``dicom``
    - File  
    - no 
    - Record images directly as dicom files
  
  * - ``multidicom``
    - File  
    - no 
    - Record images directly as one or more multi-dicom file(s)

- ``file_path`` Path where the image file(s) should be stored (only for modes who directly save to file)

.. ---------------------------------------------------------------------------

stop()
------

Stops the current recording.

.. code-block:: python

    def stop(self):

In ``'ring buffer'`` and ``'fifo'`` mode this function must to be called by the user.
In ``'sequence'`` and ``'sequence non blocking'`` mode, this function is automatically called up
when the ``number_of_images`` is reached.


.. ---------------------------------------------------------------------------

close()
-------
.. code-block:: python

    def close(self):

Closes the activated camera and releases the blocked ressources.
This function must be called before the application is terminated.
Otherwise the resources remain occupied.

This function is called automatically, if the camera object is
created by the ``with`` statement. An explicit call to ``close()`` is no
longer necessary.

.. code-block:: python

    with pco.Camera() as cam:
        # do some stuff


.. ---------------------------------------------------------------------------

image()
-------

Returns an image from the recorder. The type of the image is a ``numpy.ndarray``.
This array is shaped depending on the resolution and ROI of the image.

.. code-block:: python

    def image(self, image_number=0, roi=None):

- ``image_number`` specifies the number of the image to read. In ``'sequence'`` or ``'sequence non blocking'`` mode the recorder
  index matches the image number.
  If ``image_number`` is set to ``0xFFFFFFFF`` the last recorded image is copied. This allows
  e.g. thumbnail while recording.

- ``roi`` sets the region fo interest. Only this region of the image is copied to the return value.

  .. code-block:: python

      >>> cam.record(number_of_images=1, mode='sequence')

      >>> image, meta = cam.image()

      >>> type(image)
      numpy.ndarray

      >>> image.shape
      (2160, 2560)

      >>> image, metadata = cam.image(roi=(1, 1, 300, 300))

      >>> image.shape
      (300, 300)

.. ---------------------------------------------------------------------------

images()
--------

Returns all recorded images from the recorder as list of numpy arrays.

.. code-block:: python

    def images(self, roi=None, blocksize=None):

- ``roi`` sets the region fo interest. Only this region of the image is copied to the return value.

- ``blocksize`` defines the maximum number of images that are returned.
  This parameter is only useful in ``'fifo'`` mode and under special conditions.

  .. code-block:: python

      >>> cam.record(number_of_images=20, mode='sequence')

      >>> images, metadatas = cam.images()

      >>> len(images)
      20

      >>> for image in images:
      ...     print('Mean: {:7.2f} DN'.format(image.mean()))
      ...
      Mean: 2147.64 DN
      Mean: 2144.61 DN
      ...

     >>> images = cam.images(roi=(1, 1, 300, 300))
     
     >>> images[0].shape
    (300, 300)

.. ---------------------------------------------------------------------------

image_average()
------------------------

Returns the averaged image. This image is calculated from all recorded images in the buffer.

.. code-block:: python

    def image_average(self, roi=None):

- ``roi`` defines the region fo interest. Only this region of the image is copied to the return value.

  .. code-block:: python

      >>> cam.record(number_of_images=100, mode='sequence')

      >>> avg = cam.image_average()

      >>> avg = cam.image_average(roi=(1, 1, 300, 300))


.. ---------------------------------------------------------------------------

wait_for_first_image()
-------------------------
Waits for the first available image in the recorder memory.

.. code-block:: python

    def wait_for_first_image(self, delay=True, timeout=None):


.. ---------------------------------------------------------------------------

wait_for_new_image()
-------------------------
Wait until a new image has been recorded and is available (i.e. an image that has not been read
yet).

.. code-block:: python

    def wait_for_new_image(self, delay=True, timeout=None):


.. ---------------------------------------------------------------------------

sdk
---
The object ``sdk`` allows direct access to all underlying functions of the pco.sdk.

.. code-block:: python

       >>> cam.sdk.get_temperature()
       {'sensor temperature': 7.0, 'camera temperature': 38.2, 'power temperature': 36.7}

All return values form ``sdk`` functions are dictionarys.
Not all camera settings are currently covered by the ``camera`` class.
Special settings have to be set directly  by calling the respective SDK function.

.. ---------------------------------------------------------------------------

rec
--------

The object ``rec`` offers direct access to all underlying functions of the pco.recorder.
It is not necessary to call a recorder class method directly. 
All functions are fully covered by the methods of the ``camera`` class.


.. ---------------------------------------------------------------------------

conv
--------

The object ``conv``  is a dictionary of convert objects to offer direct access to all
underlying functions of the pco.convert.
It is not necessary to call a ``conv`` class method directly. 
All functions are fully covered by the methods of the ``camera`` class.





.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/pco.svg
   :target: https://pypi.python.org/pypi/pco

.. |LICENCE| image:: https://img.shields.io/badge/License-MIT-green.svg
   :target: https://opensource.org/licenses/MIT

.. |Platform| image:: https://img.shields.io/badge/platform-win_x64%20%7C%20linux_x64-green.svg
   :target: https://pypi.python.org/pypi/pco
   
.. |PyPI-Status| image:: https://img.shields.io/pypi/v/pco.svg
  :target: https://pypi.python.org/pypi/pco


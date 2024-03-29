![PyPI](https://img.shields.io/pypi/v/web-mage?color=blue&label=PyPI%20version)
![PyPI - Downloads](https://img.shields.io/pypi/dm/web-mage?label=Downloads)

web-mage
========

web-mage is a simple Python package that's used to automate the process
of optimizing image files for the web. It can be imported and customized
in a Python module, or run simply as a command-line utility.

This project is functional, but still in early development.


Changelog can be found [here](https://github.com/c8bit/web-mage/wiki/Changelog).

Installation
------------

Install using `pip`:
```bash
pip install web-mage
```

Usage
-----

```bash
python3 -m web_mage SOURCE_DIR DEST_DIR
```

This will optimize all files in `SOURCE_DIR` to 60% quality with no image resizing,
and output them to `DEST_DIR` with a filename suffix.

Usage in Code
-------------

This is the preferred method of usage. You can import web-mage into
Python if you want to run jobs in a script or program, or customize
the way images are optimized.

```python
from web_mage.web_mage import Job
from web_mage.formats import IMG_FORMAT_CONTENT_LARGE

formats = [IMG_FORMAT_CONTENT_LARGE]
optim_job = Job(source="/path/to/source/directory",
                dest="/path/to/output/directory",
                formats=formats)
optim_job.run()
```

You can use multiple formats if you want images to be optimized for
multiple different devices or layouts. You can also define your own
image formats based on a few different parameters.

```python
from web_mage.formats import (ImageFormat,
                              IMG_FORMAT_CONTENT_LARGE,
                              IMG_FORMAT_CONTENT_MEDIUM,
                              IMG_FORMAT_CONTENT_SMALL)

my_format = ImageFormat(max_width=1024,  # Image will be resized based on dimensions.
                        max_height=768,
                        min_quality=85,  # This will optimize to 85% quality.
                        tag="my_format") # Tags are appended to the filename of the
                                         # resulting file so multiple output formats
                                         # can be distinguished.
my_other_format = ImageFormat(max_dimension=1280, # This will ensure that neither height
                                                  # nor width will exceed 1280 pixels.
                              tag="my_other_format")

formats = [IMG_FORMAT_CONTENT_LARGE,
           IMG_FORMAT_CONTENT_MEDIUM,
           IMG_FORMAT_CONTENT_SMALL,
           my_format,
           my_other_format]
```


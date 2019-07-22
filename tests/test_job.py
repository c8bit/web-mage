
import os
import urllib.request as request

from PIL import Image
import pytest

from tests.context import web_mage
from web_mage.formats import ImageFormat
from web_mage.web_mage import Job


@pytest.fixture(scope="session")
def image_file(tmpdir_factory):
    """
        Fixture to download an image from the internet for testing.
    """

    test_img_url_2048_1536 = "https://www.w3.org/MarkUp/Test/xhtml-print/20050519/tests/jpeg420exif.jpg"
    filename = str(tmpdir_factory.mktemp("test_data").join("img.jpg"))
    request.urlretrieve(test_img_url_2048_1536, filename)
    return filename


def test_job(image_file):
    """
        Basic end-to-end test.
    """

    org_filesize = os.path.getsize(image_file)
    assert org_filesize > 0

    org_width = None
    org_height = None
    with Image.open(image_file) as img:
        org_width, org_height = img.size
    assert org_width > 0 and org_height > 0

    (base_filename, extension) = os.path.splitext(image_file)
    output_optimized_filename = base_filename + "_optimized" + extension
    output_minimized_filename = base_filename + "_minimized" + extension
    output_maxdim_filename = base_filename + "_maxdim" + extension
    assert not os.path.exists(output_optimized_filename)
    assert not os.path.exists(output_minimized_filename)

    img_format_minimized = ImageFormat(max_width=(org_width / 2),
                                       max_height=(org_height / 2),
                                       min_quality=60,
                                       tag="minimized")
    img_format_optimized = ImageFormat(min_quality=60, tag="optimized")
    img_format_maxdim = ImageFormat(min_quality=60,
                                    max_dimension=(org_height / 2),
                                    tag="maxdim")

    # Run the job
    job = Job(source=image_file, dest=os.path.dirname(image_file), formats=[img_format_minimized,
                                                                            img_format_optimized,
                                                                            img_format_maxdim])
    job.run()

    # Compare results
    optimized_filesize = os.path.getsize(output_optimized_filename)
    minimized_filesize = os.path.getsize(output_minimized_filename)
    maxdim_filesize    = os.path.getsize(output_maxdim_filename)
    assert os.path.exists(output_optimized_filename)
    assert optimized_filesize < org_filesize

    assert os.path.exists(output_minimized_filename)
    assert minimized_filesize < org_filesize

    assert os.path.exists(output_maxdim_filename)
    assert maxdim_filesize < org_filesize

    # Since minimized file is scaled down, should be smaller than optimized file
    assert minimized_filesize < optimized_filesize

    # Optimized file
    with Image.open(output_optimized_filename) as img:
        width, height = img.size
        assert width == org_width
        assert height == org_height

    # Minimized file
    with Image.open(output_minimized_filename) as img:
        width, height = img.size
        assert ((org_width / 2) - 1) <= width <= (org_width / 2)
        assert ((org_height / 2) - 1) <= height <= (org_height / 2)
    
    # Dimension-constrained file
    with Image.open(output_maxdim_filename) as img:
        width, height = img.size
        if org_width > org_height:
            assert ((org_height / 2) - 1) <= width <= (org_height / 2)
            assert height <= width
        else:
            assert ((org_height / 2) - 1) <= height <= (org_height / 2)
            assert width <= height


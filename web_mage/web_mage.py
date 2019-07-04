
from PIL import Image as PILImage

from .formats import ImageFormat, IMG_FORMAT_DEFAULT

class ImageSet(object):
    def __init__(self, source_file=None, destination=None, target_formats=[IMG_FORMAT_DEFAULT]):
        self.source_file = source_file
        self.destination = destination
        self.target_formats = target_formats

    def optimize(self):
        with PILImage.open(self.source_file) as image:
            for image_format in self.target_formats:
                ((height, width), quality) = image_format.dimensions_for_image(image)
                image = image.resize((height, width), PILImage.ANTIALIAS)
                image.save(self.destination, quality=quality, optimize=True)





def main():
    infile = "./test.jpg"
    outfile = "./optimized.jpg"
    myset = ImageSet(source_file=infile, destination=outfile)
    myset.optimize()



class ImageFormat(object):
    """
        Describes a set of requirements that an image must meet after the optimization
        process.
    """
    def __init__(self, max_width=None,
                       max_height=None,
                       max_size_bytes=None,
                       min_quality=60, max_quality=85):
        self.max_width = max_width
        self.max_height = max_height
        self.max_size_bytes = max_size_bytes
        self.min_quality = min_quality

    def dimensions_for_image(self, image):
        (current_height, current_width) = image.size
        target_ratio = 1

        if self.max_height is not None and self.max_height < current_height:
            target_ratio = min(target_ratio, self.max_height / current_height)
        
        if self.max_width is not None and self.max_width < current_width:
            target_ratio = min(target_ratio, self.max_width / current_width)

        return ((current_height * target_ratio, current_width * target_ratio), self.min_quality)
            

FULL_WIDTH_27_OR_30_INCH = 2560

# Common image format presets

IMG_FORMAT_DEFAULT = ImageFormat()

IMG_FORMAT_THUMBNAIL_LARGE = ImageFormat(max_width=320, max_height=320)
IMG_FORMAT_THUMBNAIL_LARGE_DOUBLE = ImageFormat(max_width=640, max_height=640)

IMG_FORMAT_AVATAR_LARGE = ImageFormat(max_width=100, max_height=100)
IMG_FORMAT_AVATAR_MEDIUM = ImageFormat(max_width=80, max_height=80)
IMG_FORMAT_AVATAR_SMALL = ImageFormat(max_width=60, max_height=60)



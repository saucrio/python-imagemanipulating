import requests, io
from PIL import Image, ImageFilter, ImageEnhance, ImageOps, ImageColor

class Effects:
    """
    Instantiate an effect operation.
    """

    def flip(self, url:str, orientation:str='vertical') -> bytes:
        """
        Flip the image in the specified URL.
        
        :param url: The url of the image you want to flip.
        :type url: str

        :param orientation: Which orientation you want your flipped image to be. Can be either vertical or horizontal.
        :type orientation: str
    
        :return: Flipped image bytes.
        :rtype: bytes
        """
        
        with io.BytesIO() as stream:
            with Image.open(requests.get(url, stream=True).raw) as image:
                if orientation == 'vertical':
                    image = image.transpose(Image.FLIP_TOP_BOTTOM)
                elif orientation == 'horizontal':
                    image = image.transpose(Image.FLIP_LEFT_RIGHT)
                image.save(stream, format='PNG')
            return stream.getvalue()

    def blur(self, url:str, radius:int=3) -> bytes:
        """
        Blurs the image in the specified URL. Images are automatically converted to RGB, because if a GIF is given, Pillow sets the color mode to P or L.
        
        :param url: The url of the image you want to flip.
        :type url: str

        :param radius: Blurs the image depending on the given radius. Higher radius returns a more blurred image. Radius can only be =< 10 because higher values have a higher tendency to crash.
        :type radius: int
    
        :return: Blurred image bytes.
        :rtype: bytes
        """

        if radius < 1: radius == 1
        elif radius > 10: radius == 10
        
        with io.BytesIO() as stream:
            with Image.open(requests.get(url, stream=True).raw) as image:
                image = (image.convert('RGB')).filter(ImageFilter.GaussianBlur(radius))
                image.save(stream, format='PNG')
            return stream.getvalue()

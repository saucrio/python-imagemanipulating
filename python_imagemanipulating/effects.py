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


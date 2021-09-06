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

    def pixelate(self, url:str) -> bytes:
        """
        Pixelates the image in the specified URL.
        
        :param url: The url of the image you want to pixelate.
        :type url: str
    
        :return: Pixelated image bytes.
        :rtype: bytes
        """
        
        with io.BytesIO() as stream:
            with Image.open(requests.get(url, stream=True).raw) as image:
                image = (image.resize((64, 64))).resize(image.size, Image.NEAREST)
                image.save(stream, format='PNG')
            return stream.getvalue()

    def rotate(self, url:str, orientation:str='right') -> bytes:
        """
        Rotates the image in the specified URL to the right or the left depending on the specified orientation. Images are automatically converted to RGB, because if a GIF is given, Pillow sets the color mode to P or L.
        
        :param url: The url of the image you want to rotate.
        :type url: str

        :param url: Rotates the image in the specified orientation. Can be either left or right.
        :type orientation: str
    
        :return: Pixelated image bytes.
        :rtype: bytes
        """
        
        with io.BytesIO() as stream:
            with Image.open(requests.get(url, stream=True).raw) as image:
                if orientation == 'right':
                    image = (image.rotate(90)).convert('RGB')
                elif orientation == 'left':
                    image = (image.rotate(-90)).convert('RGB')
                image.save(stream, format='PNG')
            return stream.getvalue()

    def grayscale(self, url:str) -> bytes:
        """
        Grayscales the image in the specified URL.
        
        :param url: The url of the image you want to grayscale.
        :type url: str
    
        :return: Grayscaled image bytes.
        :rtype: bytes
        """
        
        with io.BytesIO() as stream:
            with Image.open(requests.get(url, stream=True).raw) as image:
                image = image.convert('L')
                image.save(stream, format='PNG')
            return stream.getvalue()

    def invert(self, url:str) -> bytes:
        """
        Inverts the image in the specified URL.
        
        :param url: The url of the image you want to invert. Images are automatically converted to RGB, because if a GIF is given, Pillow sets the color mode to P or L.
        :type url: str
    
        :return: Inverted image bytes.
        :rtype: bytes
        """
        
        with io.BytesIO() as stream:
            with Image.open(requests.get(url, stream=True).raw) as image:
                image = ImageOps.invert(image.convert('RGB'))
                image.save(stream, format='PNG')
            return stream.getvalue()

    def emboss(self, url:str) -> bytes:
        """
        Embosses the image in the specified URL.
        
        :param url: The url of the image you want to emboss. Images are automatically converted to RGB, because if a GIF is given, Pillow sets the color mode to P or L.
        :type url: str
    
        :return: Embossed image bytes.
        :rtype: bytes
        """
        
        with io.BytesIO() as stream:
            with Image.open(requests.get(url, stream=True).raw) as image:
                image = image.convert('RGB').filter(ImageFilter.EMBOSS)
                image.save(stream, format='PNG')
            return stream.getvalue()

    def sepia(self, url:str) -> bytes:
        """
        Applies the sepia effect to the image in the specified URL.
        
        :param url: The url of the image you want to apply the sepia effect to. Images are automatically converted to RGB, because if a GIF is given, Pillow sets the color mode to P or L.
        :type url: str
    
        :return: Sepia image bytes.
        :rtype: bytes
        """

        with io.BytesIO() as stream:
            with Image.open(requests.get(url, stream=True).raw) as image:
                image = image.convert('RGB')
                width, height = image.size
                pixels = image.load() # creating the pixel map

                for py in range(height):
                    for px in range(width):
                        r, g, b = image.getpixel((px, py))

                        tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                        tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                        tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                        if tr > 255:
                            tr = 255

                        if tg > 255:
                            tg = 255

                        if tb > 255:
                            tb = 255

                        pixels[px, py] = (tr,tg,tb)

                image.save(stream, format='PNG')
            return stream.getvalue()
    
    def contour(self, url:str) -> bytes:
        """
        Contours the image in the specified URL.
        
        :param url: The url of the contoured image. Images are automatically converted to RGB, because if a GIF is given, Pillow sets the color mode to P or L.
        :type url: str
    
        :return: Contoured image bytes.
        :rtype: bytes
        """
        
        with io.BytesIO() as stream:
            with Image.open(requests.get(url, stream=True).raw) as image:
                image = image.convert('RGB').filter(ImageFilter.CONTOUR)
                image.save(stream, format='PNG')
            return stream.getvalue()
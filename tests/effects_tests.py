import unittest, random
from python_imagemanipulating import Effects

class EffectsTestCase(unittest.TestCase):

    def test_bytes(self):
        """Test if the returned value from functions is of bytes type."""
        
        test_images = [
            'https://i.imgur.com/4KHa7cL.png', # png
            'https://i.imgur.com/4KHa7cL.jpg', # jpg
            'https://i.imgur.com/Jg0gWBo.gif' # gif
        ]

        random_int = random.randint(-5, 15) # if lower than 1, radius is 1 and if higher than 10, radius is 10, but we make this random number higher to be sure everything works
        
        for image in test_images:
            assert type(Effects().flip(image)) == bytes
            assert type(Effects().flip(image, orientation='horizontal')) == bytes
            assert type(Effects().blur(image, radius=random_int)) == bytes
            assert type(Effects().pixelate(image)) == bytes
            assert type(Effects().rotate(image)) == bytes
            assert type(Effects().rotate(image, orientation='left')) == bytes
            assert type(Effects().grayscale(image)) == bytes
            assert type(Effects().invert(image)) == bytes
            assert type(Effects().emboss(image)) == bytes
            assert type(Effects().sepia(image)) == bytes
            assert type(Effects().contour(image)) == bytes

if __name__ == '__main__':
    unittest.main()
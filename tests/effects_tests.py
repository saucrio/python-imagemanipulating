import unittest
from discordpy_images import Effects

class EffectsTestCase(unittest.TestCase):

    def test_bytes(self):
        """Test if the returned value from functions is of bytes type."""
        test_images = [
            'https://i.imgur.com/4KHa7cL.png', # png
            'https://i.imgur.com/4KHa7cL.jpg', # jpg
            'https://i.imgur.com/Jg0gWBo.gif' # gif
        ]
        for image in test_images:
            assert type(Effects().flip(image)) == bytes
        
        for image in test_images:
            assert type(Effects().flip(image, orientation='horizontal')) == bytes

if __name__ == '__main__':
    unittest.main()
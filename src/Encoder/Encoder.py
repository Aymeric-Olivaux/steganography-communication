from PIL import Image
import numpy as np

from src.Utils.utils import *


class Encoder:
    @staticmethod
    def encode_msg(msg, image_name):
        """
        Encode a msg(string) into a image define by image_name (place the image into resources folder
        :param msg: a string like "Hello World!"
        :param image_name: a image name like "color.jpg"
        :return: The new image
        """
        string_byte = concatenate_binary_to_string(string_to_binary(msg))
        print(string_byte)

        with Image.open("/home/aymeric/Documents/Imagees/resources/" + image_name) as im:
            array = np.array(im)
            jump = 0
            for k in range(len(string_byte) + jump):
                i = k // len(array[0])
                j = k % len(array[0])
                if array[i][j][0] == 255:
                    jump += 1
                    continue
                array[i][j][0] += int(string_byte[k])

            new_image = Image.fromarray(array)
            return new_image

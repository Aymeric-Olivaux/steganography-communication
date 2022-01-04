from PIL import Image
import numpy as np

from src.Utils.utils import *


class Decoder:
    @staticmethod
    def decode_msg(pub_image_name, private_image_name):
        """
        Decode a msg(string) from a public image by comparing every bit with a private image
        :param pub_image_name: The modified image that contain the message
        :param private_image_name: The original image
        :return msg: The famous message
        """

        with Image.open("/home/aymeric/Documents/Imagees/resources/" + private_image_name) as im:
            private_array = np.array(im)

        with Image.open("/home/aymeric/Documents/Imagees/resources/results/" + pub_image_name) as im:
            pub_array = np.array(im)

        if len(pub_array) != len(private_array) or len(pub_array[0]) != len(private_array[0]):
            raise Exception("Images should at least be equal in lengths")

        result_bin_str = ""
        is_end = 0
        for j in range(len(pub_array)):
            for i in range(len(pub_array[0])):
                result_int = int(pub_array[j][i][0]) - int(private_array[j][i][0])
                result_bin_str += str(result_int)
                if result_int == 0:
                    is_end += 1
                else:
                    is_end = 0
                if is_end == 8:
                    break

            if is_end == 8:
                break
        list_bin = separate_string_to_binary(result_bin_str)
        msg = binary_to_string(list_bin)
        print("msg: " + msg)
        return msg

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

        with Image.open("/home/aymeric/Documents/Imagees/resources/original/" + private_image_name) as im:
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
        return msg

    @staticmethod
    def run_decode():
        print("What if the name of the original image?")
        original_name = input('>')
        encoded_name = "pub_" + original_name
        print("What is the type of the file? ('text', 'image', 'pdf', '.txt')")
        type_name = input('>')
        if type_name != "text" and type_name != "image" and type_name != "pdf" and type_name != ".txt":
            raise Exception("Bad type")
        if type_name != 'text':
            raise Exception("Type not yet implemented")
        message = Decoder.decode_msg(encoded_name, original_name)

        print("The final message is:\n===============\n" + message + "\n===============")


if __name__ == '__main__':
    Decoder.run_decode()

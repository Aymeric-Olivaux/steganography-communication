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

        with Image.open(PATH_TO_RESOURCES + "original/" + private_image_name) as im:
            private_array = np.array(im)

        with Image.open(PATH_TO_RESOURCES + "results/" + pub_image_name) as im:
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
        result_bin_str = result_bin_str[8:] # Cur the first word for type
        list_bin = separate_string_to_binary(result_bin_str)
        msg = binary_to_string(list_bin)
        return msg

    @staticmethod
    def get_type(pub_image_name, private_image_name):

        with Image.open(PATH_TO_RESOURCES + "original/" + private_image_name) as im:
            private_array = np.array(im)

        with Image.open(PATH_TO_RESOURCES + "results/" + pub_image_name) as im:
            pub_array = np.array(im)
        if len(pub_array) != len(private_array) or len(pub_array[0]) != len(private_array[0]):
            raise Exception("Images should at least be equal in lengths")

        result_bin_str = ""
        is_end = 0
        for j in range(len(pub_array)):
            for i in range(len(pub_array[0])):
                result_int = int(pub_array[j][i][0]) - int(private_array[j][i][0])
                result_bin_str += str(result_int)

                is_end += 1
                if is_end == 8:
                    break
            if is_end == 8:
                break
        i = int(result_bin_str)

        if i == 1: # text
            return 'text'
        if i == 2: # image
            return 'image'
        if i == 3: # pdf
            return 'pdf'
        if i == 4: # .txt
            return '.txt'
        raise Exception("Unknown type")

    @staticmethod
    def run_decode():
        print("What if the name of the original image?")
        original_name = input('>')
        encoded_name = "pub_" + original_name
        type_name = Decoder.get_type(pub_image_name=encoded_name, private_image_name=original_name)
        if type_name != "text" and type_name != "image" and type_name != "pdf" and type_name != ".txt":
            raise Exception("Bad type")
        if type_name != 'text':
            raise Exception("Type not yet implemented")
        message = Decoder.decode_msg(encoded_name, original_name)

        print("The final message is:\n===============\n" + message + "\n===============")


if __name__ == '__main__':
    Decoder.run_decode()

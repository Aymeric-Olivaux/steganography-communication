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

    @staticmethod
    def run_encode():
        print("What type of file you want to encode?\n('text', 'image', 'pdf', '.txt'")
        argument = input('>')

        if argument == 'text':
            print("What is the text?")
            text = input()
            image_to_encode_name = "color.png"
            encoded_image = Encoder.encode_msg(text, image_to_encode_name)
            path_to_save = "/home/aymeric/Documents/Imagees/resources/results/pub_im1.png"
            encoded_image.save(path_to_save)
            print("Your encoded image have been saved into " + path_to_save)
            return
        elif argument == 'image':
            raise Exception("Image are not yet implemented")
        elif argument == 'pdf':
            raise Exception("Pdf are not yet implemented")
        elif argument == '.txt':
            raise Exception(".txt are not yet implemented")
        return


if __name__ == '__main__':
    Encoder.run_encode()

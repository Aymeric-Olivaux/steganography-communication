from PIL import Image
import numpy as np

from Generator.Generator import Generator

def strToBinary(a):
    """
    Transform a string to a list of binary with an ASCII conversion
    :param a: A string like "Hello World!"
    :return: A list of binary(int) like : [1001000, ..., 100001]
    """
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

def binarytoString(a):
    """
    Transform a list of binary to a string whit a ASCII conversion
    :param a: A list of binary(int) like : [1001000, ... , 100001]
    :return: A string like "Hello World!"
    """
    list_char_int = []
    list_char_str = ""
    for i in a:
        i = str(i)
        i = int(i, 2)
        list_char_int.append(i)
    for i in list_char_int:
        list_char_str += chr(i)
    return list_char_str

def concatenate_binary_to_string(l):
    """
    Transform a list of binary to a single string that concatenate every byte
    :param l: A list of binary(int) like : [1001000, ... , 100001]
    :return: A string like "1001000...100001"
    """
    result_string = ""

    for i in l:
        for j in range(len(str(i)), 8):
            result_string += "0"
        result_string += str(i)


    if len(result_string) % 8 != 0:
       raise Exception("Something goes wrong")
    return result_string

def separate_string_to_binary(result_string):
    """
    Transform a single string to a list of binary
    :param l: A string like "1001000...100001"
    :return: A list of binary(int) like : [1001000, ... , 100001
    """
    if len(result_string) % 8 != 0:
        result_string = result_string[:(len(result_string) // 8) * 8]


    result_list = []
    for i in range(int(len(result_string) / 8)):
        element = result_string[i*8:i*8+8]
        element = int(element)
        result_list.append(element)

    return result_list

def encode_msg(msg, image_name):
    """
    Encode a msg(string) into a image define by image_name (place the image into ressources folder
    :param msg: a string like "Hello World!"
    :param image_name: a image name like "color.jpg"
    :return: The new image
    """
    string_byte = concatenate_binary_to_string(strToBinary(msg))
    print(string_byte)

    with Image.open("/home/aymeric/Documents/Imagees/ressources/" + image_name) as im:
        array = np.array(im)
        jump = 0
        for k in range(len(string_byte) + jump):
            i = k // len(array[0])
            j = k % len(array[0])
            if array[i][j][0] == 255:
                jump += 1
                continue
            #print("i: " + str(i) + " j: " + str(j))
            array[i][j][0] += int(string_byte[k])

        new_image = Image.fromarray(array)
        return new_image

def decode_msg(pub_image_name, priv_image_name):
    """
    Decode a msg(string) from a public image by comparing every bit with a private image
    :param pub_image_name: The modified image that contain the message
    :param priv_image_name: The original image
    :return msg: The famous message
    """

    with Image.open("/home/aymeric/Documents/Imagees/ressources/" + priv_image_name) as im:
        priv_array = np.array(im)

    with Image.open("/home/aymeric/Documents/Imagees/ressources/results/" + pub_image_name) as im:
        pub_array = np.array(im)

    if len(pub_array) != len(priv_array) or len(pub_array[0]) != len(priv_array[0]):
        raise Exception("Images should at least be equal in lenghts")

    result_bin_str = ""
    is_end = 0
    for j in range(len(pub_array)):
        for i in range(len(pub_array[0])):
            result_int = int(pub_array[j][i][0]) - int(priv_array[j][i][0])
            result_bin_str += str(result_int)
            if(result_int == 0):
                is_end += 1
            else:
                is_end = 0
            if is_end == 8:
                break

        if is_end == 8:
            break
    list_bin = separate_string_to_binary(result_bin_str)
    msg = binarytoString(list_bin)
    print("msg: " + msg)
    return msg

def run_try():
    msg = "Hello World!"
    image_name = "im1.png"

    with open("/home/aymeric/Documents/Imagees/ressources/LoremIpsum", 'r') as file:
        lorem_ipsum = file.read()

    msg = "Hello World!"
    new_image = encode_msg(msg, image_name)
    new_image.save("/home/aymeric/Documents/Imagees/ressources/results/pub_im1.png")
    msg = decode_msg("pub_im1.png", image_name)


if __name__ == '__main__':
    new_gen = Generator
    Generator.generate(new_gen, 200, 200, rgb=True)

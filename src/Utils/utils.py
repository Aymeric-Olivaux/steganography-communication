import os


def string_to_binary(a):
    """
    Transform a string to a list of binary with an ASCII conversion
    :param a: A string like "Hello World!"
    :return: A list of binary(int) like : [1001000, ..., 100001]
    """
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m


def binary_to_string(a):
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


def concatenate_binary_to_string(list_binary):
    """
    Transform a list of binary to a single string that concatenate every byte
    :param list_binary: A list of binary(int) like : [1001000, ... , 100001]
    :return: A string like "1001000...100001"
    """
    result_string = ""

    for i in list_binary:
        for j in range(len(str(i)), 8):
            result_string += "0"
        result_string += str(i)

    if len(result_string) % 8 != 0:
        raise Exception("Something goes wrong")
    return result_string


def separate_string_to_binary(result_string):
    """
    Transform a single string to a list of binary
    :param result_string: A string like "1001000...100001"
    :return: A list of binary(int) like : [1001000, ... , 100001]
    """
    if len(result_string) % 8 != 0:
        result_string = result_string[:(len(result_string) // 8) * 8]

    result_list = []
    for i in range(int(len(result_string) / 8)):
        element = result_string[i * 8:i * 8 + 8]
        element = int(element)
        result_list.append(element)

    return result_list


def pdf_to_binary(name_pdf):
    """
    This function transform a pdf into a list of binary
    The pdf have to be save in resources/data
    :param name_pdf:
    :return: A list of binary(int) like : [1001000, ... , 100001]
    """
    lines = []
    with open(PATH_TO_RESOURCES + "data/" + name_pdf, 'rb') as file:
        for line in file.readlines():
            lines.append(line)

    path = PATH_TO_RESOURCES + "results/"
    file = open(path + "new.pdf", 'wb')
    for line in lines:
        file.write(line)
    file.close()


def get_path_to_resources():
    path = os.path.abspath(__file__)
    index = path.index("Imagees")
    result = path[:index]
    result = result + "Imagees/resources/"
    return result


PATH_TO_RESOURCES = get_path_to_resources()

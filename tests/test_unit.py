import unittest

import numpy

from src.main import *
class TestUnit(unittest.TestCase):

    def test_str_to_binary_1(self):
        self.assertEqual([1100001], strToBinary("a"))

    def test_str_to_binary_2(self):
        self.assertEqual([1100010], strToBinary("b"))

    def test_str_to_binary_3(self):
        self.assertEqual([110001], strToBinary("1"))

    def test_str_to_binary_4(self):
        self.assertEqual([1100001, 110001], strToBinary("a1"))


    def test_binary_to_string_1(self):
        self.assertEqual(binarytoString([1100001]), "a")

    def test_binary_to_string_2(self):
        self.assertEqual(binarytoString([1100010]), "b")

    def test_binary_to_string_3(self):
        self.assertEqual(binarytoString([110001]), "1")

    def test_binary_to_string_4(self):
        self.assertEqual(binarytoString([1100001, 110001]), "a1")


    def test_concatenate_binary_to_string_1(self):
        test = [1100001]
        expected = "01100001"
        self.assertEqual(concatenate_binary_to_string(test), expected)

    def test_concatenate_binary_to_string_2(self):
        test = [1100001, 110001]
        expected = "0110000100110001"
        self.assertEqual(concatenate_binary_to_string(test), expected)


    def test_concatenate_binary_to_string_3(self):
        test = [0, 0]
        expected = "0000000000000000"
        self.assertEqual(concatenate_binary_to_string(test), expected)


    def test_concatenate_binary_to_string_4(self):
        test = [11111111, 11111111]
        expected = "1111111111111111"
        self.assertEqual(concatenate_binary_to_string(test), expected)

    def test_separate_string_to_binary_1(self):
        expected = [1100001]
        test = "01100001"
        self.assertEqual(separate_string_to_binary(test), expected)

    def test_separate_string_to_binary_2(self):
        expected = [1100001, 110001]
        test = "0110000100110001"
        self.assertEqual(separate_string_to_binary(test), expected)

    def test_separate_string_to_binary_3(self):
        expected = [0, 0]
        test = "0000000000000000"
        self.assertEqual(separate_string_to_binary(test), expected)

    def test_separate_string_to_binary_4(self):
        expected = [11111111, 11111111]
        test = "1111111111111111"
        self.assertEqual(separate_string_to_binary(test), expected)

    def test_image_to_array_to_image_to_array(self):
        with Image.open("/home/aymeric/Documents/Imagees/ressources/color.png") as im:
            array_1 = np.array(im)

        new_image = Image.fromarray(array_1)
        new_image.save("/home/aymeric/Documents/Imagees/ressources/tmp/tmp.png")
        with Image.open("/home/aymeric/Documents/Imagees/ressources/tmp/tmp.png") as im:
            array_2 = np.array(im)
        b = numpy.array_equal(array_2, array_1)
        self.assertEqual(b, True)

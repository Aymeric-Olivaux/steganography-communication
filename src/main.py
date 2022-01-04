from PIL import Image
import numpy as np

from Generator.Generator import Generator
from Encoder.Encoder import Encoder
from Decoder.Decoder import Decoder

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

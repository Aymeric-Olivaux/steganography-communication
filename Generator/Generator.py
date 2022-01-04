import random

from PIL import Image
import numpy as np

class Generator:

    def generate(self, x: int, y: int, rgb: bool = False):
        if rgb:
            new_image = Image.new('RGB', (x, y))
        else:
            new_image = Image.new('L', (x, y))
        new_image_array = np.array(new_image)
        for i in range(x):
            for j in range(y):
                if rgb:
                    for k in range(0, 3):
                        new_image_array[i][j][k] = random.randint(0, 255)
                else:
                    new_image_array[i][j] = random.randint(0, 255)

        new_image_2 = Image.fromarray(new_image_array)
        new_image_2.show()

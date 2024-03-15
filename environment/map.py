import random

import matplotlib.pyplot as plt
import numpy as np


class MapEnv:

    def __init__(
        self,
        map_size: tuple,
    ):
        self.map = np.zeros(map_size)

        self.width, self.height = map_size

    def update_map(self, positions):

        for position in positions:
            print(position)
            if not self.check_bounds(position=position):
                print(f"{position}: out of bounds")
                continue
            col, row = position
            self.map[row, col] = 1  # Update map as occupied

    def check_bounds(self, position):
        col, row = position
        if col >= self.width or col < 0:
            return False
        if row >= self.height or row < 0:
            return False
        return True

    def viz_map(self):
        print(np.unique(self.map))
        plt.imshow(self.map, cmap="grey")
        plt.show()

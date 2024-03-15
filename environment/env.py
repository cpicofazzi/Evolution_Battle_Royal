from map import MapEnv
from resources import BaseResource


class Env:

    def __init__(self, map_size: tuple = (200, 200)):
        self.map_size = map_size
        self.map = MapEnv(map_size=self.map_size)

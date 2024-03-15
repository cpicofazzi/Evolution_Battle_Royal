import time

from environment.map import MapEnv

MAP_SIZE = (800, 800)
ENTITY_COLOR = (255, 50, 50)
TILE_SIZE = 10
import pygame

pygame.init()

map_env = MapEnv(map_size=MAP_SIZE, tile_size=TILE_SIZE)

positions = [(1, 1), (10, 5)]
map_env.screen.fill((200, 200, 200))
map_env.draw_map(positions=positions, color=ENTITY_COLOR)
pygame.display.update()

while True:

    time.sleep(5)

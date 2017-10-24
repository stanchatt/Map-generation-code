import random
import pygame
import os

pygame.init()

"""This finds and names each tile appropriately"""
textures = {
    'Dirt': pygame.image.load('Dirt.png'),
    'Grass': pygame.image.load('Grass.png'),
    'Sand': pygame.image.load('Sand.png'),
    'Stone': pygame.image.load('Stone.png'),
    'Water': pygame.image.load('Water.png')
}

"""makes the list of tiles to be used"""
list_of_tiles = ['Dirt', 'Grass', 'Sand', 'Stone', 'Water']

"""set the tile size and then times it by the number of tiles required """
tile_size_in_pixels = 64
number_of_tiles_in_width = 16
number_of_tiles_in_height = 11
set_screen_width = tile_size_in_pixels*number_of_tiles_in_width
set_screen_height = tile_size_in_pixels*number_of_tiles_in_height

screen = pygame.display.set_mode((set_screen_width, set_screen_height))

done = False

"""Displays the tiles in a random pattern"""


def tiles():
    for x in range(0,set_screen_width, tile_size_in_pixels):
        for y in range(0, set_screen_height, tile_size_in_pixels):
            key = list_of_tiles[random.randint(0, len(list_of_tiles) - 1)]
            screen.blit(textures[key], (x, y))


tiles()

"""keeps the window open until you want to close it"""
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    pygame.display.update()
import pygame, sys
from pygame.math import Vector2 as vector

WINDOWS_WIDTH, WINDOWS_HEIGHT = 1280, 720
TILE_SIZE = 128
ANIMATION_SPEED = 6

# layers
Z_LAYERS = {
    'bg':0,
    'clouds':1,
    'bg tiles':2,
    'path':3,
    'bg details':4,
    'main':5,
    'water':6,
    'fg':7,
}
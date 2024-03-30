from settings import *

class Level:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()

        self.setup(tmx_map)

    def setup(self, tmx_map):
        for x,y,surf in tmx_map.get_layer_by_name('Terrain').tiles():
            print(x)
            print(y)
            print(surf)

    def run(self):
        self.display_surface.fill('gray')

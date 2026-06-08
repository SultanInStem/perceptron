import pygame
 

class Canvas: 
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.fps = 30
        self.clock = pygame.time.Clock()


    def update(self): 
        pass




    def run(self): 
        pass

    
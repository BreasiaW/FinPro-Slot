from machine import Machine
from settings import *
import pygame, sys

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Slot Machine')
        self.clock = pygame.tick_Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)

        self.machine = Machine()
        self.delta_time = 0

    def run(self):


        while True:
            #Handle quit operation
            for event in pygame.event_get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()
            

            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time)
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()






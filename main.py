"All libraries for AI and level generation will be called here"

from pygame.locals import *
import pygame
import numpy as np
 
class Player:
    x = 200
    y = 150
    x2 = 400
    y2 = 300
    speed = 0.45
 
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def moveUp(self):
        self.y = self.y - self.speed
 
    def moveDown(self):
        self.y = self.y + self.speed
 
class Maze:
    def __init__(self):
       self.M = 11
       self.N = 8
       #Create a goal for the game
       
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,
                     1,0,0,0,0,0,0,1,1,1,1,
                     1,0,0,0,0,1,0,0,0,1,1,
                     1,0,1,1,1,1,1,1,0,0,1,
                     1,0,1,0,0,0,0,0,0,0,1,
                     1,1,1,0,1,1,1,1,0,0,1,
                     1,1,0,0,0,0,0,1,1,0,1,
                     1,1,1,1,1,1,1,1,1,0,1,]
       
       hx = 0
       hy = 0
       tempx = []
       tempy = []
       self.WumpaArrayX = []
       self.WumpaArrayY = []
       self.WumpaArrayX.append(hx)
       self.WumpaArrayY.append(hy)
       for i in range(0,self.M*self.N):
           if self.maze[ hx + (hy*self.M) ] == 1:
               self.WumpaArrayX.append(hx * 130)
               self.WumpaArrayY.append(hy * 130)
           elif self.maze[ hx + (hy*self.M) ] == 2:
               print('YOU WIN!')
           hx = hx + 1

           
           if hx > self.M-1:
               hx = 0
               hy = hy + 1
               


    def draw(self,display_surf,image_surf,dot_surf):
       bx = 0
       by = 0
       for i in range(0,self.M*self.N):
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(image_surf,( bx * 130 , by * 130))
           bx = bx + 1
           if bx > self.M-1:
               bx = 0
               by = by + 1


class Game:
    def isCollision(self,x1,x2,y1,y2,hitbox):
        if x2 >= x1 and x2 <= x1 + hitbox:
            if y2 >= y1 and y2 <= y1 + hitbox:
                return True
            return False
        
class App:

    windowWidth = 1400
    windowHeight = 600
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self._dot_surf = None
        self.player = Player()
        self.maze = Maze()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((1420, 700))
        boarders = {}

        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self.game = Game()
        self._image_surf = pygame.image.load("Pixel.png").convert()
        self._block_surf = pygame.image.load("Pixel.png").convert()
        self._dot_surf = pygame.image.load("Pixel.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        # did player collide with surface?
        for i in range(len(self.maze.WumpaArrayX)):
            if self.game.isCollision(self.maze.WumpaArrayX[i], self.player.x, self.maze.WumpaArrayY[i], self.player.y, 80):
                print('You LOSE')
                exit(0)
        

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf, self._block_surf, self._dot_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.display.quit()
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            pass
            
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()

import pygame
import os

im_path = os.path.join("Kamui.png")

class Kamui(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    Kamui.image = pygame.image.load("Kamui.png") 
    #Above you are loading in the image
    self.image = Kamui.image
          #transform is pygame exclusive

    self.x = 50
    self.y = 50 #calling this object ot exist at 50 on our grid
    self.hitbox = (self.x, self.y, 55,55)
    #represents pixels in an area
#everything above is for the picture
  def draw(self, surface):
    surface.blit(self.image, (self.x, self.y))
#This function is used to draw the image onto the background
#You need this because the computer can't draw it itself




pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

Sprite = Kamui()  
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
  
  screen.fill((255,255,255))
  Sprite.draw(screen)

  pygame.display.update()
  
  clock.tick(60)



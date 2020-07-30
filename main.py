import pygame
import os

im_path = os.path.join("RyUU.png")

class RyUU(object):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    RyUU.image = pygame.image.load("RyUU.png") 
    #Above you are loading in the image
    self.image = RyUU.image
    self.image = pygame.transform.scale(self.image,(150,100))

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
  def movement(self, width, height):
    key = pygame.key.get_pressed()

    if key[pygame.K_DOWN] and self.y < height - 50:
      self.y += 1
    if key[pygame.K_UP] and self.y > 0:
      self.y -= 2
    if key[pygame.K_LEFT] and self.x > 0:
      self.x -= 1
    if key[pygame.K_RIGHT] and self.x < width - 50:
      self.x += 1

def Gravity(self, height):
  if self.y < height - 50 and pygame.key.get_focused():
    self.y += 1


pygame.init()
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

Sprite = RyUU()  
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      running = False
  
  screen.fill((255,255,255))
  Sprite.Gravity(screen_height  )
  Sprite.draw(screen)

  pygame.display.update()
  
  clock.tick(60)





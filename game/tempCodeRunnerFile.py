import pygame
import random
import math

# initializing pygame
pygame.init()

# creating a screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load(
    'C://Users//win7//Desktop//python//game//749.png')

# change caption and icon
pygame.display.set_caption("Save the shinobhi")
icon = pygame.image.load('C://Users//win7//Desktop//python//game//naruto.png')
pygame.display.set_icon(icon)

# player img
playerimg = pygame.image.load(
    'C://Users//win7//Desktop//python//game//ninja.png')
playerX = 300
playerY = 480
playerX_change = 0

# enemy img
enemyimg = pygame.image.load(
    'C://Users//win7//Desktop//python//game//evil.png')
enemyX = random.randint(0, 740)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 40

# score
score = 0

# weapon img
# at the beggining it is at ready
# when the fuction is called the state changes to fire
weponimg = pygame.image.load(
    'C://Users//win7//Desktop//python//game//blade.png')
weponX = 0
weponY = 480
weponX_change = 0
weponY_change = 10
wepon_state = 'ready'


def enemy(x, y):
  screen.blit(enemyimg, (x, y))


def player(x, y):
  screen.blit(playerimg, (x, y))


def wepon(x, y):
  global wepon_state
  wepon_state = 'fire'
  screen.blit(weponimg, (x+22, y+12))


def isCollision(enemyX, enemyY, weponX, weponY):
  distance = math.sqrt((math.pow(enemyX-weponX, 2)) +
                       (math.pow(enemyY-weponY, 2)))
  if distance < 27:
     return True
  else:
    return False


# loop for the game to stay
running = True
while running:

    # Colour    red gre blu
  screen.fill((50, 70, 100))
  screen.blit(background, (0, 0))
  for game in pygame.event.get():
    if game.type == pygame.QUIT:
      running = False

    # keyboard control over the game
    if game.type == pygame.KEYDOWN:
     if game.key == pygame.K_LEFT:
       playerX_change -= 4
     if game.key == pygame.K_RIGHT:
       playerX_change += 4
     if game.key == pygame.K_SPACE:
       # check if a bullet is there if not then it sets its cordinate
       if wepon_state is 'ready':
         weponX = playerX
         wepon(weponX, weponY)

    if game.type == pygame.KEYUP:
      if game.key == pygame.K_LEFT or game.key == pygame.K_RIGHT:
        playerX_change = 0

 # player movements
  playerX += playerX_change

  if playerX <= 0:
    playerX = 0
  if playerX >= 740:
    playerX = 740

# enemy movement
  enemyX += enemyX_change
  if enemyX <= 0:
    enemyX_change = 3
    enemyY += enemyY_change
  if enemyX >= 740:
    enemyX_change = -3
    enemyY += enemyY_change

# bullet movement
  if weponY <= 0:
    weponY = 480
    wepon_state = 'ready'
  if wepon_state is 'fire':
    wepon(weponX, weponY)
    weponY -= weponY_change

# collision
  collision = isCollision(enemyX, enemyY, weponX, weponY)
  if collision:
    weponY = 480
    wepon_state = 'ready'
    score += 1
    print(score)
    enemyX = random.randint(0, 740)
    enemyY = random.randint(50, 150)

  player(playerX, playerY)
  enemy(enemyX, enemyY)

  pygame.display.update()

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
# for multiple enimies
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 5

for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load(
        'C://Users//win7//Desktop//python//game//evil.png'))
    enemyX.append(random.randint(0, 740))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# score
score_value = 0
font = pygame.font.Font('C://Users//win7//Desktop//python//game//Boba milky.ttf',32)
 
textX=10
textY=10

#game over
game_over_font = pygame.font.Font('C://Users//win7//Desktop//python//game//Boba milky.ttf',100)


def show_score(x,y):
  score=font.render("Score : "+ str(score_value),True,(225,225,225))
  screen.blit(score,(x,y))

def game_over():
  gameOver=font.render("GAME OVER",True,(0,0,0))
  screen.blit(gameOver,(300,250))


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


def enemy(x, y, i):
  screen.blit(enemyimg[i], (x, y))


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
       playerX_change -= 5
     if game.key == pygame.K_RIGHT:
       playerX_change += 5
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
  for i in range(num_of_enemy):
    #game over
    if enemyY[i]>400:
      for j in range(num_of_enemy):
        enemyY[j]=2000
      game_over()
      break


    enemyX[i] += enemyX_change[i]
    if enemyX[i] <= 0:
      enemyX_change[i] = 3
      enemyY[i] += enemyY_change[i]
    if enemyX[i] >= 740:
      enemyX_change[i] = -3
      enemyY[i] += enemyY_change[i]

    # collision
    collision = isCollision(enemyX[i], enemyY[i], weponX, weponY)
    if collision:
      weponY = 480
      wepon_state = 'ready'
      score_value += 1
      print(score_value)
      enemyX[i] = random.randint(0, 740)
      enemyY[i] = random.randint(50, 150)

    enemy(enemyX[i], enemyY[i], i)  
    

# bullet movement
  if weponY <= 0:
    weponY = 480
    wepon_state = 'ready'
  if wepon_state is 'fire':
    wepon(weponX, weponY)
    weponY -= weponY_change


  player(playerX, playerY)
  show_score(textX,textY)

  pygame.display.update()

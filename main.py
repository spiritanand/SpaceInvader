import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Player Image
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy Image
enemyImg = pygame.image.load("enemy.png")
enemyX = 370
enemyY = 50
enemyX_change = 0


# A function to display the player
def player(x,y):
    # To draw an image of the player on the screen
    screen.blit(playerImg, (x, y))


# A function to display the enemy
def enemy(x,y):
    # To draw an image of the player on the screen
    screen.blit(enemyImg, (x, y))


# Title and Icon
pygame.display.set_caption("The Space Invaders")
ufo_icon = pygame.image.load("spaceship1.png")
pygame.display.set_icon(ufo_icon)

# This makes the window to run till the required time. The Game loop.
running = True
while running:
    # RGB ~ Colour of the background
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Checking the press of a keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

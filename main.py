import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

score = 0
font = pygame.font.Font("super_mario_256/SuperMario256.ttf", 32)
textX = 600
textY = 10

# Game Over Text
over_font = pygame.font.Font("super_mario_256/SuperMario256.ttf", 72)

# Background Music
mixer.music.load("imperial_march.wav")
mixer.music.play(-1)

 
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (180, 250))


def show_score(x, y):
    score_view = font.render("Score - " + str(score), True, (255, 255, 255))
    screen.blit(score_view, (x, y))


# Create the screen
screen = pygame.display.set_mode((800, 600))

# Background Image
background = pygame.image.load("background1.jpg")

# Player Image
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Creating Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2.5)
    enemyY_change.append(30)

# Bullet Image
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 5
bullet_fire = False


# Function to display the player
def player(x, y):
    # To draw an image of the player on the screen
    screen.blit(playerImg, (x, y))


# Function to display the enemy
def enemy(x, y, i):
    # To draw an image of the player on the screen
    screen.blit(enemyImg[i], (x, y))


# Function to fire the bullet when the space bar is pressed.
def fire_bullet(x, y):
    global bullet_fire
    bullet_fire = True
    screen.blit(bulletImg, (x + 16, y + 24))


def collision_check(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    if distance < 27:
        return True
    else:
        return False


# Title and Icon
pygame.display.set_caption("The Space Invaders")
ufo_icon = pygame.image.load("spaceship1.png")
pygame.display.set_icon(ufo_icon)

# This makes the window to run till the required time. The Game loop.
running = True
while running:

    # RGB ~ Colour of the background
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Any key pressed is an event. Here we are checking if any key has been pressed.
    for event in pygame.event.get():
        # To check if the user wants to quit.
        if event.type == pygame.QUIT:
            running = False
        # Checking the press of a keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.5
            if event.key == pygame.K_SPACE:
                if not bullet_fire:
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    bullet_sound = mixer.Sound("laser_beam.wav")
                    bullet_sound.play()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_change = 0

    # Checking for the boundary of the spaceship(user)
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement mechanics
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] >= 420:
            for j in range(num_of_enemies):
                enemyY[j] = 1000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2.5
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = collision_check(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_fire = False
            score += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(48, 192)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_fire = False
    if bullet_fire:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    # This is the most essential function as this constantly updates the display.
    pygame.display.update()

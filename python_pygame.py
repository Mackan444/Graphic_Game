import  math
import pygame
import random

# intialize the system
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Title and icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyimg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0.25
enemyY_change = 40

# Bullet

# Ready - you can't see the bullet
# Fire - the bullet is currently moving
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y):
    screen.blit(enemyimg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    # RGB Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.4 -> 5 = 5 - 0.4
    # 5 = 5 + 0.4

    # Boundries for spaceship
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    # Boundries
    if enemyX <=0:
        enemyX_change = 0.25
        enemyY += enemyY_change
    elif enemyX >=736:
        enemyX_change = -0.25
        enemyY += enemyY_change

    # Bullet Movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
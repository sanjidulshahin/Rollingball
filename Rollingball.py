import pygame
import math
import random
from pygame import mixer

pygame.init()
# Creating screen
screen = pygame.display.set_mode((800, 600))
# naming the game
pygame.display.set_caption("Rolling Ball")
# creating icon of the game
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
# Background
background = pygame.image.load('background1.png')
# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)
# Fence
fence = pygame.image.load('fenceupd2.png')

# block1

blockImg1 = pygame.image.load('block1.png')
blockX1 = 650
blockY1 = 300
blockY1_change = 0
blockX1_ini = 650
blockY1_ini = 300

# block2

blockImg2 = pygame.image.load('block1.png')
blockX2 = 480
blockY2 = 400
blockY2_change = 0
blockX2_ini = 480
blockY2_ini = 400

# block3
blockImg3 = pygame.image.load('block1.png')
blockX3 = 330
blockY3 = 500
blockY3_change = 0
blockX3_ini = 330
blockY3_ini = 500

# block4
blockImg4 = pygame.image.load('block1.png')
blockX4 = 170
blockY4 = 600
blockY4_change = 0
blockX4_ini = 170
blockY4_ini = 600



# nailed block1
nailedblockImg1 = pygame.image.load('nailedblock2.png')
nailedX1 = 20
nailedY1 = 800
nailedY1_change = 0
nailedX1_ini = 20
nailedY1_ini = 800

# Ball
ballImg = pygame.image.load('icon.png')
ballX = 710
ballY = 320
ballX_change = 0
ballY_change = 0
ballX_ini = 710
ballY_ini = 320

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
testX = 10
testY = 40

# Jump
'''
CLOCK = pygame.time.Clock()
jumping = False
Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT
'''


# lives
lives = 2
# game over
game_over = False
# Extra point
extrapointImg = pygame.image.load('extrapoint1.png')
extrapointX = random.randint(200, 650)
extrapointY = random.randint(200, 400)

# Lives killer
liveskillerImg = []
liveskillerX = []
liveskillerY = []
num_of_liveskiller = 3
for i in range (num_of_liveskiller):
    liveskillerImg.append(pygame.image.load('liveskiller.png'))
    liveskillerX.append(random.randint(100,700))
    liveskillerY.append(random.randint(100,500))


# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    global game_over
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    display_restart = font.render("Press Space to Restart ",True,(125,125,125))
    screen.blit(display_restart,(200,500))
    game_over = True


def lives_text():
    player_lives = font.render("Lives: " + str(lives), True, (255, 255, 255))
    screen.blit(player_lives, (650, 50))


def ball(x, y):
    screen.blit(ballImg, (x, y))


def block(x, y):
    screen.blit(blockImg1, (x, y))


def nailedblock(x, y):
    screen.blit(nailedblockImg1, (x, y))


def extraPoint(x, y):
    screen.blit(extrapointImg, (x, y))


def livesKiller(x, y,i):
    screen.blit(liveskillerImg[i], (x, y))


def End():
    global ballY, blockY1, blockY2, blockY3, blockY4, nailedY1, extrapointX, extrapointY, liveskillerX, liveskillerY
    ballY = 2000
    blockY1 = 2000
    blockY2 = 2000
    blockY3 = 2000
    blockY4 = 2000
    nailedY1 = 2000
    extrapointX, extrapointY = 2000, 2000
    liveskillerX, liveskillerY = 2000, 2000

    game_over_text()


def iscollision(ballX, ballY, X, Y):
    distance = math.sqrt((math.pow(ballX - X, 2)) + (math.pow(ballY - Y, 2)))
    if distance < 27:
        return True
    else:
        return False


running = True
while running:

    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    # fence
    screen.blit(fence, (0, 0))
    # screen.blit(fence,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                ballX_change = -4
            if event.key == pygame.K_RIGHT:
                ballX_change = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                ballX_change = 0
            if event.key == pygame.K_SPACE and game_over:
                ballX = ballX_ini
                ballY = ballY_ini
                blockX1 = blockX1_ini
                blockY1 = blockY1_ini

                blockX2 = blockX2_ini
                blockY2 = blockY2_ini

                blockX3 = blockX3_ini
                blockY3 = blockY3_ini

                blockX4 = blockX4_ini
                blockY4 = blockY4_ini


                nailedX1 = nailedX1_ini
                nailedY1 = nailedY1_ini

                for i in range(num_of_liveskiller):
                    extrapointX = random.randint(200, 650)
                    extrapointY = random.randint(200, 400)


                liveskillerX = random.randint(200, 650)
                liveskillerY = random.randint(200, 400)


                lives = 2
                score_value = 0
                game_over =False
    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jumping = True
    if jumping:
        ballY -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
    '''


    # ball movement towards X coordinate
    ballX += ballX_change

    # boundary setting of ball's in the direction of X coordinate
    if ballX <= 0:
        ballX = 0
    elif ballX >= 768:
        ballX = 768

    if ((ballX >= blockX1 - 10) and (ballX < (blockX1 + 113))):
        if blockY1 - ballY <= -18 and blockY1 -ballY>=-34:
            ballY_change = -1
            ballY += ballY_change
        else:
            ballY_change += 0.3
            ballY += ballY_change





    elif ((ballX >= blockX2 - 10) and (ballX < (blockX2 + 113))):

        if blockY2 - ballY <= -18 and blockY2-ballY >= -34 :
            ballY_change = -1
            ballY += ballY_change

        else:
            ballY_change += 0.3
            ballY += ballY_change


    elif ((ballX >= blockX3 - 10) and (ballX < (blockX3 + 113))):

        if blockY3 - ballY <= -18 and blockY3 - ballY >= -34:
            ballY_change = -1
            ballY += ballY_change

        else:
            ballY_change += 0.3
            ballY += ballY_change



    elif ((ballX >= blockX4 - 10) and (ballX < (blockX4 + 113))):

        if blockY4 - ballY <= -18 and blockY4-ballY >=-34:
            ballY_change = -1
            ballY += ballY_change

        else:
            ballY_change += 0.3
            ballY += ballY_change



    elif ((ballX >= nailedX1 - 10) and (ballX < (nailedX1 + 113))):
        if nailedY1 - ballY <= 35 and nailedY1-ballY >=-34:
            ballY_change = -1
            ballY += ballY_change
            if lives > 0:
                lives_decreased = 1
                lives = lives - lives_decreased
                ballX = ballX_ini
                ballY = ballY_ini
                blockX1 = blockX1_ini
                blockY1 = blockY1_ini

                blockX2 = blockX2_ini
                blockY2 = blockY2_ini

                blockX3 = blockX3_ini
                blockY3 = blockY3_ini

                blockX4 = blockX4_ini
                blockY4 = blockY4_ini

                nailedX1 = nailedX1_ini
                nailedY1 = nailedY1_ini
            else:
                End()

        else:
            ballY_change += 0.3
            ballY += ballY_change




    else:
        ballY_change += 0.3
        ballY += ballY_change

        if (ballY > 20 and ballY <= 800):
            score_value += 1

    # Collision between ball and extraPoint
    collision = iscollision(ballX, ballY, extrapointX, extrapointY)
    if collision:
        score_value += 100
        extrapointX = random.randint(200, 650)
        extrapointY = random.randint(200, 400)

    extraPoint(extrapointX, extrapointY)

    # Collision between ball and livesKiller

    killerCollision = iscollision(ballX, ballY, liveskillerX[i], liveskillerY[i])
    if killerCollision:

        lives -= 1
        if lives <= 0:
            End()

        liveskillerX[i] = random.randint(200, 650)
        liveskillerY[i] = random.randint(200, 400)

    livesKiller(liveskillerX[i], liveskillerY[i],i)

    # block1 movement
    blockY1_change = -1
    blockY1 += blockY1_change

    # block1 repetition
    if blockY1 <= 0:
        blockY1 = 600
        blockY1_change = 0

    # block2 movement
    blockY2_change = - 1
    blockY2 += blockY2_change

    # block2 repetition
    if blockY2 <= -10:
        blockY2 = 600
        blockY2_change = 0

    # block3 movement
    blockY3_change = -1
    blockY3 += blockY3_change

    # block3 repetition
    if blockY3 <= -10:
        blockY3 = 600
        blockY3_change = 0
    # block4 movement
    blockY4_change = -1
    blockY4 += blockY4_change

    # block4 repetition
    if blockY4 <= -17:
        blockY4 = 600
        blockY4_change = 0

    # nailed block movement
    nailedY1_change = -1
    nailedY1 += nailedY1_change

    # nailed block repetition
    if nailedY1 <= 30:
        nailedY1 = 600
        nailedY1_change = 0

    if (ballY < 20 or ballY >= 600):

        if lives > 0:
            lives_decreased = 1
            lives = lives - lives_decreased
            ballX = ballX_ini
            ballY = ballY_ini
            blockX1 = blockX1_ini
            blockY1 = blockY1_ini

            blockX2 = blockX2_ini
            blockY2 = blockY2_ini

            blockX3 = blockX3_ini
            blockY3 = blockY3_ini

            blockX4 = blockX4_ini
            blockY4 = blockY4_ini

            nailedX1 = nailedX1_ini
            nailedY1 = nailedY1_ini

        else:
            End()

    # Function call
    block(blockX1, blockY1)
    block(blockX2, blockY2)
    block(blockX3, blockY3)
    block(blockX4, blockY4)

    nailedblock(nailedX1, nailedY1)
    ball(ballX, ballY)
    show_score(testX, testY)

    lives_text()

    pygame.display.update()
    #CLOCK.tick(60)

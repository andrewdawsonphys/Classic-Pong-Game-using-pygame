import pygame
from Paddle import Paddle
from Ball import Ball
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)

# Open a window
size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE,10,100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE,10,100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

# This will be a list that will contain all the sprites

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# Loop with carry on untill user exits the pygame
carryOn = True

# Initialise player score
scoreA = 0
scoreB = 0

clock = pygame.time.Clock()

# -------- Main Program Loop --------
while carryOn:
    # ----- Main event Loop -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_x:
                carryOn=False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(30)
        if keys[pygame.K_s]:
            paddleA.moveDown(30)
        if keys[pygame.K_UP]:
            paddleB.moveUp(30)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(30)
    # ----- Game Logic -----

    all_sprites_list.update()

    # -- Check if the ball hits any of the sides of the screen
    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    # Check for collisions between the ball and the paddle
    if pygame.sprite.collide_mask(ball,paddleA) or pygame.sprite.collide_mask(ball,paddleB):
        ball.bounce()

    screen.fill(BLACK)
    pygame.draw.line(screen,WHITE,[349,0], [349,500], 5)

    #--- Go ahead and draws the sprites to the screen in one go ---
    all_sprites_list.draw(screen)

    # Display the score board
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text,(250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text,(420,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

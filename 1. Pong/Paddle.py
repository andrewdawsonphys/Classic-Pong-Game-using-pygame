import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    # this class represents a paddle. It derives from sprite class in pygamw

    def __init__(self,color,width,height):
        # constructor method
        #call the parent class (sprite) constructor
        super().__init__()

        #Pass in the color of the paddle, and its x and y positions, width and height
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the Paddle
        pygame.draw.rect(self.image,color,[0,0,width, height])

        # Fetch the rectangle object that has dimensions of the image
        self.rect = self.image.get_rect();

    def moveUp(self,pixels):
        self.rect.y -= pixels
    # Check that you are not going too far off screen
        if self.rect.y  > 400:
            self.rect.y = 400

    def moveDown(self,pixels):
        self.rect.y += pixels
        # Check that you are not going too far off screen
        if self.rect.y < 0:
            self.rect.y = 0

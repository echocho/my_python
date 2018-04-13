import pygame
pygame.init()

WHITE = (255,255,255)

class Car(pygame.sprite.Sprite):
     #This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height, speed):
        
        # Call the parent class (Sprite) constructor
        super().__init__() 

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # initialize attributes of the car
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        
        # draw the car
        pygame.draw.rect(self.image, color, [0, 0, self.width, self.height])

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
    
    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
    
    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20
    
    def changeSpeed(self, speed):
        self.speed = speed
    
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        
 

import pygame, random
from car import Car
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

speed = 1
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

screenWidth = 800
screenHeight = 600

size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Car Racing')

all_sprites_list = pygame.sprite.Group()

playerCar = Car(RED, 60, 80, 70)
playerCar.rect.x = 160
playerCar.rect.y = screenHeight - 100

car1 = Car(PURPLE, 60, 80, random.randint(50, 100))
car1.rect.x = 60
car1.rect.y = -100

car2 = Car(YELLOW, 60, 80, random.randint(50, 100))
car2.rect.x = 160
car2.rect.y = -600

car3 = Car(CYAN, 60, 80, random.randint(50, 100))
car3.rect.x = 260
car3.rect.y = -300

car4 = Car(BLUE, 60, 80, random.randint(50, 100))
car4.rect.x = 360
car4.rect.y = -900

all_sprites_list.add(playerCar)
all_sprites_list.add(car1)
all_sprites_list.add(car2)
all_sprites_list.add(car3)
all_sprites_list.add(car4)

all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)

carryOn = True
clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  #something wrong with this command
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
    if keys[pygame.K_UP]:
        speed += 0.05
    if keys[pygame.K_DOWN]:
        speed -= 0.05
    
    for car in all_coming_cars:
        car.moveForward(speed)
        if car.rect.y > screenHeight:
            car.changeSpeed(random.randint(50, 100))
            car.repaint(random.choice(colorList))
            car.rect.y = -200
    
    # check if there is a car collision
    car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)
    for car in car_collision_list:
        print('Car Crash!')
        carryOn = False

    all_sprites_list.update()

    screen.fill(GREEN)
    # draw the road
    pygame.draw.rect(screen, GREY, [40, 0, 400, 600])
    # draw the line painting on the road
    pygame.draw.lines(screen, WHITE, False, [(140,0), (140, screenHeight)], 5)
    # draw the line painting on the road
    pygame.draw.lines(screen, WHITE, False, [(240,0), (240, screenHeight)], 5)
    # draw the line painting on the road
    pygame.draw.lines(screen, WHITE, False, [(340,0), (340, screenHeight)], 5)

    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()






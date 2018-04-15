import pygame, random
pygame.init()

BLACK = (0, 0, 0)
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

size = (800, 800)
screen = pygame.display.set_mode(size)

bodyList = []
foodList = []
        
carryOn = True

clock = pygame.time.Clock()

# set the first snake rect
x = 80
y = 80

# set the snake length
while x <= 160:
    x += 10
    bodyList.append((x, y)) 

# set food
food_x = random.randint(20, 770)
food_y = random.randint(20, 770)
foodList.append((food_x, food_y))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    
    screen.fill(BLACK)
    
    # draw border
    pygame.draw.rect(screen, GREEN, [0, 0, 800, 20])
    pygame.draw.rect(screen, GREEN, [0, 0, 20, 800])
    pygame.draw.rect(screen, GREEN, [0, 780, 800, 20])
    pygame.draw.rect(screen, GREEN, [780, 0, 20, 800])


    keys = pygame.key.get_pressed()

    head_x = bodyList[-1][0]
    head_y = bodyList[-1][1]
    right_new_head_x = head_x + 10
    right_new_head_y = head_y
    left_new_head_x = head_x - 10
    left_new_head_y = head_y
    up_new_head_x = head_x
    up_new_head_y = head_y - 10
    down_new_head_x = head_x
    down_new_head_y = head_y + 10

    if keys[pygame.K_RIGHT]:
        bodyList.pop(0)
        bodyList.append((right_new_head_x, right_new_head_y))
        

    if keys[pygame.K_LEFT]:
        bodyList.pop(0)
        bodyList.append((left_new_head_x, left_new_head_y))

    if keys[pygame.K_UP]:
        bodyList.pop(0)
        bodyList.append((up_new_head_x, up_new_head_y))

    if keys[pygame.K_DOWN]:
        bodyList.pop(0)
        bodyList.append((down_new_head_x, down_new_head_y))

    
    # generate new food after snake eats it
    # better use sprite collision!! 

    while (food_x, food_y) in bodyList or food_x % 10 != 0 or food_y % 10 != 0:
        if (food_x, food_y) in bodyList:
            bodyList.append((food_x, food_y))
        food_x = random.randint(20, 770)
        food_y = random.randint(20, 770)
        foodList.pop(0)
        foodList.append((food_x, food_y))

    for m in range(0, len(foodList)):
        pygame.draw.rect(screen, RED, [foodList[0][0], foodList[0][1], 10, 10])
    
    for i in range(0, len(bodyList)):
        pygame.draw.rect(screen, WHITE, [bodyList[i][0], bodyList[i][1], 10, 10])
    
    for q in range(0, len(bodyList)):
        if bodyList[q][0] < 20 or bodyList[q][0] >= 780 or bodyList[q][1] < 20 or bodyList[q][1] >= 780:
            carryOn = False
            print('Game Over')
            print('Final Score: ', len(bodyList)-9)

    print('after eating: ', len(bodyList))
    print(bodyList)
    print(foodList)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
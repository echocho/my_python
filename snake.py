import pygame, random, copy
pygame.init()

# -------------------
# -------------------
# CUSTOMIZED AREA
GAME_AREA_SIZE = (800, 800)
FOOD_AREA_WIDE = 20
FOOD_AREA_HEIGHT = 760
SNAKE_RECT_LEN = 10
INITIAL_SNAKE_LEN = 360
BLACK = (0, 0, 0)
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)

# FIXME: will fix dotted snake when change of speed
SPEED = 10
# -------------------
# -------------------
screen = pygame.display.set_mode(GAME_AREA_SIZE)
carryOn = True
clock = pygame.time.Clock()

# bodyList to keep record of positions every rect of the snake
bodyList = []
# foodList to record position of the food
foodList = []

# set the first snake rect
initial_tail_x_pos = 80
initial_tail_y_pos = 80

# duplicating intial tail as initial snake length:
while initial_tail_x_pos < INITIAL_SNAKE_LEN:
    initial_tail_x_pos += SNAKE_RECT_LEN
    bodyList.append((initial_tail_x_pos, initial_tail_y_pos)) 

  # set food
food_x_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
food_y_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
foodList.append((food_x_pos, food_y_pos))

# main program loop
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

    #  keys control
    keys = pygame.key.get_pressed()

    head_x_pos = bodyList[-1][0]
    head_y_pos = bodyList[-1][1]

    if keys[pygame.K_RIGHT]:
        head_x_pos += SPEED
        bodyList.pop(0)
        bodyList.append((head_x_pos, head_y_pos))

    if keys[pygame.K_LEFT]:
        head_x_pos -= SPEED
        bodyList.pop(0)
        bodyList.append((head_x_pos, head_y_pos))

    if keys[pygame.K_UP]:
        head_y_pos -= SPEED
        bodyList.pop(0)
        bodyList.append((head_x_pos, head_y_pos))

    if keys[pygame.K_DOWN]:
        head_y_pos += SPEED
        bodyList.pop(0)
        bodyList.append((head_x_pos, head_y_pos))

    # set food pool 
    while (food_x_pos, food_y_pos) in bodyList or food_x_pos % 10 != 0 or food_y_pos % 10 != 0:
        if (food_x_pos, food_y_pos) in bodyList:
            bodyList.append((food_x_pos, food_y_pos))
        food_x_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
        food_y_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
        foodList.pop(0)
        foodList.append((food_x_pos, food_y_pos))

    # draw food -- there's always only one food in foodList
    pygame.draw.rect(screen, RED, [foodList[0][0], foodList[0][1], 10, 10])

    # draw snake 
    for (snake_rect_x_pos, snake_rect_y_pos) in bodyList:
        pygame.draw.rect(screen, WHITE, [snake_rect_x_pos, snake_rect_y_pos, 10, 10])

    # check if snake hits border
    for (snake_rect_x_pos, snake_rect_y_pos) in bodyList:
        if snake_rect_x_pos < FOOD_AREA_WIDE or snake_rect_x_pos >= FOOD_AREA_HEIGHT or snake_rect_y_pos < FOOD_AREA_WIDE or snake_rect_y_pos >= FOOD_AREA_HEIGHT:
            print('hit border-game over')
            carryOn = False

    # check if snake hits itself:
    if bodyList[-1] in bodyList[:-2]:
        print('hit itself-game over')
        carryOn = False

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
import pygame, random, copy
pygame.init()

# -------------------
# -------------------
# CUSTOMIZED AREA
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BORDER_THICKNESS = 20
FOOD_AREA_WIDE = BORDER_THICKNESS
FOOD_AREA_HEIGHT = SCREEN_HEIGHT - 3*BORDER_THICKNESS
SNAKE_RECT_LEN = 5
INITIAL_SNAKE_LEN = 200
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
SPEED = 5
# -------------------
# -------------------
screen = pygame.display.set_mode(SCREEN_SIZE)
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
print(len(bodyList))
print(bodyList)

  # set food
food_x_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
food_y_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
foodList.append((food_x_pos, food_y_pos))

direction_vector = (1, 0)

# main program loop
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    screen.fill(BLACK)

    # draw border
    pygame.draw.rect(screen, GREEN, [0, 0, SCREEN_WIDTH, BORDER_THICKNESS])
    pygame.draw.rect(screen, GREEN, [0, 0, BORDER_THICKNESS, SCREEN_WIDTH])
    pygame.draw.rect(screen, GREEN, [0, SCREEN_HEIGHT - BORDER_THICKNESS, SCREEN_HEIGHT, BORDER_THICKNESS])
    pygame.draw.rect(screen, GREEN, [SCREEN_WIDTH - BORDER_THICKNESS, 0, BORDER_THICKNESS, SCREEN_HEIGHT])

    #  keys control
    keys = pygame.key.get_pressed()

    head_x_pos = bodyList[-1][0]
    head_y_pos = bodyList[-1][1]
 
    # check direction and limit opposite direction 
    new_direction_vector = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])
    if new_direction_vector != (0, 0) and [sum(x) for x in zip(new_direction_vector, direction_vector)] != [0,0]:
        direction_vector = new_direction_vector 
    bodyList.append((head_x_pos + direction_vector[0] * SPEED, head_y_pos + direction_vector[1] * SPEED))

    # set food pool 
    while (food_x_pos, food_y_pos) in bodyList or food_x_pos % 5 != 0 or food_y_pos % 5 != 0:
        if (food_x_pos, food_y_pos) in bodyList:
            bodyList = [(food_x_pos, food_y_pos)] + bodyList
            print((food_x_pos, food_y_pos))
            print(len(bodyList))
            print(bodyList)
        food_x_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
        food_y_pos = random.randint(FOOD_AREA_WIDE, FOOD_AREA_HEIGHT)
        foodList.pop(0)
        foodList.append((food_x_pos, food_y_pos))

    # draw food -- there's always only one food in foodList
    pygame.draw.rect(screen, RED, [foodList[0][0], foodList[0][1], 10, 10])
    bodyList.pop(0)
    # draw snake 
    for (snake_rect_x_pos, snake_rect_y_pos) in bodyList:
        pygame.draw.rect(screen, WHITE, [snake_rect_x_pos, snake_rect_y_pos, 10, 10])

    # check if snake hits border
    for (snake_rect_x_pos, snake_rect_y_pos) in bodyList:
        if snake_rect_x_pos < FOOD_AREA_WIDE or snake_rect_x_pos >= FOOD_AREA_HEIGHT or snake_rect_y_pos < FOOD_AREA_WIDE or snake_rect_y_pos >= FOOD_AREA_HEIGHT:
            print('hit border-game over')
            carryOn = False

    # check if snake collaps with itself:
    if bodyList[-1] in bodyList[:-1]:
        print('hit itself-game over')
        carryOn = False
    
    pygame.display.flip()
    clock.tick(35)


pygame.quit()
import pygame, random, time
pygame.init()

# -------------------
# -------------------
# CUSTOMIZED AREA
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BORDER_THICKNESS = 20
FOOD_AREA_WIDE = BORDER_THICKNESS
FOOD_AREA_HEIGHT = SCREEN_HEIGHT - 1.5*BORDER_THICKNESS
SNAKE_RECT_LEN = 5
INITIAL_SNAKE_LEN = 200
BLACK = (0, 0, 0)
GREEN = (20, 255, 140)
LIGHT_GREY = (210, 210, 210)
GREY = (190, 190, 190)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
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

def gameOver():
    message_display('Game Over!')
 
def message_display(text):
    set_textFont = pygame.font.Font('freesansbold.ttf',65)
    textSurface, textArea = text_objects(text, set_textFont)
    textArea.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(textSurface, textArea)
 
    pygame.display.update()
 
    time.sleep(3)

def text_objects(text, font):
    textSurface = font.render(text, True, GREY)
    return textSurface, textSurface.get_rect()

def botton_text_objects(text, font, color= None):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect() 

def start_botton():
    pygame.draw.rect(screen, GREY, [100, 350, 100, 50])
    # add mouse interaction
    mouse = pygame.mouse.get_pos()
    if 100+100 > mouse[0] > 100 and 350+50 > mouse[1] > 350:
        pygame.draw.rect(screen, LIGHT_GREY, [100, 350, 100, 50])
    set_textFont = pygame.font.Font('freesansbold.ttf', 25)
    textSurface, textArea = botton_text_objects('START', set_textFont)
    textArea.center = (150,380)
    screen.blit(textSurface, textArea)

def quit_botton():
    pygame.draw.rect(screen, GREY, [300, 350, 100, 50])
    # add mouse interaction
    mouse = pygame.mouse.get_pos()
    if 300+100 > mouse[0] > 300 and 350+50 > mouse[1] > 350:
        pygame.draw.rect(screen, LIGHT_GREY, [300, 350, 100, 50])
    set_font = pygame.font.Font('freesansbold.ttf', 25)
    textSurface, textArea = botton_text_objects('QUIT', set_font)
    textArea.center = (350,380)
    screen.blit(textSurface, textArea)


        






def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(BLACK)
        set_textFont = pygame.font.Font('freesansbold.ttf', 40)
        textSurface, textArea = text_objects('Snake of Simplicity', set_textFont)
        textArea.center = ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/4))
        screen.blit(textSurface, textArea)
        # draw start and quit buttons
        start_botton()
        quit_botton()
            
        pygame.display.update()
        clock.tick(15)
        #-----------------
        # Question and experiment:
        # Or we could change message_display() abit and use "message_display('Snake of Simplicity')" instead?
        #-----------------   
game_intro()

        





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
        if snake_rect_x_pos < BORDER_THICKNESS or snake_rect_x_pos > SCREEN_WIDTH-BORDER_THICKNESS or snake_rect_y_pos < BORDER_THICKNESS or snake_rect_y_pos > SCREEN_HEIGHT-BORDER_THICKNESS:
            print('hit border-game over')
            gameOver()
            carryOn = False

    # check if snake collaps with itself:
    if bodyList[-1] in bodyList[:-1]:
        print('hit itself-game over')
        gameOver
        carryOn = False
    
    pygame.display.flip()
    clock.tick(35)


pygame.quit()
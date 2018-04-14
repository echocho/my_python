import pygame, random
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)

size = (800, 800)
screen = pygame.display.set_mode(size)

bodyList = []
        
carryOn = True

clock = pygame.time.Clock()

x = 20
y = 20

# draw the snake
pygame.draw.rect(screen, WHITE, [x, y, 10, 10])
pygame.draw.rect(screen, WHITE, [x+10, y, 10, 10])
pygame.draw.rect(screen, WHITE, [x+20, y, 10, 10])
pygame.draw.rect(screen, WHITE, [x+30, y, 10, 10])
bodyList.append((x,y))
bodyList.append((x+10, y))
bodyList.append((x+20, y))
bodyList.append((x+30, y))

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    

    screen.fill(BLACK)
    
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
    
    print(bodyList)

    for i in range(0, len(bodyList)):
        pygame.draw.rect(screen, WHITE, [bodyList[i][0], bodyList[i][1], 10, 10])
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()

    

    


    







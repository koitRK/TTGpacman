import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("PACMAN")

x = 50
y = 50
diameter = 10
vel = 2

direction = "LEFT"
run = True
while run:
    pygame.time.delay(15)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    
    
    
    if keys[pygame.K_LEFT]:
        direction = "LEFT"
    if keys[pygame.K_RIGHT]:
        direction = "RIGHT"
    if keys[pygame.K_UP]:
        direction = "UP"
    if keys[pygame.K_DOWN]:
        direction = "DOWN"

    if direction is "LEFT":
        x -= vel
    elif direction is "RIGHT":
        x += vel
    elif direction is "UP":
        y -= vel        
    elif direction is "DOWN":
        y += vel
        
    print("x =", x, "   y =", y)
    window.fill((0, 0, 0))
    pygame.draw.circle(window, (200, 200, 0), (x, y), diameter)
    pygame.display.update()
    
pygame.quit()
        
        
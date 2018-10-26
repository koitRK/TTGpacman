import pygame

sinine = (0, 0, 255)

def main():
    
    pygame.init()

    pygame.display.set_caption('PACMAN')

    screen = pygame.display.set_mode((500, 500))

    serv_surface = pygame.Surface((20, 500))
    serv_surface.fill(sinine)
    screen.blit(serv_surface, (0, 0))
    screen.blit(serv_surface, (480, 0))
    
    serv_surface = pygame.Surface((500, 20))
    serv_surface.fill(sinine)
    screen.blit(serv_surface, (0,480))
    screen.blit(serv_surface, (0,0))
    
    blokk_surface = pygame.Surface((60,40))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (40,40))
    screen.blit(blokk_surface, (400,40))
    
    blokk_surface = pygame.Surface((100,40))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (120,40))
    screen.blit(blokk_surface, (280,40))
    
    blokk_surface = pygame.Surface((60,20))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (40,100))
    screen.blit(blokk_surface, (40,200))
    screen.blit(blokk_surface, (400, 100))
    screen.blit(blokk_surface, (400, 200))
    screen.blit(blokk_surface, (160,180))
    screen.blit(blokk_surface, (280,180))
    
    blokk_surface = pygame.Surface((20,60))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (240,20))
    screen.blit(blokk_surface, (240,100))
    
    blokk_surface = pygame.Surface((180,20))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (160,100))
    screen.blit(blokk_surface, (160,300))
    
    blokk_surface = pygame.Surface((20,100))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (120,200))
    screen.blit(blokk_surface, (160,200))
    screen.blit(blokk_surface, (320,200))
    screen.blit(blokk_surface, (360,200))
    screen.blit(blokk_surface, (120,320))
    screen.blit(blokk_surface, (360,320))
    
    blokk_surface = pygame.Surface((80,40))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (20,140))
    screen.blit(blokk_surface, (400,140))
    
    blokk_surface = pygame.Surface((20,80))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (120,100))
    screen.blit(blokk_surface, (360,100))
    
    blokk_surface = pygame.Surface((80,20))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (140,140))
    screen.blit(blokk_surface, (280,140))
    screen.blit(blokk_surface, (20,240))
    screen.blit(blokk_surface, (400,240))
    
    blokk_surface = pygame.Surface((60,180))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (40,280))
    screen.blit(blokk_surface, (400,280))
    
    blokk_surface = pygame.Surface((260,20))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (120,440))
    
    blokk_surface = pygame.Surface((180,80))
    blokk_surface.fill(sinine)
    screen.blit(blokk_surface, (160,340))
    
    pygame.display.flip()

    while True:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            break

    pygame.quit()

if __name__ == '__main__':
    main()
import pygame
import random
pygame.init()

winsize = 570  #Akna suurus, default 570, yks blokk on 30px * 30px, 19 * 19 blokki
window = pygame.display.set_mode((winsize, winsize))  #loob uue akna

walls = pygame.image.load("walls1.png")  #load labyrindi pilt/taust
window.blit(walls, (0, 0))  #asetab labyrindi/tausta koordinaatidele 0, 0
pygame.display.update()




class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

for n in range(50):
    pygame.draw.rect(window, (255, 255, 255), [n * 5, n * 5, 10, 10], 5)






run = True
while run:  #kordab igavesti
    
    pygame.time.delay(5)  #Aeg iga kaardi vahel. SIIN SAAB KIIRUST MUUTA. Default 5ms
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
 
    window.fill((0, 0, 0))  #taust mustaks
    
    for n in range(50):
        pygame.draw.rect(window, (255, 255, 255), [n * 5, n * 5, 10, 10], 5)

    window.blit(walls, (0, 0))  #lisa labyrint
    pygame.display.update() #update display
    
pygame.quit()
        
        



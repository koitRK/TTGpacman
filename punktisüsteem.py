import pygame
pygame.init()

winsize = 570  #Akna suurus, default 570, yks blokk on 30px * 30px, 19 * 19 blokki
window = pygame.display.set_mode((winsize, winsize))  #loob uue akna
pygame.display.set_caption("PACMAN")  #akna nimetus

x = 30  #alguskoordinaat x
y = 30  #alguskoordinaat y
diameter = 30  #pacmani suurus pikslites
vel = 1 #pacmani kiirus !!! PEAB OLEMA 1 !!!



# pacman colliders
tl = False  #topleft
tr = False  #topright
lt = False  #lefttop
lb = False  #leftbottom
rt = False  #righttop
rb = False  #rightbottom
bl = False  #bottomleft
br = False  #bottomright


walls = pygame.image.load("walls.png")  #load labyrindi pilt/taust
window.blit(walls, (0, 0))  #asetab labyrindi/tausta koordinaatidele 0, 0
wallmask = pygame.mask.from_surface(walls)  #teeb labyrindist maski, et seda colliderina kasutada
rect1 = pygame.draw.rect(window, (255, 255, 255), [x, y, diameter, diameter])  #loob ja joonistab pacmani rectangle
pygame.display.update()


#netist leitud, vaatab, kas kaks objekti kattuvad. Return True or False
#u = esimese objekti punkt, v = terve teine object
def sub(u, v):
    return [ u[i]-v[i] for i in range(len(u)) ]




direction = "STILL"  #pacman seisab alguses paigal
nextdirection = "STILL"  #pacman seisab alguses paigal

run = True
while run:  #kordab igavesti
    
    pygame.time.delay(5)  #Aeg iga kaardi vahel. SIIN SAAB KIIRUST MUUTA. Default 5ms
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()  #Vaatab, milline klahv on vajutadud
    

    if keys[pygame.K_LEFT]:
        nextdirection = "LEFT"  #nextdirection = jargmine suund, kuhu tahetakse minna
    if keys[pygame.K_RIGHT]:
        nextdirection = "RIGHT"
    if keys[pygame.K_UP]:
        nextdirection = "UP"
    if keys[pygame.K_DOWN]:
        nextdirection = "DOWN"


    #colliderid...  
    rel_point = sub((x, y - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tl = True
    else:
        tl = False               
    rel_point = sub((x + diameter - 1, y - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tr = True
    else:
        tr = False
    rel_point = sub((x - 1, y), [0, 0])
    if wallmask.get_at(rel_point): 
        lt = True
    else:
        lt = False        
    rel_point = sub((x - 1, y + diameter - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        lb = True
    else:
        lb = False           
    rel_point = sub((x + diameter, y), [0, 0])
    if wallmask.get_at(rel_point): 
        rt = True
    else:
        rt = False        
    rel_point = sub((x + diameter, y + diameter - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        rb = True
    else:
        rb = False            
    rel_point = sub((x, y + diameter), [0, 0])
    if wallmask.get_at(rel_point): 
        bl = True
    else:
        bl = False        
    rel_point = sub((x + diameter - 1, y + diameter), [0, 0])
    if wallmask.get_at(rel_point): 
        br = True
    else:
        br = False 
    

        
    
    #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection is "LEFT") and not (lt or lb):
        direction = nextdirection
    elif (nextdirection is "RIGHT") and not (rt or rb):
        direction = nextdirection
    elif (nextdirection is "UP") and not (tl or tr):
        direction = nextdirection       
    elif (nextdirection is "DOWN") and not (bl or br):
        direction = nextdirection
    
    #kui pacman liigus yhes suunas ja sein tuleb ette (colliderid = True), direction = still
    elif ((direction is "LEFT") and (lt or lb)):
        direction = "STILL"    
    elif ((direction is "RIGHT") and (rt or rb)):
        direction = "STILL" 
    elif ((direction is "UP") and (tl or tr)):
        direction = "STILL" 
    elif ((direction is "DOWN") and (bl or br)):
        direction = "STILL" 
        
    else:
        pass
  
        
        
    #pacmani liigutamine soltuvalt suunast(direction)    
    if direction is "LEFT":
        x -= vel
    elif direction is "RIGHT":
        x += vel        
    elif direction is "UP":
        y -= vel    
    elif direction is "DOWN":
        y += vel
    elif direction is "STILL":
        y = y
        x = x

    #print("x =", x, " y =", y, "   ",  "  tl=", tl,"  tr=", tr,"  lt=", lt,"  lb=", lb,"  rt=", rt,"  rb=", rb,"  bl=", bl,"  br=", br,)
    
    window.fill((0, 0, 0))  #taust mustaks
    window.blit(walls, (0, 0))  #lisa labyrint
    rect1 = pygame.draw.rect(window, (255, 255, 255), [x, y, diameter, diameter])  #loo/joonista pacman
    

    punkt = pygame.image.load("punkt.png")
    
        if ((x * 0.13) + y != 63.9):
            window.blit(punkt, (41, 71))
    
    pygame.display.update() #update display

pygame.quit()

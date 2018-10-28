import pygame
import random
pygame.init()

winsize = 570  #Akna suurus, default 570, yks blokk on 30px * 30px, 19 * 19 blokki
window = pygame.display.set_mode((winsize, winsize))  #loob uue akna

pygame.display.set_caption("PACMAN")  #akna nimetus

level = 1
x = 270 #pacmani koordinaat x, alguses 270
y = 330  #pacmani koordinaat y, alguses 330
diameter = 30  #pacmani suurus pikslites
ghostsize = 30
ghostturntime = 125  #ghost muudab suunda iga x pixli tagant

i1 = 0  #ghost 1 counter
xg1 = 240  #ghost 1 position x
yg1 = 270  #ghost 1 position y

i2 = 0  #ghost 2 counter
xg2 = 270  #ghost 2 position x
yg2 = 270  #ghost 2 position y

i3 = 0  #ghost 3 counter
xg3 = 300  #ghost 3 position x
yg3 = 270  #ghost 3 position y

vel = 1 #pacmani kiirus !!! PEAB OLEMA 1 !!!

directionlist1 = ["LEFT", "RIGHT", "UP", "DOWN"]
directionlist2 = ["LEFT", "RIGHT", "UP", "DOWN"]
directionlist3 = ["LEFT", "RIGHT", "UP", "DOWN"]


# pacman colliders
tl = False  #topleft
tr = False  #topright
lt = False  #lefttop
lb = False  #leftbottom
rt = False  #righttop
rb = False  #rightbottom
bl = False  #bottomleft
br = False  #bottomright

# ghost1 colliders
tl1 = False  #topleft
tr1 = False  #topright
lt1 = False  #lefttop
lb1 = False  #leftbottom
rt1 = False  #righttop
rb1 = False  #rightbottom
bl1 = False  #bottomleft
br1 = False  #bottomright

# ghost2 colliders
tl2 = False  #topleft
tr2 = False  #topright
lt2 = False  #lefttop
lb2 = False  #leftbottom
rt2 = False  #righttop
rb2 = False  #rightbottom
bl2 = False  #bottomleft
br2 = False  #bottomright

# ghost3 colliders
tl3 = False  #topleft
tr3 = False  #topright
lt3 = False  #lefttop
lb3 = False  #leftbottom
rt3 = False  #righttop
rb3 = False  #rightbottom
bl3 = False  #bottomleft
br3 = False  #bottomright

level = input("Vali level: 1, 2, 3, 4")


walls = pygame.image.load("walls" + level + ".png")  #load labyrindi pilt/taust
window.blit(walls, (0, 0))  #asetab labyrindi/tausta koordinaatidele 0, 0
wallmask = pygame.mask.from_surface(walls)  #teeb labyrindist maski, et seda colliderina kasutada
rect1 = pygame.draw.rect(window, (255, 255, 0), [x, y, diameter, diameter])  #loob ja joonistab pacmani rectangle
ghost1 = pygame.draw.rect(window, (255, 0, 0), [xg1, yg1, ghostsize, ghostsize])
ghost2 = pygame.draw.rect(window, (255, 184, 255), [xg2, yg2, ghostsize, ghostsize])
ghost3 = pygame.draw.rect(window, (255, 184, 82), [xg3, yg3, ghostsize, ghostsize])
pygame.display.update()


#netist leitud, vaatab, kas kaks objekti kattuvad. Return True or False
#u = esimese objekti punkt, v = terve teine object
def sub(u, v):
    return [ u[i]-v[i] for i in range(len(u)) ]




direction = "STILL"  #pacman seisab alguses paigal
nextdirection = "STILL"  #pacman seisab alguses paigal
direction1 = "STILL"
nextdirection1 = "STILL"
direction2 = "STILL"
nextdirection2 = "STILL"
direction3 = "STILL"
nextdirection3 = "STILL"

run = True

def GameOver():
    print("GAME OVER")
    run = False


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


    
    #################################### P A C M A N #####################################
        
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
    else:
        pass
    
    if rect1.colliderect(ghost1) or rect1.colliderect(ghost2) or rect1.colliderect(ghost3):  #detect collision, Kui pacman puutub ghosti
        GameOver()
    
     
    #################################### P A C M A N #####################################
    #################################### G H O S T S #####################################
    #################################### G H O S T 1 #####################################
    
        #colliderid...  
    rel_point = sub((xg1, yg1 - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tl1 = True
    else:
        tl1 = False               
    rel_point = sub((xg1 + ghostsize - 1, yg1 - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tr1 = True
    else:
        tr1 = False
    rel_point = sub((xg1 - 1, yg1), [0, 0])
    if wallmask.get_at(rel_point): 
        lt1 = True
    else:
        lt1 = False        
    rel_point = sub((xg1 - 1, yg1 + ghostsize - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        lb1 = True
    else:
        lb1 = False           
    rel_point = sub((xg1 + ghostsize, yg1), [0, 0])
    if wallmask.get_at(rel_point): 
        rt1 = True
    else:
        rt1 = False        
    rel_point = sub((xg1 + ghostsize, yg1 + ghostsize - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        rb1 = True
    else:
        rb1 = False            
    rel_point = sub((xg1, yg1 + ghostsize), [0, 0])
    if wallmask.get_at(rel_point): 
        bl1 = True
    else:
        bl1 = False        
    rel_point = sub((xg1 + ghostsize - 1, yg1 + ghostsize), [0, 0])
    if wallmask.get_at(rel_point): 
        br1 = True
    else:
        br1 = False
        
        
    if i1 > ghostturntime:
        i1 = 0
        nextdirection1 = random.choice(directionlist1)
    else:
        i1 += 1
    
        
        #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection1 is "LEFT") and not (lt1 or lb1):
        direction1 = nextdirection1
    elif (nextdirection1 is "RIGHT") and not (rt1 or rb1):
        direction1 = nextdirection1
    elif (nextdirection1 is "UP") and not (tl1 or tr1):
        direction1 = nextdirection1       
    elif (nextdirection1 is "DOWN") and not (bl1 or br1):
        direction1 = nextdirection1
    
    #kui pacman liigus yhes suunas ja sein tuleb ette (colliderid = True), direction = still
    elif ((direction1 is "LEFT") and (lt1 or lb1)):
        direction1 = "STILL"
        directionlist1 = ["RIGHT", "UP", "DOWN"]
        i1 = ghostturntime
    elif ((direction1 is "RIGHT") and (rt1 or rb1)):
        direction1 = "STILL"
        directionlist1 = ["LEFT", "UP", "DOWN"]
        i1 = ghostturntime
    elif ((direction1 is "UP") and (tl1 or tr1)):
        direction1 = "STILL"
        directionlist1 = ["LEFT", "RIGHT", "DOWN"]
        i1 = ghostturntime
    elif ((direction1 is "DOWN") and (bl1 or br1)):
        direction1 = "STILL"
        directionlist1 = ["LEFT", "RIGHT", "UP"]
        i1 = ghostturntime
    else:
        pass
    
    if direction1 is "LEFT":
        xg1 -= vel
    elif direction1 is "RIGHT":
        xg1 += vel        
    elif direction1 is "UP":
        yg1 -= vel    
    elif direction1 is "DOWN":
        yg1 += vel
    elif direction1 is "STILL":
        yg1 = yg1
        xg1 = xg1
        i1 = ghostturntime + 1
    else:
        pass
    
    #################################### G H O S T 1 #####################################
    #################################### G H O S T 2 #####################################
    
        #colliderid...  
    rel_point = sub((xg2, yg2 - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tl2 = True
    else:
        tl2 = False               
    rel_point = sub((xg2 + ghostsize - 1, yg2 - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tr2 = True
    else:
        tr2 = False
    rel_point = sub((xg2 - 1, yg2), [0, 0])
    if wallmask.get_at(rel_point): 
        lt2 = True
    else:
        lt2 = False        
    rel_point = sub((xg2 - 1, yg2 + ghostsize - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        lb2 = True
    else:
        lb2 = False           
    rel_point = sub((xg2 + ghostsize, yg2), [0, 0])
    if wallmask.get_at(rel_point): 
        rt2 = True
    else:
        rt2 = False        
    rel_point = sub((xg2 + ghostsize, yg2 + ghostsize - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        rb2 = True
    else:
        rb2 = False            
    rel_point = sub((xg2, yg2 + ghostsize), [0, 0])
    if wallmask.get_at(rel_point): 
        bl2 = True
    else:
        bl2 = False        
    rel_point = sub((xg2 + ghostsize - 1, yg2 + ghostsize), [0, 0])
    if wallmask.get_at(rel_point): 
        br2 = True
    else:
        br2 = False
        
        
    if i2 > ghostturntime:
        i2 = 0
        nextdirection2 = random.choice(directionlist2)
    else:
        i2 += 1
    
        
        #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection2 is "LEFT") and not (lt2 or lb2):
        direction2 = nextdirection2
    elif (nextdirection2 is "RIGHT") and not (rt2 or rb2):
        direction2 = nextdirection2
    elif (nextdirection2 is "UP") and not (tl2 or tr2):
        direction2 = nextdirection2      
    elif (nextdirection2 is "DOWN") and not (bl2 or br2):
        direction2 = nextdirection2
    
    #kui pacman liigus yhes suunas ja sein tuleb ette (colliderid = True), direction = still
    elif ((direction2 is "LEFT") and (lt2 or lb2)):
        direction2 = "STILL"
        directionlist2 = ["RIGHT", "UP", "DOWN"]
        i2 = ghostturntime
    elif ((direction2 is "RIGHT") and (rt2 or rb2)):
        direction2 = "STILL"
        directionlist2 = ["LEFT", "UP", "DOWN"]
        i2 = ghostturntime
    elif ((direction2 is "UP") and (tl2 or tr2)):
        direction2 = "STILL"
        directionlist2 = ["LEFT", "RIGHT", "DOWN"]
        i2 = ghostturntime
    elif ((direction2 is "DOWN") and (bl2 or br2)):
        direction2 = "STILL"
        directionlist2 = ["LEFT", "RIGHT", "UP"]
        i2 = ghostturntime
    else:
        pass
    
    if direction2 is "LEFT":
        xg2 -= vel
    elif direction2 is "RIGHT":
        xg2 += vel        
    elif direction2 is "UP":
        yg2 -= vel    
    elif direction2 is "DOWN":
        yg2 += vel
    elif direction2 is "STILL":
        yg2 = yg2
        xg2 = xg2
        i2 = ghostturntime + 1
    else:
        pass
    
    #################################### G H O S T 2 #####################################
    #################################### G H O S T 3 #####################################
    
        #colliderid...  
    rel_point = sub((xg3, yg3 - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tl3 = True
    else:
        tl3 = False               
    rel_point = sub((xg3 + ghostsize - 1, yg3 - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tr3 = True
    else:
        tr3 = False
    rel_point = sub((xg3 - 1, yg3), [0, 0])
    if wallmask.get_at(rel_point): 
        lt3 = True
    else:
        lt3 = False        
    rel_point = sub((xg3 - 1, yg3 + ghostsize - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        lb3 = True
    else:
        lb3 = False           
    rel_point = sub((xg3 + ghostsize, yg3), [0, 0])
    if wallmask.get_at(rel_point): 
        rt3 = True
    else:
        rt3 = False        
    rel_point = sub((xg3 + ghostsize, yg3 + ghostsize - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        rb3 = True
    else:
        rb3 = False            
    rel_point = sub((xg3, yg3 + ghostsize), [0, 0])
    if wallmask.get_at(rel_point): 
        bl3 = True
    else:
        bl3 = False        
    rel_point = sub((xg3 + ghostsize - 1, yg3 + ghostsize), [0, 0])
    if wallmask.get_at(rel_point): 
        br3 = True
    else:
        br3 = False
        
        
    if i3 > ghostturntime:
        i3 = 0
        nextdirection3 = random.choice(directionlist3)
    else:
        i3 += 1
    
        
        #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection3 is "LEFT") and not (lt3 or lb3):
        direction3 = nextdirection3
    elif (nextdirection3 is "RIGHT") and not (rt3 or rb3):
        direction3 = nextdirection3
    elif (nextdirection3 is "UP") and not (tl3 or tr3):
        direction3 = nextdirection3      
    elif (nextdirection3 is "DOWN") and not (bl3 or br3):
        direction3 = nextdirection3
    
    #kui pacman liigus yhes suunas ja sein tuleb ette (colliderid = True), direction = still
    elif ((direction3 is "LEFT") and (lt3 or lb3)):
        direction3 = "STILL"
        directionlist3 = ["RIGHT", "UP", "DOWN"]
        i3 = ghostturntime
    elif ((direction3 is "RIGHT") and (rt3 or rb3)):
        direction3 = "STILL"
        directionlist3 = ["LEFT", "UP", "DOWN"]
        i3 = ghostturntime
    elif ((direction3 is "UP") and (tl3 or tr3)):
        direction3 = "STILL"
        directionlist3 = ["LEFT", "RIGHT", "DOWN"]
        i3 = ghostturntime
    elif ((direction3 is "DOWN") and (bl3 or br3)):
        direction3 = "STILL"
        directionlist3 = ["LEFT", "RIGHT", "UP"]
        i3 = ghostturntime
    else:
        pass
    
    if direction3 is "LEFT":
        xg3 -= vel
    elif direction3 is "RIGHT":
        xg3 += vel        
    elif direction3 is "UP":
        yg3 -= vel    
    elif direction3 is "DOWN":
        yg3 += vel
    elif direction3 is "STILL":
        yg3 = yg3
        xg3 = xg3
        i3 = ghostturntime + 1
    else:
        pass
    
    #################################### G H O S T 3 #####################################
    #################################### G H O S T S #####################################

    #print("x =", x, " y =", y, "   ",  "  tl=", tl,"  tr=", tr,"  lt=", lt,"  lb=", lb,"  rt=", rt,"  rb=", rb,"  bl=", bl,"  br=", br,)
    
    window.fill((0, 0, 0))  #taust mustaks
    window.blit(walls, (0, 0))  #lisa labyrint
    rect1 = pygame.draw.rect(window, (255, 255, 0), [x, y, diameter, diameter])  #loo/joonista pacman
    ghost1 = pygame.draw.rect(window, (255, 0, 0), [xg1, yg1, ghostsize, ghostsize])
    ghost2 = pygame.draw.rect(window, (255, 184, 255), [xg2, yg2, ghostsize, ghostsize])
    ghost3 = pygame.draw.rect(window, (255, 184, 82), [xg3, yg3, ghostsize, ghostsize])
    pygame.display.update() #update display
    
pygame.quit()
        
        


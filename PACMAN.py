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
rotation = 0
ghostsize = 30
ghostturntime = 100  #ghost muudab suunda iga x pixli tagant
score = 0





class Point(object):
    objs = []
    def __init__(self, xp, yp, elus, col):
        Point.objs.append(self)
        self.elus = True
        self.xp = xp
        self.yp = yp
        self.col = pygame.draw.rect(window, (255, 255, 255), [self.xp, self.yp, 3, 3])
        
    @classmethod
    def draw_all(cls):
        for obj in cls.objs:
            if obj.elus:
               obj.col = pygame.draw.rect(window, (255, 255, 255), [obj.xp, obj.yp, 3, 3])
        
    def collect(self):
        self.elus = False
        print("collect")
        
        
list = []
for n in range(19):
    for i in range(19):
        list.append(Point(15 + (30 * n), 15 + (30 * i), True, pygame.draw.rect(window, (255, 255, 255), [15 + (30 * n), 15 + (30 * i), 3, 3])))


pacmansheet = pygame.image.load("pacmansprite.gif").convert()
cells = []
for n in range(5):
    width, height = (30, 30)
    rect = pygame.Rect((n - 1) * width, 0, width, height)
    image = pygame.Surface(rect.size).convert()
    image.blit(pacmansheet, (0, 0), rect)
    alpha = image.get_at((0,0))
    image.set_colorkey(alpha)
    cells.append(image)
    
playerImg = cells[0]
frame = 1

ghost1sheet = pygame.image.load("ghost1.gif").convert()
cellsg1 = []
for n in range(3):
    width, height = (30, 30)
    rect = pygame.Rect((n - 1) * width, 0, width, height)
    image = pygame.Surface(rect.size).convert()
    image.blit(ghost1sheet, (0, 0), rect)
    alpha = image.get_at((0,0))
    image.set_colorkey(alpha)
    cellsg1.append(image)
    
ghost1Img = cellsg1[0]
frameg1 = 1

ghost2sheet = pygame.image.load("ghost2.gif").convert()
cellsg2 = []
for n in range(3):
    width, height = (30, 30)
    rect = pygame.Rect((n - 1) * width, 0, width, height)
    image = pygame.Surface(rect.size).convert()
    image.blit(ghost2sheet, (0, 0), rect)
    alpha = image.get_at((0,0))
    image.set_colorkey(alpha)
    cellsg2.append(image)
    
ghost2Img = cellsg2[0]
frameg2 = 1

ghost3sheet = pygame.image.load("ghost3.gif").convert()
cellsg3 = []
for n in range(3):
    width, height = (30, 30)
    rect = pygame.Rect((n - 1) * width, 0, width, height)
    image = pygame.Surface(rect.size).convert()
    image.blit(ghost3sheet, (0, 0), rect)
    alpha = image.get_at((0,0))
    image.set_colorkey(alpha)
    cellsg3.append(image)
    
ghost3Img = cellsg3[0]
frameg3 = 1


ghost4sheet = pygame.image.load("ghost4.gif").convert()
cellsg4 = []
for n in range(3):
    width, height = (30, 30)
    rect = pygame.Rect((n - 1) * width, 0, width, height)
    image = pygame.Surface(rect.size).convert()
    image.blit(ghost4sheet, (0, 0), rect)
    alpha = image.get_at((0,0))
    image.set_colorkey(alpha)
    cellsg4.append(image)
    
ghost4Img = cellsg4[0]
frameg4 = 1


temp = 1

player = playerImg.get_rect()
player.x = x
player.y = y

i1 = 0  #ghost 1 counter
xg1 = 240  #ghost 1 position x
yg1 = 270  #ghost 1 position y

i2 = 0  #ghost 2 counter
xg2 = 270  #ghost 2 position x
yg2 = 270  #ghost 2 position y

i3 = 0  #ghost 3 counter
xg3 = 300  #ghost 3 position x
yg3 = 270  #ghost 3 position y

i4 = 0  #ghost 4 counter
xg4 = 300  #ghost 4 position x
yg4 = 270  #ghost 4 position y

vel = 1 #pacmani kiirus !!! PEAB OLEMA 1 !!!

directionlist1 = ["LEFT", "RIGHT", "UP", "DOWN"]
directionlist2 = ["LEFT", "RIGHT", "UP", "DOWN"]
directionlist3 = ["LEFT", "RIGHT", "UP", "DOWN"]
directionlist4 = ["LEFT", "RIGHT", "UP", "DOWN"]


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

# ghost4 colliders
tl4 = False  #topleft
tr4 = False  #topright
lt4 = False  #lefttop
lb4 = False  #leftbottom
rt4 = False  #righttop
rb4 = False  #rightbottom
bl4 = False  #bottomleft
br4 = False  #bottomright

direction = "STILL"  #pacman seisab alguses paigal
nextdirection = "STILL"  #pacman seisab alguses paigal
direction1 = "STILL"
nextdirection1 = "STILL"
direction2 = "STILL"
nextdirection2 = "STILL"
direction3 = "STILL"
nextdirection3 = "STILL"
direction4 = "STILL"
nextdirection4 = "STILL"

level = input("Vali level: 1, 2, 3, 4")


walls = pygame.image.load("walls" + level + ".png")  #load labyrindi pilt/taust
window.blit(walls, (0, 0))  #asetab labyrindi/tausta koordinaatidele 0, 0
wallmask = pygame.mask.from_surface(walls)  #teeb labyrindist maski, et seda colliderina kasutada
rect1 = pygame.draw.rect(window, (255, 255, 0), [x, y, diameter, diameter])  #loob ja joonistab pacmani rectangle
rectcol = pygame.Rect(x + 10, y + 10, diameter - 20, diameter - 20)
ghost1 = pygame.draw.rect(window, (255, 0, 0), [xg1, yg1, ghostsize, ghostsize])
ghost2 = pygame.draw.rect(window, (255, 184, 255), [xg2, yg2, ghostsize, ghostsize])
ghost3 = pygame.draw.rect(window, (255, 184, 82), [xg3, yg3, ghostsize, ghostsize])
ghost4 = pygame.draw.rect(window, (0, 255, 255), [xg4, yg4, ghostsize, ghostsize])
pygame.display.update()


#netist leitud, vaatab, kas kaks objekti kattuvad.
#u = esimese objekti punkt, v = terve teine object
def sub(u, v):
    return [ u[i]-v[i] for i in range(len(u)) ]



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
        rotation = 180
        x -= vel
    elif direction is "RIGHT":
        x += vel
        rotation = 0
    elif direction is "UP":
        y -= vel
        rotation = 90
    elif direction is "DOWN":
        y += vel
        rotation = 270
    elif direction is "STILL":
        y = y
        x = x
    else:
        pass
    
    if rectcol.colliderect(ghost1) or rectcol.colliderect(ghost2) or rectcol.colliderect(ghost3) or rectcol.colliderect(ghost4):  #detect collision, Kui pacman puutub ghosti
        GameOver()
    

    index = 0
    for n in range(19):
        for i in range(19):
            if list[index].col.colliderect(rectcol):
                if list[index].elus:
                    list[index].elus = False
                    score += 1
                    print(score)
                
            index += 1

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
        
    
    if x > xg1:  # pacman paremal
        
        if y == yg1:  #pacman paremal
            if not (rt1 or rb1):
                i1 = ghostturntime + 1
                directionlist1 = ["RIGHT"]
                
        elif y > yg1:  #pacman paremal all
            if not (rt1 or rb1):  #pacman paremal all, parem serv vaba
                if not (bl1 or br1):  #pacman paremal all, parem ja alumine serv vaba
                    directionlist1 = ["RIGHT", "DOWN"]
                else:  #pacman paremal all, parem serv vaba, alumine serv kinni
                    directionlist1 = ["RIGHT"]
            else:  #pacman paremal all, parem serv kinni
                if not (bl1 or br1):  #pacman paremal all, parem serv kinni, alumine serv vaba
                    directionlist1 = ["DOWN"]
                else:  #pacman paremal all, parem ja alumine serv kinni
                    directionlist1 = ["LEFT", "UP"]
                    
        elif y < yg1:  #pacman paremal yleval
            if not (rt1 or rb1):  #pacman paremal yleval, parem serv vaba
                if not (tl1 or tr1):  #pacman paremal yleval, parem ja ylemine serv vaba
                    directionlist1 = ["RIGHT", "UP"]
                else:  #pacman paremal yleval, parem serv vaba, ylemine serv kinni
                    directionlist1 = ["RIGHT"]
            else:  #pacman paremal yleval, parem serv kinni
                if not (tl1 or tr1):  #pacman paremal yleval, parem serv kinni, ylemine serv vaba
                    directionlist1 = ["UP"]
                else:  #pacman paremal yleval, parem ja ylemine serv kinni
                    directionlist1 = ["LEFT", "DOWN"]
    
        
    elif x < xg1:  #pacman vasakul
        
        if y == yg1:  #pacman vasakul
            if not (lt1 or lb1):
                i1 = ghostturntime + 1
                directionlist1 = ["LEFT"]
                
        elif y > yg1:  #pacman vasakul all
            if not (lt1 or lb1):  #pacman vasakul all, vasak serv vaba
                if not (bl1 or br1):  #pacman vasakul all, vasak ja alumine serv vaba
                    directionlist1 = ["LEFT", "DOWN"]
                else:  #pacman vasakul all, vasak serv vaba, alumine serv kinni
                    directionlist1 = ["LEFT"]
            else:  #pacman vasakul all, vasak serv kinni
                if not (bl1 or br1):  #pacman vasakul all, vasak serv kinni, alumine serv vaba
                    directionlist1 = ["DOWN"]
                else:  #pacman vasakul all, vasak ja alumine serv kinni
                    directionlist1 = ["RIGHT", "UP"]
                    
        elif y < yg1:  #pacman vasakul yleval
            if not (lt1 or lb1):  #pacman vasakul yleval, vasak serv vaba
                if not (tl1 or tr1):  #pacman vasakul yleval, vasak ja ylemine serv vaba
                    directionlist1 = ["LEFT", "UP"]
                else:  #pacman vasakul yleval, vasak serv vaba, ylemine serv kinni
                    directionlist1 = ["LEFT"]
            else:  #pacman vasakul yleval, vasak serv kinni
                if not (tl1 or tr1):  #pacman vasakul yleval, vasak serv kinni, ylemine serv vaba
                    directionlist1 = ["UP"]
                else:  #pacman vasakul yleval, vasak ja ylemine serv kinni
                    directionlist1 = ["RIGHT", "DOWN"]
                    
                
    elif x == xg1:  
        if y > yg1:  #pacman all
            if not (bl1 or br1):
                i1 = ghostturntime + 1
                directionlist1 = ["DOWN"]
        if y < yg1:  #pacman yleval
            if not (tl1 or tr1):
                i1 = ghostturntime + 1
                directionlist1 = ["UP"]
                
            
    if i1 > ghostturntime:
        i1 = random.randint(30, ghostturntime - 30)
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
        
    
    if x > xg2:  # pacman paremal
        '''
        if y == yg2:  #pacman paremal
            if not (rt2 or rb2):
                i2 = ghostturntime + 1
                directionlist2 = ["RIGHT"]
        '''        
        if y > yg2:  #pacman paremal all
            if not (rt2 or rb2):  #pacman paremal all, parem serv vaba
                if not (bl2 or br2):  #pacman paremal all, parem ja alumine serv vaba
                    directionlist2 = ["RIGHT", "DOWN"]
                else:  #pacman paremal all, parem serv vaba, alumine serv kinni
                    directionlist2 = ["RIGHT"]
            else:  #pacman paremal all, parem serv kinni
                if not (bl2 or br2):  #pacman paremal all, parem serv kinni, alumine serv vaba
                    directionlist2 = ["DOWN"]
                else:  #pacman paremal all, parem ja alumine serv kinni
                    directionlist2 = ["LEFT", "UP"]
                    
        elif y < yg2:  #pacman paremal yleval
            if not (rt2 or rb2):  #pacman paremal yleval, parem serv vaba
                if not (tl2 or tr2):  #pacman paremal yleval, parem ja ylemine serv vaba
                    directionlist2 = ["RIGHT", "UP"]
                else:  #pacman paremal yleval, parem serv vaba, ylemine serv kinni
                    directionlist2 = ["RIGHT"]
            else:  #pacman paremal yleval, parem serv kinni
                if not (tl2 or tr2):  #pacman paremal yleval, parem serv kinni, ylemine serv vaba
                    directionlist2 = ["UP"]
                else:  #pacman paremal yleval, parem ja ylemine serv kinni
                    directionlist2 = ["LEFT", "DOWN"]
    
        
    elif x < xg2:  #pacman vasakul
        '''
        if y == yg2:  #pacman vasakul
            if not (lt2 or lb2):
                i2 = ghostturntime + 1
                directionlist2 = ["LEFT"]
        '''        
        if y > yg2:  #pacman vasakul all
            if not (lt2 or lb2):  #pacman vasakul all, vasak serv vaba
                if not (bl2 or br2):  #pacman vasakul all, vasak ja alumine serv vaba
                    directionlist2 = ["LEFT", "DOWN"]
                else:  #pacman vasakul all, vasak serv vaba, alumine serv kinni
                    directionlist2 = ["LEFT"]
            else:  #pacman vasakul all, vasak serv kinni
                if not (bl2 or br2):  #pacman vasakul all, vasak serv kinni, alumine serv vaba
                    directionlist2 = ["DOWN"]
                else:  #pacman vasakul all, vasak ja alumine serv kinni
                    directionlist2 = ["RIGHT", "UP"]
                    
        elif y < yg2:  #pacman vasakul yleval
            if not (lt2 or lb2):  #pacman vasakul yleval, vasak serv vaba
                if not (tl2 or tr2):  #pacman vasakul yleval, vasak ja ylemine serv vaba
                    directionlist2 = ["LEFT", "UP"]
                else:  #pacman vasakul yleval, vasak serv vaba, ylemine serv kinni
                    directionlist2 = ["LEFT"]
            else:  #pacman vasakul yleval, vasak serv kinni
                if not (tl2 or tr2):  #pacman vasakul yleval, vasak serv kinni, ylemine serv vaba
                    directionlist2 = ["UP"]
                else:  #pacman vasakul yleval, vasak ja ylemine serv kinni
                    directionlist2 = ["RIGHT", "DOWN"]
                    
    '''            
    elif x == xg2:  
        if y > yg2:  #pacman all
            if not (bl2 or br2):
                i2 = ghostturntime + 1
                directionlist2 = ["DOWN"]
        if y < yg2:  #pacman yleval
            if not (tl2 or tr2):
                i2 = ghostturntime + 1
                directionlist2 = ["UP"]
    '''            
            
    if i2 > ghostturntime:
        i2 = random.randint(0, ghostturntime / 4)
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
        
        
    if x < xg3:  # pacman vasakul
        
        if y == yg3:  #pacman vasakul
            if not (rt3 or rb3):
                i3 = ghostturntime + 1
                directionlist3 = ["RIGHT"]
                
        elif y < yg3:  #pacman vasakul yleval
            if not (rt3 or rb3):  #pacman vasakul yleval, parem serv vaba
                if not (bl3 or br3):  #pacman vasakul yleval, parem ja alumine serv vaba
                    directionlist3 = ["RIGHT", "DOWN"]
                else:  #pacman vasakul yleval, parem serv vaba, alumine serv kinni
                    directionlist3 = ["RIGHT"]
            else:  #pacman vasakul yleval, parem serv kinni
                if not (bl3 or br3):  #pacman vasakul yleval, parem serv kinni, alumine serv vaba
                    directionlist3 = ["DOWN"]
                else:  #pacman vasakul yleval, parem ja alumine serv kinni
                    directionlist3 = ["LEFT", "UP"]
                    
        elif y > yg3:  #pacman vasakul all
            if not (rt3 or rb3):  #pacman vasakul all, parem serv vaba
                if not (tl3 or tr3):  #pacman vasakul all, parem ja ylemine serv vaba
                    directionlist3 = ["RIGHT", "UP"]
                else:  #pacman vasakul all, parem serv vaba, ylemine serv kinni
                    directionlist3 = ["RIGHT"]
            else:  #pacman vasakul all, parem serv kinni
                if not (tl3 or tr3):  #pacman vasakul all, parem serv kinni, ylemine serv vaba
                    directionlist3 = ["UP"]
                else:  #pacman vasakul all, parem ja ylemine serv kinni
                    directionlist3 = ["LEFT", "DOWN"]
    
        
    elif x > xg3:  #pacman paremal
        
        if y == yg3:  #pacman paremal
            if not (lt3 or lb3):
                i3 = ghostturntime + 1
                directionlist3 = ["LEFT"]
                
        elif y < yg3:  #pacman paremal yleval
            if not (lt3 or lb3):  #pacman paremal yleval, vasak serv vaba
                if not (bl3 or br3):  #pacman paremal yleval, vasak ja alumine serv vaba
                    directionlist3 = ["LEFT", "DOWN"]
                else:  #pacman paremal yleval, vasak serv vaba, alumine serv kinni
                    directionlist3 = ["LEFT"]
            else:  #pacman paremal yleval, vasak serv kinni
                if not (bl3 or br3):  #pacman paremal yleval, vasak serv kinni, alumine serv vaba
                    directionlist3 = ["DOWN"]
                else:  #pacman paremal yleval, vasak ja alumine serv kinni
                    directionlist3 = ["RIGHT", "UP"]
                    
        elif y > yg3:  #pacman paremal all
            if not (lt3 or lb3):  #pacman paremal all, vasak serv vaba
                if not (tl3 or tr3):  #pacman paremal all, vasak ja ylemine serv vaba
                    directionlist3 = ["LEFT", "UP"]
                else:  #pacman paremal all, vasak serv vaba, ylemine serv kinni
                    directionlist3 = ["LEFT"]
            else:  #pacman paremal all, vasak serv kinni
                if not (tl3 or tr3):  #pacman paremal all, vasak serv kinni, ylemine serv vaba
                    directionlist3 = ["UP"]
                else:  #pacman paremal all, vasak ja ylemine serv kinni
                    directionlist3 = ["RIGHT", "DOWN"]
                    
                
    elif x == xg3:  
        if y > yg3:  #pacman all
            if not (bl3 or br3):
                i3 = ghostturntime + 1
                directionlist3 = ["DOWN"]
        if y < yg3:  #pacman yleval
            if not (tl3 or tr3):
                i3 = ghostturntime + 1
                directionlist3 = ["UP"]
                
            
    if i3 > ghostturntime:
        i3 = random.randint(0, ghostturntime - 20)
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
    #################################### G H O S T 4 #####################################
    
        #colliderid...  
    rel_point = sub((xg4, yg4 - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tl4 = True
    else:
        tl4 = False               
    rel_point = sub((xg4 + ghostsize - 1, yg4 - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        tr4 = True
    else:
        tr4 = False
    rel_point = sub((xg4 - 1, yg4), [0, 0])
    if wallmask.get_at(rel_point): 
        lt4 = True
    else:
        lt4 = False        
    rel_point = sub((xg4 - 1, yg4 + ghostsize - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        lb4 = True
    else:
        lb4 = False           
    rel_point = sub((xg4 + ghostsize, yg4), [0, 0])
    if wallmask.get_at(rel_point): 
        rt4 = True
    else:
        rt4 = False        
    rel_point = sub((xg4 + ghostsize, yg4 + ghostsize - 1), [0, 0])
    if wallmask.get_at(rel_point): 
        rb4 = True
    else:
        rb4 = False            
    rel_point = sub((xg4, yg4 + ghostsize), [0, 0])
    if wallmask.get_at(rel_point): 
        bl4 = True
    else:
        bl4 = False        
    rel_point = sub((xg4 + ghostsize - 1, yg4 + ghostsize), [0, 0])
    if wallmask.get_at(rel_point): 
        br4 = True
    else:
        br4 = False
        
        
    if i4 > ghostturntime:
        i4 = 0
        nextdirection4 = random.choice(directionlist4)
    else:
        i4 += 1
    
        
        #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection4 is "LEFT") and not (lt4 or lb4):
        direction4 = nextdirection4
    elif (nextdirection4 is "RIGHT") and not (rt4 or rb4):
        direction4 = nextdirection4
    elif (nextdirection4 is "UP") and not (tl4 or tr4):
        direction4 = nextdirection4       
    elif (nextdirection4 is "DOWN") and not (bl4 or br4):
        direction4 = nextdirection4
    
    #kui pacman liigus yhes suunas ja sein tuleb ette (colliderid = True), direction = still
    elif ((direction4 is "LEFT") and (lt4 or lb4)):
        direction4 = "STILL"
        directionlist4 = ["RIGHT", "UP", "DOWN"]
        i4 = ghostturntime
    elif ((direction4 is "RIGHT") and (rt4 or rb4)):
        direction4 = "STILL"
        directionlist4 = ["LEFT", "UP", "DOWN"]
        i4 = ghostturntime
    elif ((direction4 is "UP") and (tl4 or tr4)):
        direction4 = "STILL"
        directionlist4 = ["LEFT", "RIGHT", "DOWN"]
        i4 = ghostturntime
    elif ((direction4 is "DOWN") and (bl4 or br4)):
        direction4 = "STILL"
        directionlist4 = ["LEFT", "RIGHT", "UP"]
        i4 = ghostturntime
    else:
        pass
    
    if direction4 is "LEFT":
        xg4 -= vel
    elif direction4 is "RIGHT":
        xg4 += vel        
    elif direction4 is "UP":
        yg4 -= vel    
    elif direction4 is "DOWN":
        yg4 += vel
    elif direction4 is "STILL":
        yg4 = yg4
        xg4 = xg4
        i4 = ghostturntime + 1
    else:
        pass
    
    #################################### G H O S T 4 #####################################
    #################################### G H O S T S #####################################

    #print("x =", x, " y =", y, "   ",  "  tl=", tl,"  tr=", tr,"  lt=", lt,"  lb=", lb,"  rt=", rt,"  rb=", rb,"  bl=", bl,"  br=", br,)
    
    window.fill((0, 0, 0))  #taust mustaks
    
    
    '''
    for n in range(19):
        for i in range(19):
            p = Point(15 + (30 * n), 15 + (30 * i), True)
            p.draw()'''
    
    Point.draw_all()
    
    window.blit(walls, (0, 0))  #lisa labyrint
    
    rect1 = pygame.Rect(x, y, diameter, diameter)  #loo/joonista pacman
    rectcol = pygame.Rect(x + 10, y + 10, diameter - 20, diameter - 20)
    ghost1 = pygame.Rect(xg1, yg1, ghostsize, ghostsize)
    ghost2 = pygame.Rect(xg2, yg2, ghostsize, ghostsize)
    ghost3 = pygame.Rect(xg3, yg3, ghostsize, ghostsize)
    ghost4 = pygame.Rect(xg4, yg4, ghostsize, ghostsize)
    
    
    if temp < 10:
        temp += 1
    else:
        temp = 1
        frame += 1
        frameg1 += 1
        frameg2 += 1
        frameg3 += 1
        frameg4 += 1
        
        if frame >= len(cells):
            frame = 1
        if frameg1 >= len(cellsg1):
            frameg1 = 1
        if frameg2 >= len(cellsg2):
            frameg2 = 1
        if frameg3 >= len(cellsg3):
            frameg3 = 1
        if frameg4 >= len(cellsg4):
            frameg4 = 1
            
    playerImg = cells[frame]    
    window.blit(pygame.transform.rotate(playerImg, rotation), (x, y))
    ghost1Img = cellsg1[frameg1]    
    window.blit(ghost1Img, (xg1, yg1))
    ghost2Img = cellsg2[frameg2]    
    window.blit(ghost2Img, (xg2, yg2))
    ghost3Img = cellsg3[frameg3]    
    window.blit(ghost3Img, (xg3, yg3))
    ghost4Img = cellsg4[frameg4]    
    window.blit(ghost4Img, (xg4, yg4))

    pygame.display.update() #update display
    
pygame.quit()
        
        


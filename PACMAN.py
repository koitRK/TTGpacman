import pygame
import pygame.freetype
import random
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

#Load font
GAME_FONT = pygame.freetype.Font("emulogic.ttf", 24)

channel1 = pygame.mixer.Channel(1)  #Music channel
channel2 = pygame.mixer.Channel(2)  #SFX channel

#Load sound files
chomp = pygame.mixer.Sound("chomp.wav")
ghostmove = pygame.mixer.Sound("ghostmove.wav")
death = pygame.mixer.Sound("death.wav")
beginning = pygame.mixer.Sound("beginning.wav")

#Taastab koigi muutujate vaartused algasendisse
def Reset():
    #Ei oskand muutmoodi, kui muuta koik muutujad globaliks
    global level, x, y, xg1, yg1, xg2, yg2, xg3, yg3, xg4, yg4, diameter, rotation, ghostturntime, score, temp, vel, winsize, i1, i2, i3, i4, list
    global tl, tr, lt, lb, rt, rb, bl, br, tl1, tr1, lt1, lb1, rt1, rb1, bl1, br1, tl2, tr2, lt2, lb2, rt2, rb2, bl2, br2, tl3, tr3, lt3, lb3, rt3, rb3, bl3, br3, tl4, tr4, lt4, lb4, rt4, rb4, bl4, br4
    global direction, direction1, direction2, direction3, direction4, nextdirection, nextdirection1, nextdirection2, nextdirection3, nextdirection4,directionlist1, directionlist2, directionlist3, directionlist4

    x = 270 #pacmani koordinaat x, alguses 270
    y = 330  #pacmani koordinaat y, alguses 330
    diameter = 30  #pacmani ja ghostide suurus pikslites
    rotation = 0  #pacmani sprite-i orientatsioon
    ghostturntime = 100  #ghost muudab suunda iga x pixli tagant
    score = 0  #skoor
    temp = 1  #loendur, loeb, mitu korda on main loopi labitud
    vel = 1 #pacmani ja ghostide kiirus. Peab olema 1 voi arvu 30 tegur
    winsize = 570  #Akna suurus, default 570, yks blokk on 30px * 30px, 19 * 19 blokki
    list = []  #List, mis hoiab klassi Punkt objecte

    i1 = 0  #ghost 1 counter. Kui counter = ghostturntime, siis ghost muudab suunda
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

    #Colliders. (none) = pacman, 1 = ghost1, 2 = ghost2, 3 = ghost3, 4 = ghost4
    #tl = topleft, tr = topright, lt = lefttop, lb = leftbottom, rt = righttop, rb = rightbottom, bl = bottomleft, br = bottomright
    tl, tr, lt, lb, rt, rb, bl, br = (False,) * 8  #Pacman colliders
    tl1, tr1, lt1, lb1, rt1, rb1, bl1, br1 = (False,) * 8  #Ghost 1 colliders
    tl2, tr2, lt2, lb2, rt2, rb2, bl2, br2 = (False,) * 8  #Ghost 2 colliders
    tl3, tr3, lt3, lb3, rt3, rb3, bl3, br3 = (False,) * 8  #Ghost 3 colliders
    tl4, tr4, lt4, lb4, rt4, rb4, bl4, br4 = (False,) * 8  #Ghost 4 colliders

    #List suundadest, kuhu ghostid saavad minna
    directionlist1 = ["LEFT", "RIGHT", "UP", "DOWN"]
    directionlist2 = ["LEFT", "RIGHT", "UP", "DOWN"]
    directionlist3 = ["LEFT", "RIGHT", "UP", "DOWN"]
    directionlist4 = ["LEFT", "RIGHT", "UP", "DOWN"]

    #Pacmani ja ghostide liikumissuund
    #direction = praegune liikumissuund, nextdirection = liikumissuund, kuhu object esimesel võimalusel läheb
    direction = "STILL"
    nextdirection = "STILL"
    direction1 = "STILL"
    nextdirection1 = "STILL"
    direction2 = "STILL"
    nextdirection2 = "STILL"
    direction3 = "STILL"
    nextdirection3 = "STILL"
    direction4 = "STILL"
    nextdirection4 = "STILL"


Reset()

#Funktsioon, mis lisab skoori
def AddScore(amount):
    global score
    score += 1

#Funktstioon, mis kutsutakse suremise korral
#Katkestab taustaheli, mangib suremise heli, valjub main loop-ist, kutsub esile funktsiooni Menu
def GameOver():
    print("GAME OVER")
    pygame.mixer.pause()
    channel2.play(death)
    pygame.time.delay(2000)
    global run
    run = False
    Menu()

#Klass Point. xp = x coord, yp = ycoord, elus = elus/surnud, col = collider
#draw_all() = joonistab koik elus punktid
#collect() = Vaatab, kas punkt collidib pacmaniga. Kui jah, siis punkt != elus ja listatakse skoori
#kill_all() = Tapab koik eelmisest levelist allesjaanud punktid
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
    @classmethod
    def collect(cls):
        for obj in cls.objs:
            if obj.elus:
                if hasattr(obj, "col"):
                    if obj.col.colliderect(siseRect):
                        obj.elus = False
                        AddScore(1)
                        print(score)
                        channel2.play(chomp)
    @classmethod
    def kill_all(cls):
        for obj in cls.objs:
            obj.elus = False


window = pygame.display.set_mode((winsize, winsize + 75))  #loob uue akna
pygame.display.set_caption("PACMAN")  #akna nimetus
s = pygame.Surface((winsize, winsize + 75))  #poollabipaistev surface
s.set_alpha(128)                #alpha value

#Funktsioon, tapab koik Pointi objektid, ja loob 19*19 ruudustikus uues Point objektid
def CreatePoints():
#Loob 19 * 19 ruudustikus klass Point-i kasutades punktid
    Point.kill_all() #Tapab koik eelmisest levelist allesjaanud punktid
    for n in range(19):
        for i in range(19):
            list.append(Point(15 + (30 * n), 15 + (30 * i), True, pygame.draw.rect(window, (255, 255, 255), [15 + (30 * n), 15 + (30 * i), 3, 3])))


################## SPRITES ##################
################## SPRITES ##################
logo = pygame.image.load("logo.png")

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
playerImg = cells[0]  #Sprite, mis joonistatakse
frame = 1  #Sprite number, mis valitakse

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

################## SPRITES ##################
################## SPRITES ##################

#Funktsioon, mis sisaldab menyy joonistamist ja navigeerimist ja leveli valikut ja skoori jms
def Menu():
    channel2.play(beginning, -1)  #Mangib loputult algusmuusikat
    xbox = 155  #Highlighti x coord
    count = 0  #Counter, mis piirab liiga kiiret leveli valikut
    global level
    level = 1
    while True:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        keys = pygame.key.get_pressed()  #Vaatab, milline klahv on vajutadud
        count += 1
        if keys[pygame.K_LEFT] and xbox > 155 :  #Kui vajutatakse LEFT, siis highlightitakse vasakul pool oleva leveli number
            if count > 10:
                level -= 1
                count = 0
                xbox -= 71
        elif keys[pygame.K_RIGHT] and xbox < 365 :  #Kui vajutatakse RIGHT, siis highlightitakse paremal pool oleva leveli number
            if count > 10:
                level += 1
                count = 0
                xbox += 71
        elif keys[pygame.K_SPACE]:  #START THE GAME, kutsub funktsiooni Reset() ja CreatePoints()
            Reset()
            global walls, wallmask, siseRect, valisRect, ghost1, ghost2, ghost3, ghost4
            CreatePoints()

            #Loob/joonistab koik vajaliku ekraanile, et tulevad funktsioonid saaksid nende atribuute kasutada
            walls = pygame.image.load("walls" + str(level) + ".png")  #load labyrindi pilt/taust
            #window.blit(walls, (0, 0))  #asetab labyrindi/tausta koordinaatidele 0, 0
            wallmask = pygame.mask.from_surface(walls)  #teeb labyrindist maski, et seda colliderina kasutada
            valisRect = pygame.draw.rect(window, (255, 255, 0), [x, y, diameter, diameter])  #loob ja joonistab pacmani valimise rectangle
            siseRect = pygame.Rect(x + 10, y + 10, diameter - 20, diameter - 20)  #loob ja joonistab pacmani sisemise rectangle
            ghost1 = pygame.draw.rect(window, (255, 0, 0), [xg1, yg1, diameter, diameter])  #loob ghost1 rectangle
            ghost2 = pygame.draw.rect(window, (255, 184, 255), [xg2, yg2, diameter, diameter])  #loob ghost2 rectangle
            ghost3 = pygame.draw.rect(window, (255, 184, 82), [xg3, yg3, diameter, diameter])  #loob ghost3 rectangle
            ghost4 = pygame.draw.rect(window, (0, 255, 255), [xg4, yg4, diameter, diameter])  #loob ghost4 rectangle
            window.fill((0, 0, 0))  #Taidab ekraani musta varviga, et eelnevalt valedesse kohtadesse joonistatud naha ei jaaks
            pygame.display.update()  #Update display
            pygame.mixer.pause()  #Katkestab heli/muusika
            channel1.play(ghostmove, -1)  #Kordab loputult taustaheli
            global run
            run = True
            break

        pygame.time.delay(10)


        walls = pygame.image.load("walls" + str(level) + ".png")  #Laeb vastavalt eelnevalt valitud levelile labyrindi pildi
        window.blit(walls, (0, 0))  #Joonistab labyrindi
        s.fill((0,0,0))
        window.blit(s, (0,0))  #Lisab poollabipaistva kihi
        window.blit(logo, (50, 100))  #Joonistab pacmani logo

        pygame.draw.rect(window, (50, 50, 150), [xbox, 335, 50, 50])  #Joonistab valitud leveli highlighti
        GAME_FONT.render_to(window, (150, 270), "SELECT LEVEL", (255, 255, 255))  #Lisab teksti
        GAME_FONT.render_to(window, (170, 350), "1  2  3  4", (255, 255, 255))
        GAME_FONT.render_to(window, (155, 400), "press space", (100, 100, 100))
        GAME_FONT.render_to(window, (200, 600), ("score " + str(score)), (255, 255, 255))
        pygame.display.update()  #Update display

#Mangu kaivitamisel kutsutakse funktsioon Menu()
Menu()

run = True
###################################### M A I N   L O O P ############################################
while run:  #Main loop

    pygame.time.delay(5)  #Aeg iga kaardi vahel. SIIN SAAB KIIRUST MUUTA. Default 5ms

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()  #Vaatab, milline klahv on vajutadud

    if keys[pygame.K_LEFT]:
        nextdirection = "LEFT"  #nextdirection = jargmine suund, kuhu tahetakse minna
    elif keys[pygame.K_RIGHT]:
        nextdirection = "RIGHT"
    elif keys[pygame.K_UP]:
        nextdirection = "UP"
    elif keys[pygame.K_DOWN]:
        nextdirection = "DOWN"



    #################################### P A C M A N #####################################

    #colliderid...
    try:
        tl = True if wallmask.get_at([x, y -1]) else False
        tr = True if wallmask.get_at([x + diameter - 1, y - 1]) else False
        lt = True if wallmask.get_at([x - 1, y]) else False
        lb = True if wallmask.get_at([x - 1, y + diameter - 1]) else False
        rt = True if wallmask.get_at([x + diameter, y]) else False
        rb = True if wallmask.get_at([x + diameter, y + diameter - 1]) else False
        bl = True if wallmask.get_at([x, y + diameter]) else False
        br = True if wallmask.get_at([x + diameter - 1, y + diameter]) else False
    except IndexError:
        lt, lb, rt, rb = (False,)*4
        tl, tr, bl, br = (True,)*4


    #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection == "LEFT") and not (lt or lb):
        direction = nextdirection
    elif (nextdirection == "RIGHT") and not (rt or rb):
        direction = nextdirection
    elif (nextdirection == "UP") and not (tl or tr):
        direction = nextdirection
    elif (nextdirection == "DOWN") and not (bl or br):
        direction = nextdirection

    #kui pacman liigub yhes suunas ja sein tuleb ette (colliderid = True), pacman jaab seisma
    elif ((direction == "LEFT") and (lt or lb)):
        direction = "STILL"
    elif ((direction == "RIGHT") and (rt or rb)):
        direction = "STILL"
    elif ((direction == "UP") and (tl or tr)):
        direction = "STILL"
    elif ((direction == "DOWN") and (bl or br)):
        direction = "STILL"


    #pacmani liigutamine soltuvalt suunast(direction). Rotation muudab vaid sprite-i orientatsiooni
    if direction == "LEFT":
        rotation = 180
        x -= vel
        if x < -30:
            x = 570
    elif direction == "RIGHT":
        x += vel
        rotation = 0
        if x > 570:
            x = -30
    elif direction == "UP":
        y -= vel
        rotation = 90
    elif direction == "DOWN":
        y += vel
        rotation = 270
    elif direction == "STILL":
        y = y
        x = x

    #Kui pacman puutub ghosti, kutsutakse functsioon GameOver()
    if siseRect.colliderect(ghost1) or siseRect.colliderect(ghost2) or siseRect.colliderect(ghost3) or siseRect.colliderect(ghost4):
        GameOver()

    #Kutsutakse klassi Point funktsioon collect()
    Point.collect()


    #################################### P A C M A N #####################################
    #################################### G H O S T S #####################################
    #################################### G H O S T 1 #####################################

    #colliderid...
    try:
        tl1 = True if wallmask.get_at([xg1, yg1 -1]) else False
        tr1 = True if wallmask.get_at([xg1 + diameter - 1, yg1 - 1]) else False
        lt1 = True if wallmask.get_at([xg1 - 1, yg1]) else False
        lb1 = True if wallmask.get_at([xg1 - 1, yg1 + diameter - 1]) else False
        rt1 = True if wallmask.get_at([xg1 + diameter, yg1]) else False
        rb1 = True if wallmask.get_at([xg1 + diameter, yg1 + diameter - 1]) else False
        bl1 = True if wallmask.get_at([xg1, yg1 + diameter]) else False
        br1 = True if wallmask.get_at([xg1 + diameter - 1, yg1 + diameter]) else False
    except IndexError:
        lt1, lb1, rt1, rb1 = (False,)*4
        tl1, tr1, bl1, br1 = (True,)*4

    if x > xg1:  #pacman paremal

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

    #Ghost muudab suunda, kui on piisavalt palju liikunud
    if i1 > ghostturntime:
        i1 = random.randint(30, ghostturntime - 30)
        nextdirection1 = random.choice(directionlist1)
    else:
        i1 += 1


    #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection1 == "LEFT") and not (lt1 or lb1):
        direction1 = nextdirection1
    elif (nextdirection1 == "RIGHT") and not (rt1 or rb1):
        direction1 = nextdirection1
    elif (nextdirection1 == "UP") and not (tl1 or tr1):
        direction1 = nextdirection1
    elif (nextdirection1 == "DOWN") and not (bl1 or br1):
        direction1 = nextdirection1

    #kui ghost1 liigub yhes suunas ja sein tuleb ette (colliderid = True), direction = still
    elif ((direction1 == "LEFT") and (lt1 or lb1)):
        direction1 = "STILL"
        directionlist1 = ["RIGHT", "UP", "DOWN"]
        i1 = ghostturntime
    elif ((direction1 == "RIGHT") and (rt1 or rb1)):
        direction1 = "STILL"
        directionlist1 = ["LEFT", "UP", "DOWN"]
        i1 = ghostturntime
    elif ((direction1 == "UP") and (tl1 or tr1)):
        direction1 = "STILL"
        directionlist1 = ["LEFT", "RIGHT", "DOWN"]
        i1 = ghostturntime
    elif ((direction1 == "DOWN") and (bl1 or br1)):
        direction1 = "STILL"
        directionlist1 = ["LEFT", "RIGHT", "UP"]
        i1 = ghostturntime


    if direction1 == "LEFT":
        xg1 -= vel
        if xg1 < -30:
            xg1 = 570
    elif direction1 == "RIGHT":
        xg1 += vel
        if xg1 > 570:
            xg1 = -30
    elif direction1 == "UP":
        yg1 -= vel
    elif direction1 == "DOWN":
        yg1 += vel
    elif direction1 == "STILL":
        yg1 = yg1
        xg1 = xg1
        i1 = ghostturntime + 1


    #################################### G H O S T 1 #####################################
    #################################### G H O S T 2 #####################################

    #colliderid...
    try:
        tl2 = True if wallmask.get_at([xg2, yg2 -1]) else False
        tr2 = True if wallmask.get_at([xg2 + diameter - 1, yg2 - 1]) else False
        lt2 = True if wallmask.get_at([xg2 - 1, yg2]) else False
        lb2 = True if wallmask.get_at([xg2 - 1, yg2 + diameter - 1]) else False
        rt2 = True if wallmask.get_at([xg2 + diameter, yg2]) else False
        rb2 = True if wallmask.get_at([xg2 + diameter, yg2 + diameter - 1]) else False
        bl2 = True if wallmask.get_at([xg2, yg2 + diameter]) else False
        br2 = True if wallmask.get_at([xg2 + diameter - 1, yg2 + diameter]) else False
    except IndexError:
        lt2, lb2, rt2, rb2 = (False,)*4
        tl2, tr2, bl2, br2 = (True,)*4

    if x > xg2:  #pacman paremal

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

    #Ghost muudab suunda, kui on piisavalt palju liikunud
    if i2 > ghostturntime:
        i2 = random.randint(0, ghostturntime / 4)
        nextdirection2 = random.choice(directionlist2)
    else:
        i2 += 1


    #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection2 == "LEFT") and not (lt2 or lb2):
        direction2 = nextdirection2
    elif (nextdirection2 == "RIGHT") and not (rt2 or rb2):
        direction2 = nextdirection2
    elif (nextdirection2 == "UP") and not (tl2 or tr2):
        direction2 = nextdirection2
    elif (nextdirection2 == "DOWN") and not (bl2 or br2):
        direction2 = nextdirection2

    #kui pacman liigus yhes suunas ja sein tuleb ette (colliderid = True), direction = still
    elif ((direction2 == "LEFT") and (lt2 or lb2)):
        direction2 = "STILL"
        directionlist2 = ["RIGHT", "UP", "DOWN"]
        i2 = ghostturntime
    elif ((direction2 == "RIGHT") and (rt2 or rb2)):
        direction2 = "STILL"
        directionlist2 = ["LEFT", "UP", "DOWN"]
        i2 = ghostturntime
    elif ((direction2 == "UP") and (tl2 or tr2)):
        direction2 = "STILL"
        directionlist2 = ["LEFT", "RIGHT", "DOWN"]
        i2 = ghostturntime
    elif ((direction2 == "DOWN") and (bl2 or br2)):
        direction2 = "STILL"
        directionlist2 = ["LEFT", "RIGHT", "UP"]
        i2 = ghostturntime


    if direction2 == "LEFT":
        xg2 -= vel
        if xg2 < -30:
            xg2 = 570
    elif direction2 == "RIGHT":
        xg2 += vel
        if xg2 > 570:
            xg2 = -30
    elif direction2 == "UP":
        yg2 -= vel
    elif direction2 == "DOWN":
        yg2 += vel
    elif direction2 == "STILL":
        yg2 = yg2
        xg2 = xg2
        i2 = ghostturntime + 1


    #################################### G H O S T 2 #####################################
    #################################### G H O S T 3 #####################################

    #colliderid...
    try:
        tl3 = True if wallmask.get_at([xg3, yg3 -1]) else False
        tr3 = True if wallmask.get_at([xg3 + diameter - 1, yg3 - 1]) else False
        lt3 = True if wallmask.get_at([xg3 - 1, yg3]) else False
        lb3 = True if wallmask.get_at([xg3 - 1, yg3 + diameter - 1]) else False
        rt3 = True if wallmask.get_at([xg3 + diameter, yg3]) else False
        rb3 = True if wallmask.get_at([xg3 + diameter, yg3 + diameter - 1]) else False
        bl3 = True if wallmask.get_at([xg3, yg3 + diameter]) else False
        br3 = True if wallmask.get_at([xg3 + diameter - 1, yg3 + diameter]) else False
        if xg3 <= 30:
            lt3, lb3 = True, True
        elif xg3 + diameter > 570 - 30:
            rt3, rb3 = True, True
    except IndexError:
        lt3, lb3, rt3, rb3 = (False,)*4
        tl3, tr3, bl3, br3 = (True,)*4


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
            if not (tl3 or tr3):
                i3 = ghostturntime + 1
                directionlist3 = ["UP"]
        if y < yg3:  #pacman yleval
            if not (bl3 or br3):
                i3 = ghostturntime + 1
                directionlist3 = ["DOWN"]

    #Ghost muudab suunda, kui on piisavalt palju liikunud
    if i3 > ghostturntime:
        i3 = random.randint(0, ghostturntime - 20)
        nextdirection3 = random.choice(directionlist3)
    else:
        i3 += 1


    #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection3 == "LEFT") and not (lt3 or lb3):
        direction3 = nextdirection3
    elif (nextdirection3 == "RIGHT") and not (rt3 or rb3):
        direction3 = nextdirection3
    elif (nextdirection3 == "UP") and not (tl3 or tr3):
        direction3 = nextdirection3
    elif (nextdirection3 == "DOWN") and not (bl3 or br3):
        direction3 = nextdirection3

    #kui ghost3 liigub yhes suunas ja sein tuleb ette (colliderid = True), direction = still
    elif ((direction3 == "LEFT") and (lt3 or lb3)):
        direction3 = "STILL"
        directionlist3 = ["RIGHT", "UP", "DOWN"]
        i3 = ghostturntime
    elif ((direction3 == "RIGHT") and (rt3 or rb3)):
        direction3 = "STILL"
        directionlist3 = ["LEFT", "UP", "DOWN"]
        i3 = ghostturntime
    elif ((direction3 == "UP") and (tl3 or tr3)):
        direction3 = "STILL"
        directionlist3 = ["LEFT", "RIGHT", "DOWN"]
        i3 = ghostturntime
    elif ((direction3 == "DOWN") and (bl3 or br3)):
        direction3 = "STILL"
        directionlist3 = ["LEFT", "RIGHT", "UP"]
        i3 = ghostturntime



    if direction3 == "LEFT":
        xg3 -= vel
        if xg3 < -30:
            xg3 = 570
    elif direction3 == "RIGHT":
        xg3 += vel
        if xg3 > 570:
            xg3 = -30
    elif direction3 == "UP":
        yg3 -= vel
    elif direction3 == "DOWN":
        yg3 += vel
    elif direction3 == "STILL":
        yg3 = yg3
        xg3 = xg3
        i3 = ghostturntime + 1


    #################################### G H O S T 3 #####################################
    #################################### G H O S T 4 #####################################

    #colliderid...
    try:
        tl4 = True if wallmask.get_at([xg4, yg4 -1]) else False
        tr4 = True if wallmask.get_at([xg4 + diameter - 1, yg4 - 1]) else False
        lt4 = True if wallmask.get_at([xg4 - 1, yg4]) else False
        lb4 = True if wallmask.get_at([xg4 - 1, yg4 + diameter - 1]) else False
        rt4 = True if wallmask.get_at([xg4 + diameter, yg4]) else False
        rb4 = True if wallmask.get_at([xg4 + diameter, yg4 + diameter - 1]) else False
        bl4 = True if wallmask.get_at([xg4, yg4 + diameter]) else False
        br4 = True if wallmask.get_at([xg4 + diameter - 1, yg4 + diameter]) else False
    except IndexError:
        lt4, lb4, rt4, rb4 = (False,)*4
        tl4, tr4, bl4, br4 = (True,)*4

    #Ghost muudab suunda, kui on piisavalt palju liikunud
    if i4 > ghostturntime:
        i4 = 0
        nextdirection4 = random.choice(directionlist4)
    else:
        i4 += 1


        #kui nextdirection on midagi, ja rada on vaba, siis liikumissuund(direction) muudetakse
    if (nextdirection4 == "LEFT") and not (lt4 or lb4):
        direction4 = nextdirection4
    elif (nextdirection4 == "RIGHT") and not (rt4 or rb4):
        direction4 = nextdirection4
    elif (nextdirection4 == "UP") and not (tl4 or tr4):
        direction4 = nextdirection4
    elif (nextdirection4 == "DOWN") and not (bl4 or br4):
        direction4 = nextdirection4

    #kui ghost3 liigub yhes suunas ja sein tuleb ette (colliderid = True), direction = still
    elif ((direction4 == "LEFT") and (lt4 or lb4)):
        direction4 = "STILL"
        directionlist4 = ["RIGHT", "UP", "DOWN"]
        i4 = ghostturntime
    elif ((direction4 == "RIGHT") and (rt4 or rb4)):
        direction4 = "STILL"
        directionlist4 = ["LEFT", "UP", "DOWN"]
        i4 = ghostturntime
    elif ((direction4 == "UP") and (tl4 or tr4)):
        direction4 = "STILL"
        directionlist4 = ["LEFT", "RIGHT", "DOWN"]
        i4 = ghostturntime
    elif ((direction4 == "DOWN") and (bl4 or br4)):
        direction4 = "STILL"
        directionlist4 = ["LEFT", "RIGHT", "UP"]
        i4 = ghostturntime


    if direction4 == "LEFT":
        xg4 -= vel
        if xg4 < -30:
            xg4 = 570
    elif direction4 == "RIGHT":
        xg4 += vel
        if xg4 > 570:
            xg4 = -30
    elif direction4 == "UP":
        yg4 -= vel
    elif direction4 == "DOWN":
        yg4 += vel
    elif direction4 == "STILL":
        yg4 = yg4
        xg4 = xg4
        i4 = ghostturntime + 1

    #################################### G H O S T 4 #####################################
    #################################### G H O S T S #####################################


    window.fill((0, 0, 0))  #taust mustaks

    Point.draw_all()  #joonistab koik elusad punktid
    window.blit(walls, (0, 0))  #lisa labyrint

    valisRect = pygame.Rect(x, y, diameter, diameter)  #loo pacman
    siseRect = pygame.Rect(x + 10, y + 10, diameter - 20, diameter - 20)
    ghost1 = pygame.Rect(xg1, yg1, diameter, diameter)
    ghost2 = pygame.Rect(xg2, yg2, diameter, diameter)
    ghost3 = pygame.Rect(xg3, yg3, diameter, diameter)
    ghost4 = pygame.Rect(xg4, yg4, diameter, diameter)


    #Iga 10 kaardi tagant votab jargmise sprite-i
    if temp < 7:
        temp += 1
    else:
        temp = 1
        frame += 1
        frameg1 += 1
        frameg2 += 1
        frameg3 += 1
        frameg4 += 1

        #Kui kaadri number on vordne/yletab listis olevate sprite-de arvu, alustatakse algusest
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

    #Listist voetakse frame-le vastav sprite
    playerImg = cells[frame]
    window.blit(pygame.transform.rotate(playerImg, rotation), (x, y)) #Pacmani sprite pooratakse, vastavalt liikumissuunale
    ghost1Img = cellsg1[frameg1]
    window.blit(ghost1Img, (xg1, yg1))
    ghost2Img = cellsg2[frameg2]
    window.blit(ghost2Img, (xg2, yg2))
    ghost3Img = cellsg3[frameg3]
    window.blit(ghost3Img, (xg3, yg3))
    ghost4Img = cellsg4[frameg4]
    window.blit(ghost4Img, (xg4, yg4))
    GAME_FONT.render_to(window, (200, 600), ("score " + str(score)), (255, 255, 255))

    pygame.display.update() #update display

###################################### M A I N   L O O P ############################################

pygame.quit()

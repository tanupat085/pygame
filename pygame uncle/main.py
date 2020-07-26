import pygame
import math
import random
from pygame import mixer


#setup เริ่มต้น ให้ pygame ทำงาน
pygame.init()


# ปรับหน้าจอ
WIDTH = 800 
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#เปลี่ยนชื่อ title
pygame.display.set_caption('tan_aod')
#set icon
icon = pygame.image.load('person.png')
pygame.display.set_icon(icon)
background = pygame.image.load('back.png')

#############COLLISION################
def isCollision(ecx,ecy,mcx,mcy) :
    distance = math.sqrt(math.pow(ecx - mcx,2)+ math.pow(ecy - mcy,2))
    print(distance)
    if distance < (esize / 2) + (msize / 2 ) :
        #ระยะที่ชนกัน
        return True
    else:
        return False

#############STUDENT################
#1.player

psize = 128
pimg = pygame.image.load('student.png')

px = 100
py = HEIGHT - psize
pxchange = 1
def Player(x,y):
    screen.blit(pimg,(x,y))       #วางภาพในหน้าจอ

#############BOSCO################
#2. enemy
esize = 128
eimg = pygame.image.load('person.png')
ex = 50 
ey = 0
eychange = 1
def Enemy (x,y):
    screen.blit(eimg,(x,y))






#############BOOK################
#3. book
msize = 32
mimg = pygame.image.load('book.png')
mx = 100 
my = HEIGHT - psize
mychange = 20
mstate = 'ready'
def fire_mask(x,y):
    global mstate
    mstate = 'fire'
    screen.blit(mimg,(x,y))





#############MULTI BOSCO################

exlist = []  #x ของ enemy
eylist = []  #y ของ enemy
ey_change_list = []
allenemy = 5
for i in range (allenemy) :
    exlist.append(random.randint(50, WIDTH - esize))
    eylist.append(random.randint(0,100))
    ey_change_list.append(random.randint(1,5)) #สุ่มความเร็ว enemy

    colissionmulti = isCollision(exlist[i] , eylist[i] , mx , my)
    if colissionmulti :
        my = HEIGHT - psize
        mstate = 'ready'
        eylist[i] = 0
        exlist[i] = random.randint(50,WIDTH - esize)
        allscore += 1
        ey_change_list[i] += 1

    Enemy(exlist[i] , eylist[i])

#########SCORE#########
allscore = 0 
font = pygame.font.Font('angsana.ttc' , 50)

def showscore():
    score  = font.render('คะแนน: {} คะแนน'.format(allscore) , True , (255,255,255))
    screen.blit(score,(30,30))





########sound########
#-1 รันตลอด
# pygame.mixer.music.load('beach.mp3')
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.play(-1)
# เสียงใช้ WAVต้องใช้ 16 bit , mp3ได้

sound = pygame.mixer.Sound('tang.wav')
sound.play()


##########GAMEOVER##########
def GameOver():
    overtext = 






#runโปรแกรม
running = True #บอกให้โปรแกรมทำงาน , ประกาศน้องclass เลยทำงานเล้ว
clock = pygame.time.Clock()  #game clock
FPS = 60       #framerate




while running :
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        #เช็คว่ากดปิดหรือไม่
        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pxchange = -10
            if event.key == pygame.K_RIGHT:
                pxchange = 10
            if event.key == pygame.K_SPACE:
                if mstate == 'ready' :
                    mx = px + 50
                    fire_mask(mx , my)
            
            if event.type == pygame.KEYUP:
                if event.KEY == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pxchange = 0




#################RUN#################
    #px จุดเริ่มต้น
    Player(px,py)

    if px <= 0 :
         pxchange = 1
         px += pxchange #px = px + 1

    elif px >= WIDTH - psize :
         #ความกว้างของหน้าจอ width - psize
         px = WIDTH - psize
         px += pxchange    

    else :
         px += pxchange

############RUN e ################

    # for i in range(5):
    #     Enemy(ex + (i * 100),ey)
    #     ey += eychange 
    Enemy(ex,ey)
    ey += eychange

    if mstate == 'fire':
        fire_mask(mx,my)
        my = my - mychange
##################run multi ene################
    
    for i in range(allenemy):
    #เพิ่มความเร็วของ enemy
        eylist[i] += ey_change_list[i]
        Enemy(exlist[i] , eylist[i])





    #เช็คว่า mask วิ่งไปชนขอบบนแล้วยัง ถ้าชนให้ state เปลี่ยนเป็นพร้อมยิง
    if my <= 0 :
        my = HEIGHT - psize
        mstate = 'ready'

    #เช็คว่าชนกันหรือไม่
    collision = isCollision(ex,ey,mx,my)
    if collision: 
        my = HEIGHT - psize
        mstate = 'ready'
        ey = 0 
        ex = random.randint(0,WIDTH  - esize)

        




    print(px)
    pygame.display.update() 
    pygame.event.pump()
    screen.fill((0,0,0,))
    clock.tick(FPS)
   

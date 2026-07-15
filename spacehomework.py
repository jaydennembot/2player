import pygame,pyautogui
import random
pygame.init()


print(pyautogui.size())
width,height=pyautogui.size()
#width,height=600,600
screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("the last dance")
vegeta=pygame.transform.flip(pygame.image.load("Vegeta.png"),True,False)
vegeta=pygame.transform.scale(vegeta,(160,160))
goku=pygame.image.load("GokuBlack.png")
goku=pygame.transform.scale(goku,(160,160))
rx,ry=width-220,height//2
vx,vy=120,height//2
border = pygame.Rect(width//2-10,0,20,height)
dgz=pygame.image.load("dgzarena.jpg")
BG=pygame.image.load("mainmenu.jpg")
dgz=pygame.transform.scale(dgz,(width,height))
bullet=pygame.image.load("VegetaBullets.png")
bullet=pygame.transform.scale(bullet,(50,50))
Goku=pygame.image.load("GokuBullets.png")
Goku=pygame.transform.scale(Goku,(50,50))
healthfont=pygame.font.SysFont("arial",60,True)
textfont=pygame.font.SysFont("arial",40,True)
rhealth=10
vhealth=10
GameState="start"


def draw(g1,v1,gbullets,vbullets,ghealth,vhealth,winner):
    screen.blit(dgz,(0,0))
    pygame.draw.rect(screen,"blue",border)
    # pygame.draw.rect(screen,"white",g1)
    # pygame.draw.rect(screen,"white",v1)
    screen.blit(vegeta,(v1.x-40,v1.y))
    screen.blit(goku,(g1.x-40,g1.y))
    if GameState=="start":
        message="this is a two player game ,control vegeta with wasd and goku with arrow keys \n vegeta shoot leftshift and goku shoot rightshift\nget hit and you lose one health\nthe person that loses 10 lives is the loser"
        starttext=textfont.render(message,1,"white")
        screen.blit(starttext,(100,height//3))
    elif GameState=="play":
        for i in gbullets:
            # pygame.draw.rect(screen,"grey",i)
            screen.blit(bullet,(i.x,i.y))
        for i in vbullets:
            # pygame.draw.rect(screen,"red",i)
            screen.blit(Goku,(i.x,i.y))
    else: 
        message=f"{winner} press space to restart"
        starttext=textfont.render(message,1,"white")
        screen.blit(starttext,(width//3,height//3))

    gtext=healthfont.render(f"health:{ghealth}",1,"white")
    vtext=healthfont.render(f"health:{vhealth}",1,"white")
    screen.blit(gtext,(width-300,50))
    screen.blit(vtext,(50,50))

def handlebullets(g1,v1,gbullets,vbullets,ghealth,vhealth):
    for i in gbullets:
        i.x-=10
        if i.x <0:
            gbullets.remove(i)
        if i.colliderect(v1):
            gbullets.remove(i)
            vhealth=vhealth-1
            print(vhealth)
        
    for i in vbullets:
        i.x+=10
        if i.x >width:
            vbullets.remove(i)
        if i.colliderect(g1):
            vbullets.remove(i)
            ghealth-=1
            continue
        for j in gbullets:
            if i.colliderect(j):
                vbullets.remove(i)
                gbullets.remove(j)
                break
    return ghealth,vhealth




def movement(g1,v1,button):
    # print(button)
    if button[pygame.K_w]and v1.y>0:
        v1.y-=10
    if button[pygame.K_a]and v1.x>0 :
        v1.x-=10
    if button[pygame.K_s]and v1.y<height-v1.height:
        v1.y+=10
    if button[pygame.K_d]and v1.x<border.x-v1.width:
        v1.x+=10
        print("hello")
    if button[pygame.K_UP]and g1.y>0:
        g1.y-=10
    if button[pygame.K_DOWN]and g1.y<height-g1.height:
        g1.y+=10
    if button[pygame.K_LEFT]and g1.x>border.x+border.width:
        g1.x-=10
    if button[pygame.K_RIGHT]and g1.x<width-g1.width:
        g1.x+=10


def main():
    global GameState,ghealth,vhealth
    g1=pygame.Rect(rx,ry,80,140)
    v1=pygame.Rect(vx,vy,80,140)
    gbullets=[]
    vbullets=[]
    ghealth=10
    vhealth=10
    winner=None
    while True:
    
        draw(g1,v1,gbullets,vbullets,ghealth,vhealth,winner)
        # print(GameState)
        for i in pygame.event.get():
            
            if i.type == pygame.QUIT :
                pygame.quit()
            if i.type== pygame.KEYDOWN:
                if i.key == pygame.K_SPACE and GameState !="play":
                    GameState="play"
                    vhealth=10
                    ghealth=10
                    winner=None
                    gbullets=[]
                    vbullets=[]
            

                if i.key == pygame.K_LSHIFT and GameState=="play": 
                    b=pygame.Rect(v1.x-50,v1.y+50,50,50)
                    vbullets.append(b)
                if i.key == pygame.K_RSHIFT and GameState=="play":
                    b=pygame.Rect(g1.x-50,g1.y+50,50,50)
                    gbullets.append(b)
        
        if GameState=="play":
            button=pygame.key.get_pressed()
            movement(g1,v1,button)
    
            ghealth,vhealth=handlebullets(g1,v1,gbullets,vbullets,ghealth,vhealth)
        if ghealth==0:
            winner="Vegeta wins"
        if vhealth==0:
            winner="Goke black wins"
        if winner:
            GameState="end"
        pygame.display.update()





main()


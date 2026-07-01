import pygame,pyautogui
import random
pygame.init()


print(pyautogui.size())
width,height=pyautogui.size()
#width,height=600,600
screen=pygame.display.set_mode((width,height))


pygame.display.set_caption("space invasion")
Vegeta=pygame.transform.flip(pygame.image.load("Vegeta.png"),True,False)
Vegeta=pygame.transform.scale(Vegeta,(160,160))
Goku=pygame.image.load("GokuBlack.png")
Goku=pygame.transform.scale(Goku,(160,160))
rx,ry=width-220,height//2
vx,vy=120,height//2
border = pygame.Rect(width//2-10,0,20,height)
space=pygame.image.load("dgzarena.jpg")
space=pygame.transform.scale(space,(width,height))
bullet=pygame.image.load("VegetaBullets.png")
bullet=pygame.transform.scale(bullet,(100,100))
bbullet=pygame.image.load("GokuBullets.png")
bbullet=pygame.transform.scale(bbullet,(100,100))
healthfont=pygame.font.SysFont("arial",60,True)
textfont=pygame.font.SysFont("arial",40,True)
Ghealth=10
Vhealth=10
GameState="start"
def draw(r1,v1,Gbullets,Vbullets,Ghealth,Vhealth,winner):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"blue",border)
    # pygame.draw.rect(screen,"white",r1)
    # pygame.draw.rect(screen,"white",v1)
    screen.blit(Vegeta,(v1.x-40,v1.y))
    screen.blit(Goku,(r1.x-40,r1.y))
    if GameState=="start":
        message="this is a two player game ,control Vegeta with wasd and Goku with arrow keys \n Vegeta shoot leftshift and Goku shoot rightshift\nget hit and you lose one health\nthe person that loses 10 lives is the loser"
        starttext=textfont.render(message,1,"white")
        screen.blit(starttext,(width//3,height//3))
    if GameState=="play":
        for i in Gbullets:
            # pygame.draw.rect(screen,"grey",i)
            screen.blit(bullet,(i.x,i.y))
        for i in Vbullets:
            # pygame.draw.rect(screen,"red",i)
            screen.blit(bbullet,(i.x,i.y))

    Gtext=healthfont.render(f"health:{Ghealth}",1,"white")
    Vtext=healthfont.render(f"health:{Vhealth}",1,"white")
    screen.blit(Gtext,(width-300,50))
    screen.blit(Vtext,(50,50))

def handlebullets(r1,v1,Gbullets,Vbullets,Ghealth,Vhealth):
    for i in Gbullets:
        i.x-=10
        if i.x <0:
            Gbullets.remove(i)
        if i.colliderect(v1):
            Gbullets.remove(i)
            Vhealth=Vhealth-1
            print(Vhealth)
        
    for i in Vbullets:
        i.x+=10
        if i.x >width:
            Vbullets.remove(i)
        if i.colliderect(r1):
            Vbullets.remove(i)
            Ghealth-=1
            continue
        for j in Gbullets:
            if i.colliderect(j):
                Vbullets.remove(i)
                Gbullets.remove(j)
                break
    return Ghealth,Vhealth





def movement(G1,V1,button):
    # print(button)
    if button[pygame.K_w]and V1.y>0:
        V1.y-=10
    if button[pygame.K_a]and V1.x>0 :
        V1.x-=10
    if button[pygame.K_s]and V1.y<height-V1.height:
        V1.y+=10
    if button[pygame.K_d]and V1.x<border.x-V1.width:
        V1.x+=10
        print("hello")
    if button[pygame.K_UP]and G1.y>0:
        G1.y-=10
    if button[pygame.K_DOWN]and G1.y<height-G1.height:
        G1.y+=10
    if button[pygame.K_LEFT]and G1.x>border.x+border.width:
        G1.x-=10
    if button[pygame.K_RIGHT]and G1.x<width-G1.width:
        G1.x+=10
    


def main():
    global GameState,Ghealth,Vhealth
    G1=pygame.Rect(rx,ry,80,140)
    V1=pygame.Rect(vx,vy,80,140)
    Gbullets=[]
    Vbullets=[]
    # Ghealth=10
    # Vhealth=10
    winner=None
    while True:
    
        draw(G1,V1,Gbullets,Vbullets,Ghealth,Vhealth,winner)
        # print(GameState)
        for i in pygame.event.get():
            
            if i.type == pygame.QUIT :
                pygame.quit()
            if i.type== pygame.KEYDOWN:
                if i.key == pygame.K_SPACE and GameState !="play":
                    GameState="play"
                    Vhealth=10
                    Ghealth=10
                    winner=None
                    Gbullets=[]
                    Vbullets=[]

                if i.key == pygame.K_LSHIFT :
                    b=pygame.Rect(V1.x-50,V1.y+50,50,15)
                    Vbullets.append(b)
                if i.key == pygame.K_RSHIFT:
                    b=pygame.Rect(G1.x-50,G1.y+50,50,15)
                    Gbullets.append(b)
        button=pygame.key.get_pressed()
        movement(G1,V1,button)
    
        Ghealth,Vhealth=handlebullets(G1,V1,Gbullets,Vbullets,Ghealth,Vhealth)
        if Ghealth==0:
            winner="Vegeta wins"
        if Vhealth==0:
            winner="Goku wins"
        if winner:
            GameState="end"
        pygame.display.update()





main()



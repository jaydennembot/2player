import pygame,pyautogui
import random
pygame.init()


print(pyautogui.size())
width,height=pyautogui.size()
#width,height=600,600
screen=pygame.display.set_mode((width,height))


pygame.display.set_caption("space invasion")
vampire=pygame.transform.flip(pygame.image.load("vampire.png"),True,False)
vampire=pygame.transform.scale(vampire,(160,160))
robot=pygame.image.load("robot.png")
robot=pygame.transform.scale(robot,(160,160))
rx,ry=width-220,height//2
vx,vy=120,height//2
border = pygame.Rect(width//2-10,0,20,height)
space=pygame.image.load("space.jpg")
space=pygame.transform.scale(space,(width,height))
bullet=pygame.image.load("vegetabullets.png")
bullet=pygame.transform.scale(bullet,(100,100))
bbullet=pygame.image.load("bball.png")
bbullet=pygame.transform.scale(bbullet,(100,100))
healthfont=pygame.font.SysFont("arial",60,True)
textfont=pygame.font.SysFont("arial",40,True)
rhealth=10
vhealth=10
GameState="start"
def draw(r1,v1,rbullets,vbullets,rhealth,vhealth,winner):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"blue",border)
    # pygame.draw.rect(screen,"white",r1)
    # pygame.draw.rect(screen,"white",v1)
    screen.blit(vampire,(v1.x-40,v1.y))
    screen.blit(robot,(r1.x-40,r1.y))
    if GameState=="start":
        message="this is a two player game ,control vampire with wasd and robot with arrow keys \n vampire shoot leftshift and robot shoot rightshift\nget hit and you lose one health\nthe person that loses 10 lives is the loser"
        starttext=textfont.render(message,1,"white")
        screen.blit(starttext,(width//3,height//3))
    if GameState=="play":
        for i in rbullets:
            # pygame.draw.rect(screen,"grey",i)
            screen.blit(bullet,(i.x,i.y))
        for i in vbullets:
            # pygame.draw.rect(screen,"red",i)
            screen.blit(bbullet,(i.x,i.y))

    rtext=healthfont.render(f"health:{rhealth}",1,"white")
    vtext=healthfont.render(f"health:{vhealth}",1,"white")
    screen.blit(rtext,(width-300,50))
    screen.blit(vtext,(50,50))

def handlebullets(r1,v1,rbullets,vbullets,rhealth,vhealth):
    for i in rbullets:
        i.x-=10
        if i.x <0:
            rbullets.remove(i)
        if i.colliderect(v1):
            rbullets.remove(i)
            vhealth=vhealth-1
            print(vhealth)
        
    for i in vbullets:
        i.x+=10
        if i.x >width:
            vbullets.remove(i)
        if i.colliderect(r1):
            vbullets.remove(i)
            rhealth-=1
            continue
        for j in rbullets:
            if i.colliderect(j):
                vbullets.remove(i)
                rbullets.remove(j)
                break
    return rhealth,vhealth
    




def movement(r1,v1,button):
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
    if button[pygame.K_UP]and r1.y>0:
        r1.y-=10
    if button[pygame.K_DOWN]and r1.y<height-r1.height:
        r1.y+=10
    if button[pygame.K_LEFT]and r1.x>border.x+border.width:
        r1.x-=10
    if button[pygame.K_RIGHT]and r1.x<width-r1.width:
        r1.x+=10
    


def main():
    global GameState,rhealth,vhealth
    r1=pygame.Rect(rx,ry,80,140)
    v1=pygame.Rect(vx,vy,80,140)
    rbullets=[]
    vbullets=[]
    # rhealth=10
    # vhealth=10
    winner=None
    while True:
    
        draw(r1,v1,rbullets,vbullets,rhealth,vhealth,winner)
        # print(GameState)
        for i in pygame.event.get():
            
            if i.type == pygame.QUIT :
                pygame.quit()
            if i.type== pygame.KEYDOWN:
                if i.key == pygame.K_SPACE and GameState !="play":
                    GameState="play"
                    vhealth=10
                    rhealth=10
                    winner=None
                    rbullets=[]
                    vbullets=[]

                if i.key == pygame.K_LSHIFT :
                    b=pygame.Rect(v1.x-50,v1.y+50,50,15)
                    vbullets.append(b)
                if i.key == pygame.K_RSHIFT:
                    b=pygame.Rect(r1.x-50,r1.y+50,50,15)
                    rbullets.append(b)
        button=pygame.key.get_pressed()
        movement(r1,v1,button)
    
        rhealth,vhealth=handlebullets(r1,v1,rbullets,vbullets,rhealth,vhealth)
        if rhealth==0:
            winner="vampire wins"
        if vhealth==0:
            winner="robot wins"
        if winner:
            GameState="end"
        pygame.display.update()





main()


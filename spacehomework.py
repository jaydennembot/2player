import pygame,pyautogui
import random
pygame.init()


print(pyautogui.size())
width,height=pyautogui.size()
#width,height=600,600
screen=pygame.display.set_mode((width,height))


pygame.display.set_caption("dbz arena")
vegeta=pygame.transform.flip(pygame.image.load("vegeta.png"),True,False)
vegeta=pygame.transform.scale(vegeta,(160,160))
Goku=pygame.image.load("GokuBlack.png")
Goku=pygame.transform.scale(Goku,(160,160))
vx,vy=width-220,height//2
gx,gy=120,height//2
border = pygame.Rect(width//2-10,0,20,height)
dgz=pygame.image.load("dgzarena.jpg")
dgz=pygame.transform.scale(dgz,(width,height))

def draw(v1,g1,vbullets,gbullets):
    screen.blit(dgz,(0,0))
    pygame.draw.rect(screen,"blue",border)
    # pygame.draw.rect(screen,"white",r1)
    # pygame.draw.rect(screen,"white",v1)
    screen.blit(vegeta,(v1.x-40,v1.y))
    screen.blit(Goku,(g1.x-40,g1.y))
    for i in gbullets:
        pygame.image.load("gokubullets.avif")
    for i in vbullets:
        pygame.image.load(screen,"red",i)
def handlebullets(g1,v1,gbullets,vbullets):
    for i in gbullets:
        i.x-=10
        if i.x <0:
            gbullets.remove(i)
    for i in vbullets:
        i.x+=10
        if i.x >width:
            vbullets.remove(i)


    




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
    g1=pygame.Rect(gx,gy,80,140)
    v1=pygame.Rect(vx,vy,80,140)
    gbullets=[]
    vbullets=[]
    while True:
    
        draw(g1,v1,gbullets,vbullets)
        for i in pygame.event.get():
            
            if i.type == pygame.QUIT :
                pygame.quit()
            if i.type== pygame.KEYDOWN:
                if i.key == pygame.K_LSHIFT:
                    b=pygame.image.load("vegetabullets.png",v1.x-50,v1.y+50,50,15)
                    vbullets.append(b)
                if i.key == pygame.K_RSHIFT:
                    b=pygame.image.load("gokubullets.avif",g1.x-50,g1.y+50,50,15)
                    gbullets.append(b)
        button=pygame.key.get_pressed()
        print(button)
        movement(g1,v1,button)
        handlebullets(g1,v1,gbullets,vbullets)

        pygame.display.update()





main()


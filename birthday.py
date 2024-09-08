import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600
display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img=pygame.image.load("Pro Python Game Development 2/birthday animation/first page.jpg")
image=pygame.transform.scale(img,(WIDTH,HEIGHT))





run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    font=pygame.font.SysFont("Times New Roman",55)
    text=font.render("Happy Birthday",True,"black")
    display_surface.fill("white")
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(140,150))
    pygame.display.update()
    time.sleep(2)

    img2=pygame.image.load("Pro Python Game Development 2/birthday animation/second page.jpg")
    image2=pygame.transform.scale(img2,(WIDTH,HEIGHT))

    font2=pygame.font.SysFont("Times New Roman",55)
    text2=font2.render("May all your wishes come true",True,"black")
    display_surface.fill("white")
    display_surface.blit(image2,(0,0))
    display_surface.blit(text2,(0,100))
    pygame.display.update()
    time.sleep(2)

    img3=pygame.image.load("Pro Python Game Development 2/birthday animation/third page.jpg")
    image3=pygame.transform.scale(img3,(WIDTH,HEIGHT))

    font3=pygame.font.SysFont("Times New Roman",55)
    text3=font3.render("Many more happy returns",True,"black")
    text4=font3.render("of the day",True,"black")
    
    display_surface.fill("white")
    display_surface.blit(image3,(0,0))
    display_surface.blit(text3,(0,100))
    display_surface.blit(text4,(200,150))
    pygame.display.update()
    time.sleep(2)
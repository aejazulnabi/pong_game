from pgzero.actor import Actor
from pgzero.clock import clock
from random import randint, choice # Importa choice da random
import pgzrun
 
TITLE = "Colpisci la palla"
WIDTH = 800
HEIGHT = 600
 
messaggio = ""
palla = Actor("palla")
guanto = Actor("guanto")
guanto2 = Actor("guanto")
background = Actor('campo')
 
guanto.pos = 80, HEIGHT       
guanto2.pos = WIDTH-80, HEIGHT
 

verso_guanto2 =choice([-1, 1])
 
palla_vx = 7*choice([-1, 1]) 
palla_vy = 7*choice([-1, 1])

def draw():
    background.draw() 
    palla.draw()
    guanto.draw()
    guanto2.draw()
    screen.draw.text(messaggio, center=(400, 40), fontsize=60, color="white")
 
def update():
    global palla_vx, palla_vy
    if palla.bottom>=HEIGHT:
        palla.bottom==HEIGHT
    if palla.top>=HEIGHT:
        palla.top==0
    
    if palla.top<=0 or palla.bottom>=HEIGHT:
        palla_vy*=-1
    
    if guanto.colliderect(palla):
        palla_vx*=-1
    if guanto2.colliderect(palla):
        palla_vx*=-1
        
      

    
    
    
    if keyboard.up:
        guanto.y -= 10
    if keyboard.down:
        guanto.y += 10
    #guanto2.y += verso_guanto2 * 10
    if guanto.top < 0:
        guanto.top = 0
    if guanto.bottom > HEIGHT:
        guanto.bottom = HEIGHT
    if guanto2.top < 0:
        guanto2.top = 0
    if guanto2.bottom > HEIGHT:
        guanto2.bottom = HEIGHT
    
    if palla.left > WIDTH or palla.right < 0:
        piazza_palla()
    
    if palla.y > guanto2.y: 
        guanto2.y += 7
    elif palla.y < guanto2.y: 
        guanto2.y -= 7
    
    palla.x += palla_vx
    palla.y += palla_vy
 
#def movpc():
 #   global verso_guanto2
 #   verso_guanto2 = choice([-1, 1])
 
verso_guanto2
def piazza_palla():
    global palla_vx, palla_vy
    palla.pos = (WIDTH // 2, HEIGHT // 2)
    palla_vx = 7*choice([-1, 1])
    palla_vy = 7*choice([-1, 1])



piazza_palla() 
#clock.schedule_interval(piazza_palla, 20.0)

pgzrun.go()
 




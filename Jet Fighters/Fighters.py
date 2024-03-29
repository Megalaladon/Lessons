import pygame
import os

#pygame.mixer.init()
pygame.font.init()


pygame.display.set_caption("Jet Fighters")

WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

HEALTH_FONT = pygame.font.SysFont('comicsans',30)
WINNER_FONT = pygame.font.SysFont("Comicsans",100)

BULLET_SPEED = 5
BULLET_NUMBER = 5

YELLOW_HIT = pygame.USEREVENT +1
BLUE_HIT = pygame.USEREVENT +2

#BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Sounds','Fire.mp3'))
#BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Sounds','Hit.mp3'))
BLUE= ((0,0,255))
YELLOW = ((255,255,0))

FPS = 60

VELOCITY = 3

WHITE = ((255,255,255))

MID_BORDER = pygame.Rect((WIDTH/2)-2.5,0,5, HEIGHT)

YELLOW_JET = pygame.image.load(os.path.join('images','YellowJet.png'))
YJET = pygame.transform.rotate(YELLOW_JET,270)
BLUE_JET = pygame.image.load(os.path.join('images','BlueJet.png'))
BJet = pygame.transform.rotate(BLUE_JET,90)
SKY = pygame.transform.scale(pygame.image.load(os.path.join('Images','sky.png')), (WIDTH,HEIGHT))

def draw(yellow,blue,yellow_bullets,blue_bullets,yellow_health,blue_health):
    WIN.blit(SKY,(0,0 ))
    pygame.draw.rect(WIN,WHITE,MID_BORDER)
    WIN.blit(YJET,(yellow.x,yellow.y))
    WIN.blit(BJet,(blue.x,blue.y))
    for bullet in blue_bullets:
        pygame.draw.rect(WIN,BLUE, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullet)
    yellow_health_txt = HEALTH_FONT.render("Health: "+ str(yellow_health),1,WHITE)
    blue_health_txt = HEALTH_FONT.render("Health: "+ str(blue_health),1,WHITE)
    WIN.blit(yellow_health_txt,(10,10))
    WIN.blit(blue_health_txt,(WIDTH - blue_health_txt.get_width()-10,10))
    pygame.display.update()

def winner_draw(text):
    draw_text = WINNER_FONT.render(text,1,WHITE)
    WIN.blit(draw_text,(WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def yellow_move(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0: #LEFT
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < MID_BORDER.x:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0: #UP
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT: #DOWN
        yellow.y += VELOCITY

def blue_move(keys_pressed,blue):
    if keys_pressed[pygame.K_LEFT] and blue.x - VELOCITY > MID_BORDER.x + MID_BORDER.width: #LEFT
        blue.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and blue.x + VELOCITY + blue.width < WIDTH:
        blue.x += VELOCITY
    if keys_pressed[pygame.K_UP] and blue.y - VELOCITY >0 :
        blue.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and blue.y + VELOCITY + blue.width < HEIGHT: #Down
        blue.y += VELOCITY

def bullet_handle(yellow_bullets,blue_bullets,yellow, blue):
    for  bullet in yellow_bullets:
        bullet.x +=BULLET_SPEED
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in blue_bullets:
        bullet.x -= BULLET_SPEED
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            blue_bullets.remove(bullet)
        elif bullet.x < 0:
            blue_bullets.remove(bullet)





def main():
    yellow = pygame.Rect(200,250,32,32)
    blue = pygame.Rect(650,250,32,32)

    yellow_bullets = []
    blue_bullets = []

    yellow_health = 100
    blue_health = 100

    run= True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and len(yellow_bullets) < BULLET_NUMBER:
                bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//22 -2,10,5)
                yellow_bullets.append(bullet)
               # BULLET_FIRE_SOUND.play()
            if event.key == pygame.K_RCTRL and len(blue_bullets) < BULLET_NUMBER:
                bullet = pygame.Rect(blue.x,blue.width +blue.y+ blue.height//22 -2,10,5)
                blue_bullets.append(bullet)
                #BULLET_FIRE_SOUND.play()
        if event.type == YELLOW_HIT:
            yellow_health = yellow_health - 10
            #BULLET_HIT_SOUND.play()
        if event.type == BLUE_HIT:
            blue_health = blue_health - 10
            #BULLET_HIT_SOUND.play()

        winner_msg = ""
        if yellow_health <= 0:
            winner_msg = "Blue Wins!"
        if blue_health <=0:
            winner_msg = "Yellow Wins!"
        if winner_msg != "":
            winner_draw(winner_msg)
            break
        keys_pressed = pygame.key.get_pressed()
        yellow_move(keys_pressed,yellow)
        blue_move(keys_pressed,blue)
        bullet_handle(yellow_bullets,blue_bullets,yellow, blue)
        draw(yellow,blue,yellow_bullets, blue_bullets, yellow_health,blue_health)            
    

if __name__=="__main__":
    main()

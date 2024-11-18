import pygame
import os
import time
pygame.init()
pygame.font.init()
pygame.mixer.init()
FPS = 60
WIDTH, HEIGHT = 500, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FIRE FALL")
pygame.display.set_icon(pygame.image.load(os.path.join("Assets", "Plane.png")))
TOP = pygame.Rect(0, 0, 500, 10)
L_SIDE = pygame.Rect(0 , 0, 10, 700)
R_SIDE = pygame.Rect(WIDTH - 10 , 0, 10, HEIGHT)
DOWN = pygame.Rect(0 , HEIGHT - 10, WIDTH, 10)
CLOUD = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "#clouds.jfif")),(WIDTH, HEIGHT))
COMET = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "game_flame.png")),(15, 25))
LIFE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "life.png")),(15, 20))
GREEN =  pygame.transform.scale(pygame.image.load(os.path.join("Assets", "green.png")),(WIDTH, HEIGHT))
RED =  pygame.transform.scale(pygame.image.load(os.path.join("Assets", "red.png")),(WIDTH, HEIGHT))
YELLOW =  pygame.transform.scale(pygame.image.load(os.path.join("Assets", "yellow.png")),(WIDTH, HEIGHT))
HEAD = pygame.font.SysFont("bold", 25)
HEADER= pygame.font.Font("Font/umberto/umberto.ttf", 30)
WINNER_FONT = pygame.font.Font("Font/dogica/dogica.ttf", 30)
TIME_FONT = pygame.font.SysFont("consolas", 30)
GOOD_FONT = pygame.font.SysFont("comicsans", 25)
BALL =pygame.image.load(os.path.join("Assets", "Plane.png"))
FIREBALL = pygame.transform.scale(BALL, (50, 50))
#To get player input
player_font = pygame.font.Font(None, 32)
#for the sounds
HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets/audio", "GAME HIT.mp3")) 
pygame.mixer.music.load(os.path.join("Assets/audio", "cloud-rap-sample-25962.mp3"))
INTRO_SOUND = pygame.mixer.Sound(os.path.join("Assets/audio", "INTRO GAME Edit 1 Export 1.wav"))
END_MUSIC= pygame.mixer.Sound(os.path.join("Assets/audio", "END MUSIC Edit 1 Export 1.wav"))
LIFE_MUSIC = pygame.mixer.Sound(os.path.join("Assets/audio", "mixkit-arcade-video-game-bonus-2044.wav"))
VEL = 3
BLOCK_VEL = 7
HIT = pygame.USEREVENT + 1
ADD = pygame.USEREVENT +2
MAX_BLOCKA = 7
MAX_BLOCKB = 10
MAX_BLOCKC = 15
MAX_BLOCKD = 20
MAX_BLOCKE = 25
MAX_BLOCKF = 35
MAX_BLOCKG = 50

def COVER():
    front = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "FIRE FALL.png")),(WIDTH, HEIGHT))
    logo = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "EC PAGE.png")),(WIDTH, HEIGHT)) 
    INTRO_SOUND.play()
    WIN.blit(front, (0, 0))
    draw_text = HEAD.render("Get ready ...", 0.5, (0, 0, 0))
    WIN.blit(draw_text, ((WIDTH/2 - draw_text.get_width()/2),  630))
    pygame.display.update()
    pygame.time.delay(5000)
    WIN.blit(logo, (0,0))
    pygame.display.update()
    pygame.time.delay(2000)
    
    INTRO_SOUND.stop()


COVER()

def user_name():
    user_text = " "
    for events in pygame.event.get():
        if events.type == pygame.KEYDOWN:
            user_text += events.unicode
    WIN.fill((0,0,0))
    text_surface = player_font.render(user_text,True, (250, 230, 0))
    WIN.blit(text_surface, (0,0))
def wallpaper(text1,text2, ball,aye, Blocks):

    PURPLE = (255, 30, 255)
    LIGHT_GREEN = (12, 255, 30)
    BLUE = (2, 2, 150)
    bleu = (80, 129, 160)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    Red = (255, 0, 0)
    yellow = (250, 230, 0)
    
    if text2>0 and text2<70:
        WIN.blit(CLOUD, (0, 0))
        
        pygame.draw.rect(WIN, BLACK, TOP)
        pygame.draw.rect(WIN,BLACK, L_SIDE)
        pygame.draw.rect(WIN,BLACK, R_SIDE)
        pygame.draw.rect(WIN,BLACK, DOWN)
    if text2 >= 70 and text2 <200:
        WIN.blit(GREEN, (0,0))
        green = (0, 200, 30)
    
        pygame.draw.rect(WIN, green, TOP)
        pygame.draw.rect(WIN, green, L_SIDE)
        pygame.draw.rect(WIN, green, R_SIDE)
        pygame.draw.rect(WIN, green, DOWN)
    if text2 >= 200 and text2<400:
        WIN.blit(RED, (0, 0))
        red =(200,0, 10)
        pygame.draw.rect(WIN, red, TOP)
        pygame.draw.rect(WIN, red, L_SIDE)
        pygame.draw.rect(WIN, red, R_SIDE)
        pygame.draw.rect(WIN, red, DOWN)

    if text2 >=400:
        WIN.blit(YELLOW, (0, 0))
        yellow = (250, 230, 0)
        pygame.draw.rect(WIN, yellow, TOP)
        pygame.draw.rect(WIN, yellow, L_SIDE)
        pygame.draw.rect(WIN, yellow, R_SIDE)
        pygame.draw.rect(WIN, yellow, DOWN)

    WIN.blit(FIREBALL, (ball.x, ball.y))
    
   

    draw_text1 = HEADER.render("HEALTH: " + str(text1), 2, (BLACK))
    draw_text2 =HEADER.render("SCORE: " + str(text2), 2, (BLACK)) 
    WIN.blit(draw_text1, (10, 15))
    WIN.blit(draw_text2,(500-draw_text2.get_width()-10, 15 ))
    for eyan in aye:
        WIN.blit(LIFE, (eyan.x, eyan.y))
    for block in Blocks:
        WIN.blit(COMET, (block.x, block.y))
    
    pygame.display.update()
def controls(keysPressed, ball):
        if keysPressed[pygame.K_LEFT] and ball.x - VEL > 0:
            ball.x -= VEL
        if keysPressed[pygame.K_RIGHT] and ball.x + VEL + ball.width <WIDTH:
            ball.x += VEL
        if keysPressed[pygame.K_UP] and ball.y - VEL > 0:
            ball.y -= VEL
        if keysPressed[pygame.K_DOWN] and ball.y + VEL + ball.width <HEIGHT:
            ball.y += VEL
        
def handle_Hit(Blocks, ball):
    for block in Blocks:
        block.y += BLOCK_VEL
        if ball.colliderect(block):
            pygame.event.post(pygame.event.Event(HIT))
            HIT_SOUND.play()
            Blocks.remove(block)
        elif block.y > HEIGHT:
            Blocks.remove(block)
        
def life(aye, ball):
    for eyan in aye:
        eyan.y += BLOCK_VEL
        if ball.colliderect(eyan):
            pygame.event.post(pygame.event.Event(ADD))
            LIFE_MUSIC.play()
            aye.remove(eyan)
        elif eyan.y > HEIGHT:
            aye.remove(eyan)

def LOSS(Winner):
    draw_text = WINNER_FONT.render(Winner, 1, (0, 0, 0))
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    pygame.mixer.music.play(-1)
    import random         
    ball = pygame.Rect(300, 600, 50, 50)
    eyan = pygame.Rect((random.choice(range(10,490))), 0, 10, 10)
    Blocks = []
    aye = []
    clock = pygame.time.Clock()
    run = True
    text1 = 10
    start_time = 0
    text2 = 0
    full = time.time()
    while run:
        clock.tick(FPS)
        keysPressed = pygame.key.get_pressed()
        if Blocks ==[]:
            empty = 0
            empty = time.time()
            number = empty-full
            if number>= 3.5:
                delay_text = WINNER_FONT.render("YOU GOT FROZEN", 1, (0, 0, 0))
                WIN.blit(delay_text, (WIDTH/2 - delay_text.get_width()/2, HEIGHT/2 - delay_text.get_height()/2))
                pygame.display.update()
                pygame.mixer.music.stop()
                END_MUSIC.play()
                pygame.time.delay(3000)
                run=False
                break

        if Blocks != []:
            full = time.time()
        
        for event in pygame.event.get():
                    
            start_time = pygame.time.get_ticks()
            text2 = start_time/1000
            text2 = round(text2)
            if event.type == pygame.QUIT:
                run = False
                break
            
            if  text2 <5 and len(Blocks) < MAX_BLOCKA :
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)
            if text2>5  and len(Blocks) < MAX_BLOCKB:
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)  
            if text2>10 and text2<=20 and len(Blocks) < MAX_BLOCKC:
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)
                if text1<= 4 and len(aye) < 1:
                    eyan = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                    aye.append(eyan)
            if text2>30 and text2<=40 and len(Blocks) < MAX_BLOCKD:
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)
                if text1<= 3 and len(aye) < 2:
                    eyan = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                    aye.append(eyan)
            if text2>40 and text2<=50 and len(Blocks) < MAX_BLOCKE:
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)
            if text2>50 and text2<=60 and len(Blocks) < MAX_BLOCKF:
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)
                if text1<= 3 and len(aye) < 3:
                    eyan = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                    aye.append(eyan)
            if  text2>60 and text2<=70 and len(Blocks) < 32:
                for block in Blocks:
                    block.y += 8
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)
                if text1<= 2 and len(aye) <3:
                    eyan = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                    aye.append(eyan)
            if text2>70 and text2<=100 and len(Blocks) < MAX_BLOCKG:
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)
                if text1<= 2 and len(aye) < 3:
                    eyan = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                    aye.append(eyan)
            if text2>100 and text2<=120 and len(Blocks)< 65:
                for block in Blocks:
                    block.y += 5
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)
                if text1<= 2 and len(aye) < 2:
                    eyan.y += 5
                    eyan = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                    aye.append(eyan)
            if text2>120 and text2<=150 and len(Blocks)< 80:
                for block in Blocks:
                    block.y += 10
                block = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                Blocks.append(block)
                if text1<= 2 and len(aye) < 2:
                    eyan.y += 10
                    eyan = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                    aye.append(eyan)
            if text2>200 and text2<=250 and len(Blocks)< 90:
                for block in Blocks:
                    block.y += 10
                block = pygame.Rect((random.choice(range(10,490))), 0, 30, 20)
                Blocks.append(block)
                if text1<= 1 and len(aye) < 2:
                    eyan.y += 10
                    eyan = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                    aye.append(eyan)
            if text2>250 and len(Blocks)< 100:
                for block in Blocks:
                    block.y += 15
                block = pygame.Rect((random.choice(range(10,490))), 0, 45, 20)
                Blocks.append(block)
                if text1<= 1 and len(aye) < 1:
                    eyan.y += 15
                    eyan = pygame.Rect((random.choice(range(10,490))), 0, 15, 20)
                    aye.append(eyan) 
            
            if event.type == HIT:
                text1 -= 1
                if text2>200:
                    text1 -=2
            Winner = ""        
            if text1 <= 0:
                Winner = "YOU LOST :("
                pygame.mixer.music.stop()
                END_MUSIC.play()
            if event.type == ADD:
                text1 += 1   
            if Winner != "":
                LOSS(Winner)
                timely = time.time()
                text = [f"{text2} <--{time.ctime(timely)} \n"]
                with open("FIRE_FALL.txt", "a") as file:
                    file.writelines(text)

                    file.close()
        
                run = False
                break

        
        controls(keysPressed, ball)
        handle_Hit(Blocks, ball)
        life(aye, ball)
        wallpaper(text1, text2, ball, aye, Blocks)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()

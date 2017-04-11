#My Snake Game Project
import pygame;
import random;

#Initialise Pygame
pygame.init();

#Initialise Main Constants
WIDTH=800;
HEIGHT=600;
TITLE="Jack's Snake";
ICON=pygame.image.load("img/icon.png");
BLOCK_SIZE=20;

#Setup Pygame Window
gameSurface=pygame.display.set_mode((WIDTH,HEIGHT));
pygame.display.set_caption(TITLE);
pygame.display.set_icon(ICON);

#Start Clock
clock=pygame.time.Clock();

#Define Colours
WHITE=(255,255,255);
BLACK=(0,0,0);
GREY=(128,128,128);
LG=(200,200,200);
RED=(255,0,0);
GREEN=(0,255,0);
BLUE=(0,0,255);

#Title-Screen Images
title_backdrop = pygame.image.load("img/title_background.png");
#Buttons
button=pygame.image.load("img/button.png");
button_hover=pygame.image.load("img/button_hover.png");

#In-Game Images
snake_img = pygame.image.load("img/snakeHead.png");
apple_img = pygame.image.load("img/apple.png");
apple_eaten_img = pygame.image.load("img/appleEaten.png");

#Define Fonts
smallfont = pygame.font.SysFont("comicsansms",25);
medfont = pygame.font.SysFont("comicsansms",50);
largefont = pygame.font.SysFont("comicsansms",75);

#Functions
def snake(BLOCK_SIZE,snakeList,direction):
    if direction == "LEFT":
        head=pygame.transform.rotate(snake_img,180);
    elif direction == "RIGHT":
        head=pygame.transform.rotate(snake_img,0);
    elif direction == "UP":
        head=pygame.transform.rotate(snake_img,90);
    elif direction == "DOWN":
        head=pygame.transform.rotate(snake_img,270);
    gameSurface.blit(head,(snakeList[-1][0],snakeList[-1][1]));
    for xy in snakeList[:-1]:
        pygame.draw.rect(gameSurface,BLACK,[xy[0],xy[1],BLOCK_SIZE,BLOCK_SIZE]);

def set_apple():
    xx=random.randrange(0,(WIDTH/BLOCK_SIZE)-1)*BLOCK_SIZE;
    yy=random.randrange(0,(HEIGHT/BLOCK_SIZE)-1)*BLOCK_SIZE;
    return xx, yy;

def text_objects(text,colour,size):
    if(size=="small"):
        textSurface=smallfont.render(text,True,colour);
    elif(size=="medium"):
        textSurface=medfont.render(text,True,colour);
    elif(size=="large"):
        textSurface=largefont.render(text,True,colour);
        
    return textSurface, textSurface.get_rect();

def draw_text(text,colour,size,yOffset):
    textSurf,textRect=text_objects(text,colour,size);
    textRect.center=WIDTH/2,(HEIGHT/2)+yOffset;
    gameSurface.blit(textSurf,textRect);

def draw_button_text(text,colour,size,xCo,yCo):
    textSurf,textRect=text_objects(text,colour,size);
    textRect.center=xCo,yCo;
    gameSurface.blit(textSurf,textRect);

def draw_instruction(text,colour,size,xCo,yCo):
    textSurf,textRect=text_objects(text,colour,size);
    textRect.topleft=xCo,yCo;
    gameSurface.blit(textSurf,textRect);

def score(score,colour,size):
    textSurf,textRect=text_objects(score,colour,size);
    textRect.topleft=10,10;
    gameSurface.blit(textSurf,textRect);

def quit_game():
    pygame.quit();
    quit();
        
def game_start():
    start=0;
    selection=0;
    help_screen=0;
    while not start:
        while help_screen:
            gameSurface.fill(BLACK);
            draw_text("How To Play!",WHITE,"large",-208);
            draw_instruction("-Use the Arrow Keys to move your snake.",WHITE,"small",32,176);
            draw_instruction("-Eat apples to score.",WHITE,"small",32,224);
            draw_instruction("-Do not hit the sides of the screen.",WHITE,"small",32,282);
            draw_instruction("-Do not eat yourself!",WHITE,"small",32,336);

            gameSurface.blit(button_hover,(320,452));
            draw_button_text("Back",WHITE,"medium",400,502);

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit_game();
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        quit_game();
                    if event.key==pygame.K_SPACE:
                        help_screen=0;
            
            pygame.display.update();
            
            clock.tick(15);
            
        gameSurface.blit(title_backdrop,(0,0));
        #Draw buttons
        if selection==0:
            gameSurface.blit(button_hover,(48,436));
            gameSurface.blit(button,(320,436));
            gameSurface.blit(button,(592,436));
        elif selection==1:
            gameSurface.blit(button,(48,436));
            gameSurface.blit(button_hover,(320,436));
            gameSurface.blit(button,(592,436));            
        elif selection==2:
            gameSurface.blit(button,(48,436));
            gameSurface.blit(button,(320,436));
            gameSurface.blit(button_hover,(592,436));
            
        draw_button_text("Play",WHITE,"medium",128,486);
        draw_button_text("Help",WHITE,"medium",400,486);        
        draw_button_text("Quit",WHITE,"medium",672,486);
        '''draw_text("Jack's Snake Game",BLACK,"large",-30);
        draw_text("Use the Arrow Keys to Move",BLACK,"small",60);
        draw_text("Hit the Grey Squares for Points",BLACK,"small",100);
        draw_text("Don't Hit Yourself or the Sides of the Screen",BLACK,"small",140);
        draw_text("Press SPACE to Start!!! :D",BLACK,"small",250);'''
        pygame.display.update();

        #Starting the Game
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit_game();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game();
                elif event.key == pygame.K_SPACE:
                    if selection==0:
                        start=1;
                    elif selection==1:
                        help_screen=1;
                    elif selection==2:
                        quit_game();
                elif event.key == pygame.K_LEFT and selection>0:
                    selection-=1;
                elif event.key == pygame.K_RIGHT and selection<2:
                    selection+=1;
        clock.tick(30);
    
def game_loop():
    spdUp=0;
    fps=10;
    head_x=WIDTH/2;
    head_y=HEIGHT/2;
    head_x_change=BLOCK_SIZE;
    head_y_change=0;
    direction="RIGHT";
    snakeList=[];
    snakeLength=1;
    running=True;
    dead=False;

    #Spawn First Apple
    appleX,appleY=set_apple();

    #The Loop
    while running:
        #Dead
        while dead:
            gameSurface.fill(BLACK);
            draw_text("Game Over!!!",RED,"large",-30);
            draw_text("Press SPACE to Retry",WHITE,"small",90);
            draw_text("Press ESCAPE or Click X to Quit",WHITE,"small",130);
            pygame.display.update();

            #Quitting or Retrying
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    dead=False;
                    running=False;
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        dead=False;
                        running=False;
                    #Retrying
                    if event.key==pygame.K_SPACE:
                        dead=False;
                        fps=10;
                        head_x=WIDTH/2;
                        head_y=HEIGHT/2;
                        head_x_change=BLOCK_SIZE;
                        head_y_change=0;
                        direction="RIGHT";
                        snakeList=[];
                        snakeLength=1;
                        appleX,appleY=set_apple();
                        spdUp=0;

            clock.tick(5);

        #Pressing the cross button
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False;
            if event.type==pygame.KEYDOWN:
                #Quitting by pressing escape
                if event.key==pygame.K_ESCAPE:
                    running=False;
                    
                #Moving
                if event.key==pygame.K_LEFT and head_x_change!=BLOCK_SIZE:
                    head_x_change=-BLOCK_SIZE;
                    head_y_change=0;
                    direction="LEFT";
                if event.key==pygame.K_RIGHT and head_x_change!=-BLOCK_SIZE:
                    head_x_change=BLOCK_SIZE;
                    head_y_change=0;
                    direction="RIGHT";
                if event.key==pygame.K_UP and head_y_change!=BLOCK_SIZE:
                    head_x_change=0;
                    head_y_change=-BLOCK_SIZE;
                    direction="UP";
                if event.key==pygame.K_DOWN and head_y_change!=-BLOCK_SIZE:
                    head_x_change=0;
                    head_y_change=BLOCK_SIZE;
                    direction="DOWN";

        #Apply Movement
        head_x+=head_x_change;
        head_y+=head_y_change;

        #Update Section
        gameSurface.fill(LG);

        #Build the Snake
        snakeHead=[];
        snakeHead.append(head_x);
        snakeHead.append(head_y);
        snakeList.append(snakeHead);
        #Reduce snake if overgrowth
        if len(snakeList)>snakeLength:
            del snakeList[0];

        #Draw Player
        snake(BLOCK_SIZE,snakeList,direction);

        #Dying
        if(head_x<0 or head_x>=WIDTH or head_y<0 or head_y>=HEIGHT):
            dead=True;
        #Eating self
        for segment in snakeList[:-1]:
            if(segment == snakeHead):
                dead=True;

        #Draw Apple
        if(head_x!=appleX or head_y!=appleY):
            gameSurface.blit(apple_img,(appleX,appleY));
        else:
            gameSurface.blit(apple_eaten_img,(appleX,appleY));
            
        #Apple Collision
        if(head_x==appleX and head_y==appleY):
            appleX, appleY = set_apple();
            snakeLength+=1;
            if((snakeLength-1)%5==0 and fps<60):
                fps+=2;
                spdUp=15;

        #Speed Up Indicator
        if(spdUp>0):
            draw_text("Speed Increased!",BLACK,"small",-260);
            spdUp-=1;

        #Draw Score
        score(str(snakeLength-1),BLACK,"small");
        
        #Update Display
        pygame.display.update();

        #Tick Clock
        clock.tick(fps);
        
    #End Game
    quit_game();

#Main Code
game_start();
game_loop();

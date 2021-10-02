import pygame,random,time

def click():
    if (X>=tile1x and X<=tile1x+100) and (Y>=tile1y and Y<=tile1y+162):
        return 1
    if (X>=tile2x and X<=tile2x+100) and (Y>=tile2y and Y<=tile2y+162):
        return 2
    if (X>=tile3x and X<=tile3x+100) and (Y>=tile3y and Y<=tile3y+162):
        return 3
    if (X>=tile4x and X<=tile4x+100) and (Y>=tile4y and Y<=tile4y+162):
        return 4
    if (X>=tile5x and X<=tile5x+100) and (Y>=tile5y and Y<=tile5y+162):
        return 5
    return False

def Main():
    pygame.init()
    pygame.font.init()

    displaysurface=pygame.display.set_mode((400,648))
    pygame.display.set_caption("Piano Tiles")
    clock=pygame.time.Clock()

    BLACK=(0,0,0)
    WHITE=(255,255,255)
    GREY=(128,128,128)
    DARK_ORANGE=(255,159,0)
    CRIMSON=(220,20,60)
    KHAKI=(240,230,140)
    RED=(255,125,125)
    DARK_ORCHID=(104,34,139)
    COLOR1=0
    COLOR2=0
    COLOR3=0
    COLOR4=0
    COLOR5=0

    notes = ()
    for sounds in range(1,13):
        notes += ("assets/sounds/" + str(sounds)+".wav" , )

    global tile1x,tile1y,tile2x,tile2y,tile3x,tile3y,tile4x,tile4y,tile5x,tile5y,X,Y
    
    tile1x,tile1y=random.randint(0,3)*100,-162
    tile2x,tile2y=random.randint(0,3)*100,-162
    tile3x,tile3y=random.randint(0,3)*100,-162
    tile4x,tile4y=random.randint(0,3)*100,-162
    tile5x,tile5y=random.randint(0,3)*100,-162
    
    X,Y=0,0
    loops=0
    score=0
    tap=True
    firsttime=True
    exit_it=False
    restart=False
    Lasttap=''

    note=pygame.image.load("assets/images/notes.png")
    boo=pygame.image.load("assets/images/thumbs.png")
    piano=pygame.image.load("assets/images/piano.png")
    face=pygame.font.SysFont('stencil',45)
    face2=pygame.font.SysFont('lucidasans',38)
    face3=pygame.font.SysFont('georgia',28)
    face4=pygame.font.SysFont('lucidasans',28)
    text1=face.render("PIANO TILES",1,DARK_ORANGE)
    text2=face2.render("Tap to begin!",1,KHAKI)
    textLOST=face.render("YOU LOST.",1,WHITE)
    textTILE=face4.render('You tapped the WHITE TILE!',1,WHITE)
    textMISSED=face4.render('You missed the BLACK TILE!',1,WHITE)

    while True:
        textSCORE=face3.render(str(score),1,RED)
        textREALSCORE=face4.render('Your Score is '+str(score)+'.',1,WHITE)
        
        displaysurface.fill(WHITE)
        
        if not(tap):
            loops+=1

        for event in pygame.event.get():
            if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                exit_it=True
            else:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    X,Y=event.pos
                    if tap:
                        tap=False
                    elif click()==1:
                        COLOR1=GREY
                        if Lasttap!='tile1':
                            score+=1
                            sound = pygame.mixer.Sound(random.choice(notes))
                            sound.play()
                        Lasttap='tile1'
                    elif click()==2:
                        COLOR2=GREY
                        if Lasttap!='tile2':
                            score+=1
                            sound = pygame.mixer.Sound(random.choice(notes))
                            sound.play()
                        Lasttap='tile2'
                    elif click()==3:
                        COLOR3=GREY
                        if Lasttap!='tile3':
                            score+=1
                            sound = pygame.mixer.Sound(random.choice(notes))
                            sound.play()
                        Lasttap='tile3'
                    elif click()==4:
                        COLOR4=GREY
                        if Lasttap!='tile4':
                            score+=1
                            sound = pygame.mixer.Sound(random.choice(notes))
                            sound.play()
                        Lasttap='tile4'
                    elif click()==5:
                        COLOR5=GREY
                        if Lasttap!='tile5':
                            score+=1
                            sound = pygame.mixer.Sound(random.choice(notes))
                            sound.play()
                        Lasttap='tile5'
                    else:
                        displaysurface.fill(DARK_ORCHID)

                        posLOST=textLOST.get_rect()
                        posLOST.center=(200,400)

                        posTILE=textTILE.get_rect()
                        posTILE.center=(200,480)
                        posREALSCORE=textREALSCORE.get_rect()
                        posREALSCORE.center=(200,540)

                        displaysurface.blit(textLOST,posLOST)
                        displaysurface.blit(textTILE,posTILE)
                        displaysurface.blit(textREALSCORE,posREALSCORE)
                        displaysurface.blit(boo,(150,250))

                        pygame.display.update()
                        time.sleep(2)
                        
                        tap=True
                        firsttime=True
                        loops=0
                        score=0
                        
                        tile1x,tile1y=random.randint(0,3)*100,-162
                        tile2x,tile2y=random.randint(0,3)*100,-162
                        tile3x,tile3y=random.randint(0,3)*100,-162
                        tile4x,tile4y=random.randint(0,3)*100,-162
                        tile5x,tile5y=random.randint(0,3)*100,-162
                        COLOR1=BLACK
                        COLOR2=BLACK
                        COLOR3=BLACK
                        COLOR4=BLACK
                        COLOR5=BLACK
                        
        if exit_it:
            break

        if tap:
            displaysurface.fill(CRIMSON)
                        
            postext1=text1.get_rect()
            postext1.center=(200,350)

            postext2=text2.get_rect()
            postext2.center=(200,500)
            
            displaysurface.blit(text1,postext1)
            displaysurface.blit(text2,postext2)
            displaysurface.blit(piano,(125,65))
            displaysurface.blit(note,(10,10))
            displaysurface.blit(note,(340,568))

        if not(tap):
            pygame.draw.line(displaysurface,BLACK,(100,0),(100,648),1)
            pygame.draw.line(displaysurface,BLACK,(200,0),(200,648),1)
            pygame.draw.line(displaysurface,BLACK,(300,0),(300,648),1)

        if loops>=250 or not(firsttime):
            pygame.draw.rect(displaysurface,COLOR1,(tile1x,tile1y,100,162))
            tile1y+=1
        if tile1y>=0 or not(firsttime):
            pygame.draw.rect(displaysurface,COLOR2,(tile2x,tile2y,100,162))
            tile2y+=1
        if tile2y>=0  or not(firsttime):
            pygame.draw.rect(displaysurface,COLOR3,(tile3x,tile3y,100,162))
            tile3y+=1
        if tile3y>=0 or not(firsttime):
            pygame.draw.rect(displaysurface,COLOR4,(tile4x,tile4y,100,162))
            tile4y+=1
        if tile4y>=0 or not(firsttime):
            pygame.draw.rect(displaysurface,COLOR5,(tile5x,tile5y,100,162))
            tile5y+=1
            firsttime=False                  
        
        if tile1y==648:
            if COLOR1==GREY:
                tile1x,tile1y=random.randint(0,3)*100,-158
                COLOR1=BLACK
            else:
                tap=True
                restart=True
                loops=0
        if tile2y==648:
            if COLOR2==GREY:
                tile2x,tile2y=random.randint(0,3)*100,-158
                COLOR2=BLACK
            else:
                tap=True
                restart=True
                loops=0
        if tile3y==648:
            if COLOR3==GREY:
                tile3x,tile3y=random.randint(0,3)*100,-158
                COLOR3=BLACK
            else:
                tap=True
                restart=True
                loops=0
        if tile4y==648:
            if COLOR4==GREY:
                tile4x,tile4y=random.randint(0,3)*100,-158
                COLOR4=BLACK
            else:
                tap=True
                restart=True
                loops=0
        if tile5y==648:
            if COLOR5==GREY:
                tile5x,tile5y=random.randint(0,3)*100,-158
                COLOR5=BLACK
            else:
                tap=True
                restart=True
                loops=0

        if restart:
            displaysurface.fill(DARK_ORCHID)

            posLOST=textLOST.get_rect()
            posLOST.center=(200,400)
            posMISSED=textMISSED.get_rect()
            posMISSED.center=(200,480)
            posREALSCORE=textREALSCORE.get_rect()
            posREALSCORE.center=(200,540)
            

            displaysurface.blit(textLOST,posLOST)
            displaysurface.blit(textMISSED,posMISSED)
            displaysurface.blit(textREALSCORE,posREALSCORE)
            displaysurface.blit(boo,(150,250))

            pygame.display.update()
            time.sleep(2)
                        
            tap=True
            firsttime=True
            loops=0
            score=0
                       
            tile1x,tile1y=random.randint(0,3)*100,-162
            tile2x,tile2y=random.randint(0,3)*100,-162
            tile3x,tile3y=random.randint(0,3)*100,-162
            tile4x,tile4y=random.randint(0,3)*100,-162
            tile5x,tile5y=random.randint(0,3)*100,-162
            COLOR1=BLACK
            COLOR2=BLACK
            COLOR3=BLACK
            COLOR4=BLACK
            COLOR5=BLACK

            restart=False

        if not(tap):
            posSCORE=textSCORE.get_rect()
            posSCORE.center=(200,20)
            displaysurface.blit(textSCORE,posSCORE)
            clock.tick(500)
            
        pygame.display.update()
Main()

# thu vien game
import pygame, sys, threading

from button import Button

from pyvidplayer import Video




pygame.init()
# tieu de va icon
pygame.display.set_caption("CARO SQR")
icon = pygame.image.load(r'assets/eww.jpg')
pygame.display.set_icon(icon)

# cua so game
screen = pygame.display.set_mode((1280,720))
#bg
bg=pygame.image.load(r'assets/mainmenu.png')
bg=pygame.transform.scale(bg,(1280,720))
gamebg=pygame.image.load(r'assets/gamebg.jpg')
gamebg=pygame.transform.scale(gamebg,(1280,720))
pt=pygame.image.load(r'assets/1151373.png')
pt=pygame.transform.scale(pt,(1280,720))

# fps
clock = pygame.time.Clock()
#music 
nhac = pygame.mixer.Sound(r'music/game.wav')
time_skip= 603




# Loading BG
LOADING_BG = pygame.image.load("assets/Loading Bar Background.png")
#LOADING_BG=pygame.transform.scale(LOADING_BG,(771,100))
LOADING_BG_RECT = LOADING_BG.get_rect(center=(640, 360))
# Loading Bar and variables
loading_bar = pygame.image.load("assets/Loading Bar.png")
#loading_bar=pygame.transform.scale(loading_bar,(5,40))
loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8
# Work
WORK = 10000000

ok_play = True
ok_about = True
ok_setting =True

def intro():
    global time_skip
    vid = Video("music/intro vcl wtf.mp4")
    vid.set_size((1280,720))
    while True:
        vid.draw(screen, (0,0))
        SKIP_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(70, 40), 
                            text_input="SKIP", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(SKIP_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(SKIP_MOUSE_POS):
                    vid.close()
                    nhac.play(loops = -1)
                    main()    
        time_skip -= 1
        if time_skip <=0:
            
            vid.close()
            nhac.play(loops = -1)
            main() 
        
        pygame.display.update()
        clock.tick(60)

def doWork():
	# Do some math WORK amount times
	global loading_finished, loading_progress

	for i in range(WORK):
		math_equation = 523687 / 789456 * 89456
		loading_progress = i 
	loading_finished = True
# Finished text
FONT = pygame.font.SysFont("Roboto", 100)
finished = FONT.render("Done!", True, "white")
finished_rect = finished.get_rect(center=(640, 360))

ham =0


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/NeonTubes2.otf", size)
# Thread
#threading.Thread(target=doWork).start()

def ld():
    global ham
    global loading_finished
    threading.Thread(target=doWork).start()
    while True:
        global loading_bar
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill("#0d0e2e")
        if not loading_finished:
            loading_bar_width = loading_progress / WORK * 720
            loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
            loading_bar_rect = loading_bar.get_rect(midleft=(280, 360))
            screen.blit(LOADING_BG, LOADING_BG_RECT)
            screen.blit(loading_bar, loading_bar_rect)
        else:
            if(ham == 1):
                play()
            else:
                if ham == 2:
                    about()
                elif ham==3:
                    setting()     
        pygame.display.update()
        clock.tick(60)

        

        
        

def play():
    
    global ok_play
    global loading_finished
    while True:
        if ok_play:
            ok_play=False
            ld()
        else:
            screen.blit(bg, (0, 0))

            CHOSE_MOUSE_POS = pygame.mouse.get_pos()
            NORMAL_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                                text_input="VS AI", font=get_font(30), base_color="#d7fcd4", hovering_color="red")
            SUPPER_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 420), 
                                text_input="PVP", font=get_font(30), base_color="#d7fcd4", hovering_color="red")
            PLAY_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="blue", hovering_color="Green")

            for button in [NORMAL_BUTTON, SUPPER_BUTTON ,PLAY_BACK]:
                button.changeColor(CHOSE_MOUSE_POS)
                button.update(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(CHOSE_MOUSE_POS):
                        ok_play =True
                        loading_finished = False
                        main()

        pygame.display.update()

def about():
    global ok_about
    global loading_finished
    while True:
        if ok_about:
            ok_about = False
            ld()
        else:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            screen.blit(pt, (0, 0))

            PLAY_TEXT = get_font(20).render("y", True, "red")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            screen.blit(PLAY_TEXT, PLAY_RECT)
            PLAY_BACK = Button(image=None, pos=(110, 40), 
                                text_input="BACK", font=get_font(30), base_color="blue", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        ok_about =True
                        loading_finished = False
                        main()

        pygame.display.update()



def setting():
    global ok_setting
    global loading_finished
    while True:
        if ok_setting:
            ok_setting = False
            ld()
        else:
            screen.blit(pt, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()


            SETTING_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="blue", hovering_color="Green")

            SETTING_BACK.changeColor(PLAY_MOUSE_POS)
            SETTING_BACK.update(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if SETTING_BACK.checkForInput(PLAY_MOUSE_POS):
                            ok_setting =True
                            loading_finished = False
                            main()
        
        pygame.display.update()


    

#vong lap xu ly game
def main():
    #nhac.play(loops = -1) 
    
    run = True
    global ham
    while run:
        
        screen.blit(bg, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        
        
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                            text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="red")
        ABOUT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 420), 
                            text_input="ABOUT", font=get_font(30), base_color="#d7fcd4", hovering_color="red")
        SETTING_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 490), 
                            text_input="SETTING", font=get_font(30), base_color="#d7fcd4", hovering_color="red")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 560), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="red")

        for button in [PLAY_BUTTON, ABOUT_BUTTON,SETTING_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False 
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ham=1
                    play()
                if ABOUT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ham=2
                    about()    
                if SETTING_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ham=3
                    setting()          
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
        pygame.display.update()
        clock.tick(120)
    pygame.quit()
    exit()


intro()
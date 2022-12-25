# thu vien game
import pygame, sys, threading
import pygame_gui
from button import Button
#from pyvidplayer import Video





pygame.init()
# tieu de va icon
pygame.display.set_caption("CARO SQR")
icon = pygame.image.load(r'assets/eww.jpg')
pygame.display.set_icon(icon)

# cua so game
screen = pygame.display.set_mode((1280,720))
WIDTH, HEIGHT = 1280, 720
#bg
bg=pygame.image.load(r'assets/mainmenu.png')
bg=pygame.transform.scale(bg,(1280,720))
banco=pygame.image.load(r'assets/tempboard.png')
#banco=pygame.transform.scale(banco,(1280,720))
cox=pygame.image.load(r'assets/x.png')
coo=pygame.image.load(r'assets/o.png')
nenbanco=pygame.image.load(r'assets/background.png')
nenbanco=pygame.transform.scale(nenbanco,(1280,720))
gamebg=pygame.image.load(r'assets/gamebg.jpg')
gamebg=pygame.transform.scale(gamebg,(1280,720))
pt=pygame.image.load(r'assets/1151373.png')
pt=pygame.transform.scale(pt,(1280,720))

# fps
clock = pygame.time.Clock()
#music 
nhac = pygame.mixer.Sound('music/dtnd.wav')
time_skip= 603

#text input

manager1 = pygame_gui.UIManager((1280, 720))
manager2 = pygame_gui.UIManager((1280, 720))
name_1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((500, 400), (300, 50)), manager=manager1,
                                               object_id='#main_text_entry')

name_2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((500, 400), (300, 50)), manager=manager2,
                                               object_id='#main_text_entry')



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
wide = 54

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
        clock.tick(120)

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
board = [[0,0,0,0,0,0,0,0,0,0,0], 
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0]]

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
        clock.tick(120)



def AI():
    while True:
        screen.blit(bg, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="blue", hovering_color="Green")
        comingsoon = Button(image=None, pos=(640, 400), 
                                    text_input="COMING SOON", font=get_font(100), base_color="red", hovering_color="Green")
                                     
        for button in [comingsoon,  PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):                        
                        play()
        pygame.display.update()

        
        

def play():
    
    global ok_play
    global loading_finished
    while True:
        if ok_play:
            ok_play=False
            ld()
        else:
            screen.blit(bg, (0, 0))

            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            AI_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                                text_input="VS AI", font=get_font(30), base_color="#d7fcd4", hovering_color="red")
            PVP_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 420), 
                                text_input="PVP", font=get_font(30), base_color="#d7fcd4", hovering_color="red")
            PLAY_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="blue", hovering_color="Green")

            for button in [AI_BUTTON, PVP_BUTTON ,PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        ok_play =True
                        loading_finished = False
                        main()
                    if PVP_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        get_user_name1()
                    if AI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                        AI()

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

def checkxy(x,y,z):
    l=370 #goc.x
    r=100 #goc.y
    
    for i in range(10):
        for j in range(10):
            if x > (i*wide + l) and x < ( ( i +1) * wide + l)  and  y > (j*wide + r)  and y <(j*wide + wide + r) and board[i+1][j+1]==0:
                board[i+1][j+1]=z+1
                return True
    return False

def inxo():
    for i in range(10):
        for j in range(10):
            if board[i+1][j+1] == 1:
                screen.blit(cox,(370+i*wide+5, 5+100+j*wide))
            if board[i+1][j+1] == 2:
                screen.blit(coo,(370+i*wide+5, 5+ 100+j*wide))
            
                



turn =0

def show_user_name(user_name1, user_name2 ):
    global turn
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_pos = pygame.mouse.get_pos()
                x=current_pos[0]
                y=current_pos[1]
                if x > 370 and x < (370+540)   and y > 100 and y <640 :
                    
                    if checkxy(x,y, turn%2) == True:
                        
                        turn +=1
                    
            
                
                
            pygame.display.update()
            
        screen.blit(nenbanco, (0, 0)) 
        screen.blit(banco, (370, 100))  
        inxo()   
         
                
        if turn%2==1:
            uu= "assets/Play Rect.png"
            vv="assets/Play Rect - Copy.png"
            turnx="O TURN"

            u ="#d7fcd4"
            v="green"
        else:
            vv= "assets/Play Rect.png"
            uu="assets/Play Rect - Copy.png"
            v ="#d7fcd4"
            u="green"
            turnx="X TURN"
        X_BUTTON = Button(image=pygame.image.load(uu), pos=(100,100), 
                            text_input=user_name1, font=get_font(30), base_color=u, hovering_color=v)
        O_BUTTON = Button(image=pygame.image.load(vv), pos=(1060, 100), 
                            text_input=user_name2, font=get_font(30), base_color=v, hovering_color=v)
        turn_BUTTON = Button(image=pygame.image.load("assets/Play Rect - Copy.png"), pos=(640,80), 
                            text_input=turnx, font=get_font(30), base_color=u, hovering_color=v)
        for button in [X_BUTTON, O_BUTTON, turn_BUTTON]:
            #button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        #new_text = pygame.font.SysFont("dasd", 50).render(f"Hello, {user_name1} , {user_name2}", True, "black")
        #new_text_rect = new_text.get_rect(center=(WIDTH/2, HEIGHT/2))
        #screen.blit(new_text, new_text_rect)

        clock.tick(60)

        pygame.display.update()


def get_user_name1():
    global namethangdautien

    ok=0
    while True:
        screen.blit(bg, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="blue", hovering_color="Green")                              
        for button in [ PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)

        

        
        UI_REFRESH_RATE = clock.tick(60)/1000
        name1_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                            text_input="name thang dau tien", font=get_font(30), base_color="#d7fcd4", hovering_color="red")
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):                        
                        play()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                get_user_name2(event.text)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
                                               
            manager1.process_events(event)        
        manager1.update(UI_REFRESH_RATE)      
        name1_BUTTON.update(screen)       
        manager1.draw_ui(screen)
        pygame.display.update()
 


def get_user_name2(namethangdautien):
    global namthangthuhai
    while True:
        screen.blit(bg, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(110, 40), 
                                    text_input="BACK", font=get_font(30), base_color="blue", hovering_color="Green")                              
        for button in [ PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(screen)

        UI_REFRESH_RATE = clock.tick(60)/1000
        name2_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 350), 
                            text_input="name thang thu hai", font=get_font(30), base_color="#d7fcd4", hovering_color="red")
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):                        
                        get_user_name1()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                    namethangthuhai = event.text
                    show_user_name(namethangdautien,event.text)     
       
            
            manager2.process_events(event)
        
        
        manager2.update(UI_REFRESH_RATE)
        name2_BUTTON.update(screen)      
        manager2.draw_ui(screen)
        pygame.display.update()
 

 
#nhac.play(loops = -1)
#vong lap xu ly game

def main(): 
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
   
main()

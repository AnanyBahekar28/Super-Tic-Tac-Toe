import pygame, sys
from pygame import mixer

# from time import sleep

pygame.init()
# clock = pygame.time.Clock()


textFont = pygame.font.SysFont("pokemonuraniumkr", 40)
title = pygame.image.load("images/title.png")
mixer.music.load('music/EnglishCountryGardenAaronKenny.mp3')
mixer.music.set_volume(0.5)

green = (0,255,0)
light_green = (127,255,127)
dark_green = (50,150,50)
red = (255,0,0)
light_red = (255,127,127)
dark_red = (150,50,50)
blue = (0,0,255)
light_blue = (127,127,255)
dark_blue = (50,50,150)
black = (0,0,0)
grey = (128,128,128)

Width = 800
Height = 800

def UI(game = False):
    global Width, Height
    
    screen = pygame.display.set_mode((Width, Height))

    if not game:
        screen_template = pygame.image.load("images/grid_transparent.png")
        screen.blit(title, (45,80))
    elif game:
        screen_template = pygame.image.load("images/grid.png")
    
    icon = pygame.image.load("images/icon.png")
    
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Super Tic-Tac-Toe")
    
    
    screen.blit(screen_template, (0, 0))
    return screen

win = UI()






#%% Button Configuration

class button:
    def __init__(self, color, x, y, width, height, text = '', textColor = (0,0,0)):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textColor = textColor
        self._enable = False
        
    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('pokemonuraniumkr', 75)
            text = font.render(self.text, 1, self.textColor)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        self._enable = True
        
    def isOver(self, pos): #pos[0] = x, pos[1] = y
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if self._enable == True:
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
        return False
    
    def setEnable(self, status=False):
        self._enable = status
        return self._enable

    def getEnable(self):
        '''
        if self._enable:
            return True
        elif not self._enable:
            return False
        '''
        return (self._enable)

boxCoords = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]




#%% Board

"""
# board:
board = []
for i in range(9):
    board.append(["-","-","-","-","-","-","-","-","-"])

# megaBoard:
megaBoard = []
for in range(3):
    megaBoard.append(["-","-","-"])

"""

board = [
    ["-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-"]
]

megaBoard = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

Winner = "-"

#%% imposing rules of super tic tac toe
# Two ways:
# 1. Disable ineligible buttons (Is smarter)
# 2. Check if button is eligible or not and then accept or decline input (Could be easier and efficient)

def whatPos(i): # [box number, square in box]
    return [[(i%9)//3, (i//9)//3], [(i%9)%3, (i//9)%3]]


#%%--------------------------------------------------------------------- Check wins in boxes and overall board

def checkWin():
    global Winner, megaBoard, page
    box = megaBoard
    
    for player in ["X","O"]:
        for i in range(3):
            if all([box[i][j] == player for j in range(3)]) or all([box[j][i] == player for j in range(3)]):
                if page == "GamePage":
                    pygame.time.delay(1000)
                    page = "GameWinPage"
                Winner = player

                # print(f"We have a Winner: {Winner}")
        if all([box[i][i] == player for i in range(3)]) or all([box[i][2 - i] == player for i in range(3)]):
            if page == "GamePage":
                pygame.time.delay(1000)
                page = "GameWinPage"
            Winner = player
            
            # print(f"We have a Winner: {Winner}")

def checkBox():
    global board, megaBoard
    box = [[],[],[]]
    for x in boxCoords:
        for i in range(81):
            if whatPos(i)[0] == x:
                box[whatPos(i)[1][1]].append(board[i%9][i//9])

        for player in ["X","O"]:
            for i in range(3):
                if all([box[i][j] == player for j in range(3)]) or all([box[j][i] == player for j in range(3)]):
                    megaBoard[x[0]][x[1]] = player
                    #print(megaBoard)
            if all([box[i][i] == player for i in range(3)]) or all([box[i][2 - i] == player for i in range(3)]):
                megaBoard[x[0]][x[1]] = player
                #print(megaBoard)
        
        box = [[],[],[]]

    
    




#%%----------------------------------------------------------------------------- X and O drawing
'''
def drawX(button, color):
    pygame.draw.line(win, color = color, start_pos = (button.x, button.y), end_pos = (button.x+button.width, button.y+button.height))
    pygame.draw.line(win, color = color, start_pos = (button.x+button.width, button.y), end_pos = (button.x, button.y+button.height))

    disableButtons([button])
'''

def drawX(x,y,color):
    pygame.draw.line(win, color = color, start_pos = ((Width/18)*(2*x+1)-40 , (Height/18)*(2*y+1)-40), end_pos = ((Width/18)*(2*x+1)-40+80 , (Height/18)*(2*y+1)-40+80), width=7)
    pygame.draw.line(win, color = color, start_pos = ((Width/18)*(2*x+1)-40+80 , (Height/18)*(2*y+1)-40), end_pos = ((Width/18)*(2*x+1)-40 , (Height/18)*(2*y+1)-40+80), width=7)

def drawO(x,y,color):
    pygame.draw.circle(win, color = color, center = ((Width/18)*(2*x+1)-40+40 , (Height/18)*(2*y+1)-40+40), radius = 40, width = 7)


def drawBigX(x,y,color):
    pygame.draw.line(win, color = color, start_pos = ((Width/18)*(6*x+1)-40 , (Height/18)*(6*y+1)-40), end_pos = ((Width/18)*(6*x+1)-40+240 , (Height/18)*(6*y+1)-40+240), width=7)
    pygame.draw.line(win, color = color, start_pos = ((Width/18)*(6*x+1)-40+240 , (Height/18)*(6*y+1)-40), end_pos = ((Width/18)*(6*x+1)-40 , (Height/18)*(6*y+1)-40+240), width=7)

def drawBigO(x,y,color):
    pygame.draw.circle(win, color = color, center = ((Width/18)*(6*x+3)-40+40 , (Height/18)*(6*y+3)-40+40), radius = 120, width = 7)






#%%------------------------------------------ Pages Configuration

pages = [["StartPage"],
         ["PlayPage"],
         ["GamePage", "GameWinPage"]]

page = pages[0][0]
oldPage = ""
current_index = 0



#%% Button Creation # (color, x, y, width, height, text)

# common button for every page(except main menu)
BackButton = button(red, 5, 10, 150, 75, text = "Back")

# Main menu buttons
PlayButton = button(green, 250, 300, 300, 75, text = 'Play')

# Play buttons
PlayOfflineButton = button(green, 212.5, 250, 375, 75, text = 'Singleplayer')
PlayOnlineButton = button(green, 212.5, 450, 375, 75, text = 'Multiplayer')

# Tic Tac Toe
gamePage = []

for i in range(81):
    butt = button(black, (Width/18)*(2*(i%9)+1)-40 , (Height/18)*(2*(i//9)+1)-40 ,80,80, text = "")
    gamePage.append(butt)

ContinueButton = button(grey, 212.5, 250, 375, 75, text = 'Continue')
QuitButton = button(grey, 212.5, 450, 375, 75, text = 'Quit')

PauseList = [ContinueButton, QuitButton]

XwinText = button(black, 212.5, 100, 375, 75, text = 'X Player Wins!!', textColor=blue)
OwinText = button(black, 212.5, 100, 375, 75, text = 'O Player Wins!!', textColor=red)



#%% Button Disabling

buttonsOnAPage = {"StartPage": [PlayButton],
                  "PlayPage": [PlayOfflineButton, PlayOnlineButton, BackButton],
                  "GamePage": gamePage}

def disableButtons(buttonsOnPage, status = False):
    for Butt in buttonsOnPage:
        if Butt is None:
            break
        else:
            Butt.setEnable(status)






#%%

def redrawWindow():
    global page, board
    
    if page == "StartPage":
        UI()
        PlayButton.draw(win, (0,0,0))
    elif page == "PlayPage":
        UI()
        PlayOfflineButton.draw(win, (0,0,0))
        PlayOnlineButton.draw(win, (0,0,0))
        BackButton.draw(win, (0,0,0))
    elif page == "GamePage":
        UI(game=True)
        for butt in gamePage:
            if butt.getEnable():
                butt.draw(win)
        
        for x in range(81):
            i = x%9
            j = x//9
            if board[i][j] == "X" and megaBoard[whatPos(x)[0][0]][whatPos(x)[0][1]] == "-":
                drawX(i,j,blue)
            elif board[i][j] == "O" and megaBoard[whatPos(x)[0][0]][whatPos(x)[0][1]] == "-":
                drawO(i,j,red)
            elif board[i][j] == "-":
                pass
        
        for x in range(9):
            i = x%3
            j = x//3
            if megaBoard[i][j] == "X":
                drawBigX(i,j,blue)
            elif megaBoard[i][j] == "O":
                drawBigO(i,j,red)
            elif megaBoard[i][j] == "-":
                pass
    
    elif page == "PausePage":
        UI(game=True)
        for butt in PauseList:
            butt.draw(win, (0,0,0))
    
    elif page == "GameWinPage":
        UI(game=True)
        QuitButton.draw(win, (0,0,0))
        if Winner == "X":
            XwinText.draw(win)
        elif Winner == "O":
            OwinText.draw(win)












#%% Game start

#mixer.music.play(loops = -1)
redrawWindow()
run = True
n=1
square = []

while run:
    redrawWindow()
    pygame.display.update()
    checkWin()
      

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        # print(pos)
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if PlayButton.isOver(pos):
                oldPage = page
                page = "PlayPage"
                disableButtons(buttonsOnAPage[oldPage])
                continue
                # print(page)
                # print(oldPage)
            elif BackButton.isOver(pos):
                oldPage = page
                if page in pages[1]:
                    page = "StartPage"
                    disableButtons(buttonsOnAPage[oldPage])
                continue

            elif PlayOfflineButton.isOver(pos):
                oldPage = page
                page = "GamePage"
                disableButtons(buttonsOnAPage[oldPage])
                disableButtons(gamePage, status=True)
                continue
            
            elif ContinueButton.isOver(pos):
                page = "GamePage"
                disableButtons(PauseList)
                continue
            
            elif QuitButton.isOver(pos):
                page = "PlayPage"
                # ---------------------------------------Reset Game-----------------------------------------
                disableButtons(gamePage)
                disableButtons(PauseList)
                board = []
                for i in range(9):
                    board.append(["-","-","-","-","-","-","-","-","-"])
                megaBoard = []
                for i in range(3):
                    megaBoard.append(["-","-","-"])
                square = []
                Winner = "-"
                n=1
                continue
            
            elif page == "GamePage":
                i = 0
                for button in gamePage:
                    if button.isOver(pos) and ((whatPos(i)[0] == square or square == []) or (megaBoard[square[0]][square[1]] != "-")) and page == "GamePage" and board[i%9][i//9] == "-" and megaBoard[whatPos(i)[0][0]][whatPos(i)[0][1]] == "-":
                        if n%2 == 1:
                            board[i%9][i//9] = "X"
                        elif n%2 == 0:
                            board[i%9][i//9] = "O"
                        n+=1
                        disableButtons([button])
                        square = whatPos(i)[1]
                        
                        
                        checkBox()
                        # print(whatPos(i))
                        # print(square)
                        continue
                    i += 1
        
        elif event.type == pygame.MOUSEMOTION:
            # green buttons
            if PlayButton.isOver(pos):
                PlayButton.color = dark_green
            else:
                PlayButton.color = green

            if PlayOfflineButton.isOver(pos):
                PlayOfflineButton.color = dark_green
            else:
                PlayOfflineButton.color = green
            
            if PlayOnlineButton.isOver(pos):
                PlayOnlineButton.color = dark_green
            else:
                PlayOnlineButton.color = green
            
            #red buttons
            if BackButton.isOver(pos):
                BackButton.color = dark_red
            else:
                BackButton.color = red
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and page == "GamePage":
                page = "PausePage"

"""
Ideas:
for multiplayer handing and giving them assigned symbols, give odd/even numbers to the players (according to what our code supports) and need to add another condition in player trying to make moves to check if it is our turn or not.
Check chatgpt for integrating online mode for the game


"""





























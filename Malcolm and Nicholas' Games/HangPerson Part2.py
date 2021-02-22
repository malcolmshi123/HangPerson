# Name: Malcolm
# Date: April 2, 2019
# Title: HangPerson
# Description:
# Create a hangman style game with three game modes:
# 1) Two-Player Game
# 2) One-Player - 3 categories with 10 phrases each
# 3) Computer Player - 3 levels of AI (Random, Common Letters, Common Words)

#
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

#
import random

#
import time

#
def showHelp():

    print('HELP')

#
def quitGame():

    window.destroy()
    
#
def checkLetter(letterIndex):

    #disable the selected button
    buttonList[letterIndex].config (state = tk.DISABLED)

    #determine the letter selected
    guessedLetter = chr(letterIndex+65)

    #store the Phrase in temporary variable
    tempPhrase = phrase.get()

    #convert hidden phrase into string to list since strings are immutable (i.e. they cannot change)
    #strings are immutable (i.e. they cannot change)
    hiddenList = list(hiddenPhrase.get())

    #Assume the guess is wrong untill it checks to see if they are right
    correct = False

    #check if guessed letter matches with each letter in the phrase
    index = 0

    for letter in tempPhrase:

        if guessedLetter == letter:
            correct = True
            hiddenList[index] = letter

        index += 1
    #if letter was in the phrase
    if correct:

        #convert list back into a string and set the label value
        hiddenPhrase.set(''.join(hiddenList))

        #if the phrase was found then stop the game with a win
        if hiddenPhrase.get() == phrase.get():
            stopGame('win')
    #otherwise reduce turns and show next part
    else:
        turnsLeft.set(turnsLeft.get()-1)
        showPicture()


        if turnsLeft.get()==0:
            stopGame('loss')

#
def showPicture():

    picPhotoImage = tk.PhotoImage(file = ('pic' + str(6 - turnsLeft.get())+'.gif'))
    picLabel = ttk.Label(gameFrame, image = picPhotoImage)
    picLabel.picPhotoImage = picPhotoImage
    picLabel.place(x=600, y=50, width = 300, height = 400)

def hidePhrase():

    hidden=''
    tempPhrase = phrase.get()
    for letter in tempPhrase:

        if letter in tempPhrase:

            if letter == ' ':
                hidden +=' '
            else:
                hidden += '?'

        hiddenPhrase.set(hidden)

#
def enableButtons():
    for index in range (26):
        buttonList[index].config(state = tk.NORMAL)

#
def disableButtons():

    for index in range (26):

        buttonList[index].config(state = tk.DISABLED)

    #Add the Guess button here

#
def startGame(gameType):

    turnsLeft.set(6)

    showPicture()

    if gameType == 'random':

        randomStart()
    else:
        category.set(simpledialog.askstring('Category', 'What is the category?', initialvalue = ''))
        phrase.set(simpledialog.askstring('Phrase', 'What is the phrase?', initialvalue = ''))

    hidePhrase()

    enableButtons()

#
def stopGame(gameResult):

    if gameResult == 'win':
        tk.messagebox.showwarning('Congratulations!', 'You have guessed the phrase!')
    else:
        tk.messagebox.showwarning('GAME OVER', 'YOU LOSE!')

    disableButtons()

#
def twoPlayerGame():

    startGame('regular')
#
def singlePlayerGame():

    startGame('random')
    
#
def randomStart():

    categoryNum = random.randint(1,10)

    if categoryNum >=1 and categoryNum <= 3:
        category.set('Movies')
        
    elif categoryNum >= 4 and categoryNum <= 6:
        category.set('Famous People')

    elif categoryNum >= 7 and categoryNum <=9:
        category.set('Video Games')

    elif categoryNum == 10:
        category.set('BOSS FIGHT')
        

    phraseNum = random.randint (1,10)
    
    if category.get()== 'Movies':
        if phraseNum == 1:
            phrase.set('STAR WARS')

        elif phraseNum == 2:
            phrase.set('THE HUNT FOR RED OCTOBER')

        elif phraseNum == 3:
            phrase.set('SAVING PRIVATE RYAN')

        elif phraseNum == 4:
            phrase.set('BLADES OF GLORY')

        elif phraseNum == 5:
            phrase.set('TOP GUN')

        elif phraseNum == 6:
            phrase.set('MISSION IMPOSSIBLE')

        elif phraseNum == 7:
            phrase.set('TORA TORA TORA')

        elif phraseNum == 8:
            phrase.set('BATTLE OF BRITAIN')

        elif phraseNum == 9:
            phrase.set('TALLADEGA NIGHTS')

        elif phraseNum ==  10:
            phrase.set('DUNKIRK')


            
    elif category.get()==('Famous People'):
        
        if phraseNum == 1:
            phrase.set('STEPHEN HAWKING')
            
        elif phraseNum == 2:
            phrase.set('THOMAS JEFFERSON')
        
        elif phraseNum == 3:
            phrase.set('ARNOLD SCHWARZNAGGER')
            
        elif phraseNum == 4:
            phrase.set('MIKE TYSON')
            
        elif phraseNum == 5:
            phrase.set('KATY PERRY')
            
        elif phraseNum == 6:
            phrase.set('FLOYD MAYWEATHER JR')
            
        elif phraseNum == 7:
            phrase.set('LEBRON JAMES')
            
        elif phraseNum == 8:
            phrase.set('BILL NYE')
            
        elif phraseNum == 9:
            phrase.set('BRUCE LEE')
            
        elif phraseNum == 10:
            phrase.set('LEONARDO DA VINCI')


    elif category.get()==('Video Games'):

        if phraseNum == 1:
            phrase.set('POKEMON')
            
        elif phraseNum == 2:
            phrase.set('CALL OF DUTY')
            
        elif phraseNum == 3:
            phrase.set('DOOM')
            
        elif phraseNum == 4:
            phrase.set('HALO')
            
        elif phraseNum == 5:
            phrase.set('THE LAST OF US')
            
        elif phraseNum == 6:
            phrase.set('MARIO CART')
            
        elif phraseNum == 7:
            phrase.set('BORDERLANDS')
            
        elif phraseNum == 8:
            phrase.set('DESTINY')
            
        elif phraseNum == 9:
            phrase.set('WAR THUNDER')
            
        elif phraseNum == 10:
            phrase.set('PLAYERUNKNOWNS BATTLEGROUND')



    elif category.get()==('VIDEO GAME BOSS FIGHT'):

        tk.messagebox.showwarning('WARNING, BOSS FIGHT ENGAGED!')

        if phraseNum == 1:
            phrase.set('DONKEY KONG')

        elif phraseNum == 2:
            phrase.set('MIKE TYSON')

        elif phraseNum == 3:
            phrase.set('ATHEON TIMES CONFLUX')

        elif phraseNum == 4:
            phrase.set('BOWSER')

        elif phraseNum == 5:
            phrase.set('CROTA SON OF ORYX')

        elif phraseNum == 6:
            phrase.set('ARES GOD OF WAR')

        elif phraseNum == 7:
            phrase.set('AMON')

        elif phraseNum == 8:
            phrase.set('STAIN HERO KILLER')

        elif phraseNum == 9:
            phrase.set('GANONDORF')

        elif phraseNum == 10:
            phrase.set('VIPER')




def aIGame(aILevel):
    startGame('regular')
    playAI(aILevel)

def playAI (aILevel):
    while turnsLeft.get()>0:
        if aILevel == 1:
            letterNum = levelOneAI()

        elif aILevel == 2:
            letterNum = levelTwoAI()

        elif aILevel == 3:
            letterNum = levelThreeAI()

        checkLetter(letterNum)

        window.update()
        window.after(1000)

def levelOneAI():
    while True:
        randomNum = random.randint(0,25)
        if buttonList[randomNum]['state'] == 'normal':
            break
    return randomNum



    
def guessPhrase():

    print('i guess')
def giveUp():

    stopGame()
#
def setupGameFrame():

    # Add an image to the frame
    showPicture()

    # Create the labels for the frame
    categoryTitleLabel = ttk.Label(gameFrame, text = 'Category:', anchor = 'w')
    categoryTitleLabel.place(x=100, y=200, width = 75, height = 25)

    categoryLabel = ttk.Label(gameFrame, textvariable = category, anchor = 'w')
    categoryLabel.place(x=175, y=200, width = 200, height = 25)

    phraseTitleLabel = ttk.Label(gameFrame, text = 'Phrase:', anchor = 'w')
    phraseTitleLabel.place(x=100, y=250, width = 75, height = 25)

    phraseLabel = ttk.Label(gameFrame, textvariable = hiddenPhrase, anchor = 'w')
    phraseLabel.place(x=175, y=250, width = 200, height = 25)

    turnTitleLabel = ttk.Label(gameFrame, text = 'Turns Left:', anchor = 'w')
    turnTitleLabel.place(x=100, y=300, width = 75, height = 25)

    turnLabel = ttk.Label(gameFrame, textvariable = turnsLeft, anchor = 'w')
    turnLabel.place(x=175, y=300, width = 200, height = 25)

    # Add the letter buttons
    xPosition = 100

    for index in range(26):

        currentButton = tk.Button(gameFrame, text = chr(index + 65), 
                                  state = tk.DISABLED, disabledforeground = 'red', 
                                  command = lambda letterIndex = index: checkLetter(letterIndex))

        buttonList.append(currentButton)

        buttonList[index].place(x = xPosition, y = 475, width = 25, height = 25)

        xPosition += 35

    # Create the button for the frame
    guessButton = tk.Button(gameFrame, text = 'Guess', command = guessPhrase)
    guessButton.place(x = 500, y = 525, width = 100, height = 50)

    giveButton = tk.Button(gameFrame, text = 'Give Up?', command = giveUp)
    giveButton.place(x = 500, y = 575, width = 100, height = 50)

### Main Program ###

# Create the window
window = tk.Tk()

# Setup the window
frameWidth = 1100
frameHeight = 600
window.minsize(frameWidth, frameHeight)
window.title('Malcolm and Nicholas\' HangPerson Game')

# Create the menubar
menubar = tk.Menu(window)

# Create pulldown menus
fileMenu = tk.Menu(menubar, tearoff=0)
fileMenu.add_command(label="One Player", command=singlePlayerGame)
fileMenu.add_command(label="AI Level 1", command=lambda aILevel = 1:aIGame(aILevel))
fileMenu.add_command(label="Two-Player Game", command=twoPlayerGame)
fileMenu.add_command(label="Exit", command=showHelp)

# Add menus to the menubar
menubar.add_cascade(label="Game Type", menu=fileMenu)
menubar.add_command(label="Help", command=showHelp)

# Disblay the menubar
window.config(menu=menubar)

# Global variables for Login Screen
category = tk.StringVar()
hiddenPhrase = tk.StringVar()
phrase = tk.StringVar()
turnsLeft = tk.IntVar()

# Create a style for the frames
pagestyle = ttk.Style()
pagestyle.configure('lightBlue.TFrame', background='light blue')

# Create the game frame and locate it in the top left corner of the window
gameFrame=ttk.Frame(window, width = frameWidth, height = frameHeight, style = 'lightBlue.TFrame')
gameFrame.place(x = 0, y = 0)

# Create a list to hold the leter buttons
buttonList = []

# Setup all the frames
setupGameFrame()

# Start the program
window.mainloop()

#
def levelTwoAI():

    while True:

        # https://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
        rangeNum = random.randint(1, 100)

        if rangeNum >= 1 and rangeNum <= 12:
            randomNum.ord('E')-56
        elif rangeNum >= 13 and rangeNum <= 21:
            randomNum.ord('T')-56
        elif rangeNum >= 22 and rangeNum <= 29:
            randomNum.ord('A')-56
        elif rangeNum >= 30 and rangeNum <= 36:
            randomNum.ord('O')-56
        elif rangeNum >= 37 and rangeNum <= 43:
            randomNum.ord('I')-56
        elif rangeNum >= 44 and rangeNum <= 50:
            randomNum.ord('N')-56
        elif rangeNum >= 51 and rangeNum <= 56:
            randomNum.ord('S')-56
        elif rangeNum >= 57 and rangeNum <= 62:
            randomNum.ord('R')-56
        elif rangeNum >= 63 and rangeNum <= 68:
            randomNum.ord('H')-56
        elif rangeNum >= 69 and rangeNum <= 72:
            randomNum.ord('D')-56
        elif rangeNum >= 73 and rangeNum <= 76:
            randomNum.ord('L')-56
        elif rangeNum >= 77 and rangeNum <= 79:
            randomNum.ord('U')-56
        elif rangeNum == 80 or rangeNum == 81:
            randomNum.ord('C')-56
        elif rangeNum == 82 or rangeNum == 83:
            randomNum.ord('M')-56
        elif rangeNum == 84 or rangeNum == 85:
            randomNum.ord('F')-56
        elif rangeNum == 86 or rangeNum == 87:
            randomNum.ord('Y')-56
        elif rangeNum == 88 or rangeNum == 89:
            randomNum.ord('W')-56
        elif rangeNum == 90 or rangeNum == 91:
            randomNum.ord('G')-56
        elif rangeNum == 92 or rangeNum == 93:
            randomNum.ord('P')-56
        elif rangeNum == 94:
            randomNum.ord('B')-56
        elif rangeNum == 95:
            randomNum.ord('V')-56
        elif rangeNum == 96:
            randomNum.ord('K')-56
        elif rangeNum == 97:
            randomNum.ord('X')-56
        elif rangeNum == 98:
            randomNum.ord('Q')-56
        elif rangeNum == 99:
            randomNum.ord('J')-56
        else:
            randomNum.ord('Z')-56

        if buttonList[randomNum]['state'] == 'normal':
            break

    return randomNum

#
def levelThreeAI():

    if hiddenPhrase.get().find('_HE') >= 0 and buttonList(ord('T')-65)['state'] == 'normal':
        return ord('T')-65
    elif hiddenPhrase.get().find('T_E') >= 0 and buttonList(ord('H')-65)['state'] == 'normal':
        return ord('H')-65
    elif hiddenPhrase.get().find('TH_') >= 0 and buttonList(ord('E')-65)['state'] == 'normal':
        return ord('E')-65
    elif hiddenPhrase.get().find('_ND') >= 0 and buttonList(ord('A')-65)['state'] == 'normal':
        return ord('A')-65
    elif hiddenPhrase.get().find('A_D') >= 0 and buttonList(ord('N')-65)['state'] == 'normal':
        return ord('N')-65
    elif hiddenPhrase.get().find('AN_') >= 0 and buttonList(ord('D')-65)['state'] == 'normal':
        return ord('D')-65
    elif hiddenPhrase.get().find('_NG') >= 0 and buttonList(ord('I')-65)['state'] == 'normal':
        return ord('I')-65
    elif hiddenPhrase.get().find('I_G') >= 0 and buttonList(ord('N')-65)['state'] == 'normal':
        return ord('N')-65
    elif hiddenPhrase.get().find('IN_') >= 0 and buttonList(ord('G')-65)['state'] == 'normal':
        return ord('G')-65
    elif hiddenPhrase.get().find('Q_') >= 0 and buttonList(ord('U')-65)['state'] == 'normal':
        return ord('U')-65
    else:
        return levelTwoAI()




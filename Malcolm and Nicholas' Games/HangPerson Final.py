# Names: Malcolm and Nicholas
# Date: April 20, 2018
# Course: ICS2O1
# Title: HangPerson
# Description:
# Create a hangman style game with three game modes:
# 1) Two-Player Game
# 2) One-Player - 3 categories with 10 phrases each
# 3) Computer Player - 3 levels of AI (Random, Common Letters, Common Words)
# Added features:
# 1. AI and other users can create and identify phrases with lowercase letters
# 2. Detailed help message box
# 3. Additional three letter groupings and words for level 3 AI
# 4. Guess button to instantly guess the phrase - wrong guess = 1 less turn
# 5. Give up button if user is struggling
# 6. Sound effects - ding for correct letter, errr for wrong letter
# 7. Music

# Tkinter for GUI
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

# Random number generator
import random

#
import time

# Music/Sound
import winsound

# Need help?
def showHelp():

    tk.messagebox.showinfo('Help', 'The AI mode lets you make a category and phrase and lets the AI guess what word it is. \n'
                           '\n The "Game Type" lets you choose from either two play modes where a friend may pick a category and phrase, and the single player modes let the computer pick you a phrase for you.')

# Quit the program
def quitGame():

    window.destroy()
    
# Checking the selected letter
def checkLetter(letterIndex):

    #disable the selected button
    buttonList[letterIndex].config(state = tk.DISABLED)

    #determine the letter selected
    guessedLetter = chr(letterIndex+65)
    guessedLowerLetter = chr(letterIndex+97)

    #store the Phrase in temporary variable
    tempPhrase = phrase.get()

    #convert hidden phrase into string to list since strings are immutable (i.e. they cannot change)
    hiddenList = list(hiddenPhrase.get())

    #Assume the guess is wrong until it checks to see if they are right
    correct = False

    #check if guessed letter matches with each letter in the phrase
    index = 0

    for letter in tempPhrase:

        if guessedLetter == letter or guessedLowerLetter == letter:
            correct = True
            hiddenList[index] = letter

        index += 1
        
    #if letter was in the phrase
    if correct:

        # Sound effect
        winsound.PlaySound('Ding - Sound Effects YouTube.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

        #convert list back into a string and set the label value
        hiddenPhrase.set(''.join(hiddenList))

        #if the phrase was found then stop the game with a win
        if hiddenPhrase.get() == phrase.get():
            stopGame('win')
            
    #otherwise reduce turns and show next part
    else:

        # Sound effect
        winsound.PlaySound('Wrong-answer-sound-effect.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

        turnsLeft.set(turnsLeft.get()-1)
        showPicture()

        if turnsLeft.get()==0:
            stopGame('loss')

# HangPerson body parts
def showPicture():

    picPhotoImage = tk.PhotoImage(file = ('pic' + str(6 - turnsLeft.get())+'.gif'))
    picLabel = ttk.Label(gameFrame, image = picPhotoImage)
    picLabel.picPhotoImage = picPhotoImage
    picLabel.place(x=600, y=50, width = 300, height = 400)

# Hide the phrase
def hidePhrase():

    hidden=''
    tempPhrase = phrase.get()

    
    for letter in tempPhrase:

        if letter in tempPhrase:

            if letter == ' ':
                hidden +=' '
            else:
                hidden += '.'

        hiddenPhrase.set(hidden)

# Allow the buttons to work
def enableButtons():

    # Enable letter buttons
    for index in range(26):
        buttonList[index].config(state = tk.NORMAL)

    # Enable guess and give up buttons
    for i in range(2):
        bigButtonList[i].config(state = tk.NORMAL)
    
        
# Do not allow the buttons to work
def disableButtons():

    # Disable letter buttons
    for index in range(26):
        buttonList[index].config(state = tk.DISABLED)

    # Disable guess and give up buttons
    for i in range(2):
        bigButtonList[i].config(state = tk.DISABLED)

# Start the game
def startGame(gameType):

    turnsLeft.set(6)

    showPicture()

    if gameType == 'random':
        randomStart()
        
    else:
        category.set(simpledialog.askstring('Category', 'What is the category?', initialvalue = ''))
        phrase.set(simpledialog.askstring('Phrase', 'What is the phrase?', initialvalue = ''))

        # error checking
        while True:
            if phrase == 'None':
                phrase.set(simpledialog.askstring('Phrase', 'Enter a new phrase', initialvalue = ''))
            else:
                break

    hidePhrase()

    enableButtons()

# End the game
def stopGame(gameResult):

    if gameResult == 'win':
        # Play music
        winsound.PlaySound('Congratulations.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
        tk.messagebox.showwarning('Congratulations!', 'You have guessed the phrase!')

        # Stop music after ok is clicked
        if True:

            winsound.PlaySound(None, 0)
        
    else:
        # Play effect
        winsound.PlaySound('Ha Got Em.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
        tk.messagebox.showwarning('Game Over!', 'You Lose!')

        # Stop sound after ok is clicked
        if True:

            winsound.PlaySound(None, 0)
        
    disableButtons()

# Start the two player game
def twoPlayerGame():

    startGame('regular')
    
# Start the one player game
def singlePlayerGame():

    startGame('random')
    
# Random categories and phrases for one player game
def randomStart():

    # pick category number
    categoryNum = random.randint(1,10)

    if categoryNum >=1 and categoryNum <= 3:
        category.set('Movies')
        
    elif categoryNum >= 4 and categoryNum <= 6:
        category.set('Famous People')

    elif categoryNum >= 7 and categoryNum <=9:
        category.set('Video Games')

    elif categoryNum == 10:
        category.set('VIDEO GAME BOSS FIGHT')
        
    # pick phrase from category number
    phraseNum = random.randint(1,10)
    
    if category.get()== 'Movies':
        if phraseNum == 1:
            phrase.set('STAR WARS')

        elif phraseNum == 2:
            phrase.set('BLACK PANTHER')

        elif phraseNum == 3:
            phrase.set('DESPICABLE ME')

        elif phraseNum == 4:
            phrase.set('THE INCREDIBLES')

        elif phraseNum == 5:
            phrase.set('TOP GUN')

        elif phraseNum == 6:
            phrase.set('MISSION IMPOSSIBLE')

        elif phraseNum == 7:
            phrase.set('INFINITY WAR')

        elif phraseNum == 8:
            phrase.set('FIFTY SHADES OF GREY')

        elif phraseNum == 9:
            phrase.set('DAWN OF THE PLANET OF THE APES')

        elif phraseNum ==  10:
            phrase.set('THE EXORCIST')


            
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
            phrase.set('BILL NYE THE SCIENCE GUY')
            
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
            phrase.set('FORTNITE')
            
        elif phraseNum == 4:
            phrase.set('HALO')
            
        elif phraseNum == 5:
            phrase.set('THE LAST OF US')
            
        elif phraseNum == 6:
            phrase.set('MARIO KART')
            
        elif phraseNum == 7:
            phrase.set('BORDERLANDS')
            
        elif phraseNum == 8:
            phrase.set('DESTINY')
            
        elif phraseNum == 9:
            phrase.set('FORZA')
            
        elif phraseNum == 10:
            phrase.set('PLAYERUNKNOWN BATTLEGROUNDs')



    elif category.get()==('VIDEO GAME BOSS FIGHT'):

        tk.messagebox.showwarning('WARNING', 'BOSS FIGHT ENGAGED!')

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

# Start the AI game
def aIGame(aILevel):
    startGame('regular')
    playAI(aILevel)

# Change AI level according to what is selected
def playAI(aILevel):

    #
    while turnsLeft.get()>0:
        if aILevel == 1:
            letterNum = levelOneAI()

        elif aILevel == 2:
            letterNum = levelTwoAI()

        elif aILevel == 3:
            letterNum = levelThreeAI()

        checkLetter(letterNum)

        window.update()
        window.after(2000)
        
# Level 1 AI - Random letters
def levelOneAI():
    while True:
        randomNum = random.randint(0,25)
        if buttonList[randomNum]['state'] == 'normal':
            break
    return randomNum

# Level 2 AI - Most common letters
def levelTwoAI():

    while True:

        # https://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
        rangeNum = random.randint(1, 100)

        # Larger ranges for more common letters, smaller ranges for less common letters
        # based on percentages
        if rangeNum >= 1 and rangeNum <= 12:
            randomNum = ord('E')-65
        elif rangeNum >= 13 and rangeNum <= 21:
            randomNum = ord('T')-65
        elif rangeNum >= 22 and rangeNum <= 29:
            randomNum = ord('A')-65
        elif rangeNum >= 30 and rangeNum <= 36:
            randomNum = ord('O')-65
        elif rangeNum >= 37 and rangeNum <= 43:
            randomNum = ord('I')-65
        elif rangeNum >= 44 and rangeNum <= 50:
            randomNum = ord('N')-65
        elif rangeNum >= 51 and rangeNum <= 56:
            randomNum = ord('S')-65
        elif rangeNum >= 57 and rangeNum <= 62:
            randomNum = ord('R')-65
        elif rangeNum >= 63 and rangeNum <= 68:
            randomNum = ord('H')-65
        elif rangeNum >= 69 and rangeNum <= 72:
            randomNum = ord('D')-65
        elif rangeNum >= 73 and rangeNum <= 76:
            randomNum = ord('L')-65
        elif rangeNum >= 77 and rangeNum <= 79:
            randomNum = ord('U')-65
        elif rangeNum == 80 or rangeNum == 81:
            randomNum = ord('C')-65
        elif rangeNum == 82 or rangeNum == 83:
            randomNum = ord('M')-65
        elif rangeNum == 84 or rangeNum == 85:
            randomNum = ord('F')-65
        elif rangeNum == 86 or rangeNum == 87:
            randomNum = ord('Y')-65
        elif rangeNum == 88 or rangeNum == 89:
            randomNum = ord('W')-65
        elif rangeNum == 90 or rangeNum == 91:
            randomNum = ord('G')-65
        elif rangeNum == 92 or rangeNum == 93:
            randomNum = ord('P')-65
        elif rangeNum == 94:
            randomNum = ord('B')-65
        elif rangeNum == 95:
            randomNum = ord('V')-65
        elif rangeNum == 96:
            randomNum = ord('K')-65
        elif rangeNum == 97:
            randomNum = ord('X')-65
        elif rangeNum == 98:
            randomNum = ord('Q')-65
        elif rangeNum == 99:
            randomNum = ord('J')-65
        else:
            randomNum = ord('Z')-65

        # Make sure AI does not select a letter already selected
        if buttonList[randomNum]['state'] == 'normal':
            break

    return randomNum

# Level 3 AI - Most common letter groupings
def levelThreeAI():

    # http://www.rollingr.net/wordpress/2007/02/02/common-letter-sequence/

    # Have the AI recognize common words and letter groupings and complete them
    # Both uppercase and lowercase letters
    if hiddenPhrase.get().find('.HE') >= 0 or hiddenPhrase.get().find('.he') >= 0 and buttonList[ord('T')-65]['state'] == 'normal':
        return ord('T')-65
    elif hiddenPhrase.get().find('T.E') >= 0 or hiddenPhrase.get().find('t.e') >= 0 and buttonList[ord('H')-65]['state'] == 'normal':
        return ord('H')-65
    elif hiddenPhrase.get().find('TH.') >= 0 or hiddenPhrase.get().find('th.') >= 0 and buttonList[ord('E')-65]['state'] == 'normal':
        return ord('E')-65
    elif hiddenPhrase.get().find('.ND') >= 0 or hiddenPhrase.get().find('.nd') >= 0 and buttonList[ord('A')-65]['state'] == 'normal':
        return ord('A')-65
    elif hiddenPhrase.get().find('A.D') >= 0 or hiddenPhrase.get().find('a.d') >= 0 and buttonList[ord('N')-65]['state'] == 'normal':
        return ord('N')-65
    elif hiddenPhrase.get().find('AN.') >= 0 or hiddenPhrase.get().find('an.') >= 0 and buttonList[ord('D')-65]['state'] == 'normal':
        return ord('D')-65
    elif hiddenPhrase.get().find('.OR') >= 0 or hiddenPhrase.get().find('.or') >= 0 and buttonList[ord('F')-65]['state'] == 'normal':
        return ord('F')-65
    elif hiddenPhrase.get().find('F.R') >= 0 or hiddenPhrase.get().find('f.r') >= 0 and buttonList[ord('O')-65]['state'] == 'normal':
        return ord('O')-65
    elif hiddenPhrase.get().find('FO.') >= 0 or hiddenPhrase.get().find('fo.') >= 0 and buttonList[ord('R')-65]['state'] == 'normal':
        return ord('R')-65
    elif hiddenPhrase.get().find('.RE') >= 0 or hiddenPhrase.get().find('.re') >= 0 and buttonList[ord('A')-65]['state'] == 'normal':
        return ord('A')-65
    elif hiddenPhrase.get().find('A.E') >= 0 or hiddenPhrase.get().find('a.e') >= 0 and buttonList[ord('R')-65]['state'] == 'normal':
        return ord('R')-65
    elif hiddenPhrase.get().find('AR.') >= 0 or hiddenPhrase.get().find('ar.') >= 0 and buttonList[ord('E')-65]['state'] == 'normal':
        return ord('E')-65
    elif hiddenPhrase.get().find('.UT') >= 0 or hiddenPhrase.get().find('.ut') >= 0 and buttonList[ord('B')-65]['state'] == 'normal':
        return ord('B')-65
    elif hiddenPhrase.get().find('B.T') >= 0 or hiddenPhrase.get().find('b.t') >= 0 and buttonList[ord('U')-65]['state'] == 'normal':
        return ord('U')-65
    elif hiddenPhrase.get().find('BU.') >= 0 or hiddenPhrase.get().find('bu.') >= 0 and buttonList[ord('T')-65]['state'] == 'normal':
        return ord('T')-65
    elif hiddenPhrase.get().find('.IO') >= 0 or hiddenPhrase.get().find('.io') >= 0 and buttonList[ord('T')-65]['state'] == 'normal':
        return ord('T')-65
    elif hiddenPhrase.get().find('T.O') >= 0 or hiddenPhrase.get().find('t.o') >= 0 and buttonList[ord('I')-65]['state'] == 'normal':
        return ord('I')-65
    elif hiddenPhrase.get().find('TI.') >= 0 or hiddenPhrase.get().find('ti.') >= 0 and buttonList[ord('0')-65]['state'] == 'normal':
        return ord('O')-65
    elif hiddenPhrase.get().find('.ON') >= 0 or hiddenPhrase.get().find('.on') >= 0 and buttonList[ord('I')-65]['state'] == 'normal':
        return ord('I')-65
    elif hiddenPhrase.get().find('I.N') >= 0 or hiddenPhrase.get().find('i.n') >= 0 and buttonList[ord('O')-65]['state'] == 'normal':
        return ord('O')-65
    elif hiddenPhrase.get().find('IO.') >= 0 or hiddenPhrase.get().find('io.') >= 0 and buttonList[ord('N')-65]['state'] == 'normal':
        return ord('N')-65
    elif hiddenPhrase.get().find('.EN') >= 0 or hiddenPhrase.get().find('.en') >= 0 and buttonList[ord('M')-65]['state'] == 'normal':
        return ord('M')-65
    elif hiddenPhrase.get().find('M.N') >= 0 or hiddenPhrase.get().find('m.n') >= 0 and buttonList[ord('E')-65]['state'] == 'normal':
        return ord('E')-65
    elif hiddenPhrase.get().find('ME.') >= 0 or hiddenPhrase.get().find('me.') >= 0 and buttonList[ord('N')-65]['state'] == 'normal':
        return ord('N')-65
    elif hiddenPhrase.get().find('.NT') >= 0 or hiddenPhrase.get().find('.nt') >= 0 and buttonList[ord('E')-65]['state'] == 'normal':
        return ord('E')-65
    elif hiddenPhrase.get().find('E.T') >= 0 or hiddenPhrase.get().find('e.t') >= 0 and buttonList[ord('N')-65]['state'] == 'normal':
        return ord('N')-65
    elif hiddenPhrase.get().find('EN.') >= 0 or hiddenPhrase.get().find('en.') >= 0 and buttonList[ord('T')-65]['state'] == 'normal':
        return ord('T')-65
    elif hiddenPhrase.get().find('.NG') >= 0 or hiddenPhrase.get().find('.ng') >= 0 and buttonList[ord('I')-65]['state'] == 'normal':
        return ord('I')-65
    elif hiddenPhrase.get().find('I.G') >= 0 or hiddenPhrase.get().find('i.g') >= 0 and buttonList[ord('N')-65]['state'] == 'normal':
        return ord('N')-65
    elif hiddenPhrase.get().find('IN.') >= 0 or hiddenPhrase.get().find('in.') >= 0 and buttonList[ord('G')-65]['state'] == 'normal':
        return ord('G')-65
    elif hiddenPhrase.get().find('Q.') >= 0 or hiddenPhrase.get().find('q.') >= 0 and buttonList[ord('T')-65]['state'] == 'normal':
        return ord('U')-65
    else:
        # If no groupings recognized, go back to level 2 AI
        return levelTwoAI()

# Guess the phrase at any time
def guessPhrase():

    guessedPhrase.set(simpledialog.askstring('Guess', 'What is the phrase?', initialvalue = ''))
    if guessedPhrase.get() == phrase.get():

        stopGame('win')

    else:

        # Sound effect
        winsound.PlaySound('Wrong-answer-sound-effect.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
        
        turnsLeft.set(turnsLeft.get()-1)
        showPicture()

        if turnsLeft.get()==0:
            stopGame('loss')

# Give up at any time
def giveUp():

    give = tk.messagebox.askyesno('Give Up', 'Are you sure you would like to give up?')

    if give == True:

        stopGame('loss')
        
# Display the game
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

    # Create the buttons for the frame
    guessButton = tk.Button(gameFrame, text = 'Guess', state = tk.DISABLED, disabledforeground = 'red', command = guessPhrase)
    guessButton.place(x = 450, y = 525, width = 100, height = 50)

    bigButtonList.append(guessButton)

    giveButton = tk.Button(gameFrame, text = 'Give Up', state = tk.DISABLED, disabledforeground = 'red', command = giveUp)
    giveButton.place(x = 550, y = 525, width = 100, height = 50)

    bigButtonList.append(giveButton)

    # Create an info box to direct user to start a game
    tk.messagebox.showinfo('Hello!', 'Click "Game Type" in the upper left corner to get started on a game of Hangperson.  Have fun!')

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
fileMenu.add_command(label="AI Level 2", command=lambda aILevel = 2:aIGame(aILevel))
fileMenu.add_command(label="AI Level 3", command=lambda aILevel = 3:aIGame(aILevel))
fileMenu.add_command(label="Two-Player Game", command=twoPlayerGame)
fileMenu.add_command(label="Exit", command=quitGame)

# Add menus to the menubar
menubar.add_cascade(label="Game Type", menu=fileMenu)
menubar.add_command(label="Help", command=showHelp)

# Disblay the menubar
window.config(menu=menubar)

# Global variables for Login Screen
category = tk.StringVar()
hiddenPhrase = tk.StringVar()
phrase = tk.StringVar()
guessedPhrase = tk.StringVar()
turnsLeft = tk.IntVar()

# Create a style for the frames
pagestyle = ttk.Style()
pagestyle.configure('lightBlue.TFrame', background='light blue')

# Create the game frame and locate it in the top left corner of the window
gameFrame=ttk.Frame(window, width = frameWidth, height = frameHeight, style = 'lightBlue.TFrame')
gameFrame.place(x = 0, y = 0)

# Create a list to hold the leter buttons
buttonList = []
bigButtonList = []

# Setup all the frames
setupGameFrame()

# Start the program
window.mainloop()

# Names: Malcolm and Nicholas
# Date: April 20, 2018
# Course: ICS2O1
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
                hidden += '_'

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
def guessPhrase():

    print('i guess')

#


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
fileMenu.add_command(label="Two-Player Game", command=twoPlayerGame)
fileMenu.add_command(label="Exit", command=showHelp)

# Add menus to the menubar
menubar.add_cascade(label="File", menu=fileMenu)
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

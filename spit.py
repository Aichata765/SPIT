from cmu_graphics import *
import random
import copy

def onAppStart(app):
    app.playRectLeft = 250
    app.playRectTop = 375
    app.playRectWidth = 100
    app.playRectHeight = 50
    app.start = False
    app.startA = True
    app.startB = False
    app.cards = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 
    7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
    print(app.cards)
    app.shuffled = False
    app.distributed = False
    app.lastRounds = False
    app.allowed = True
    app.currentScene = 'spit'
    app.rounds = 0
    app.cardBRectLeft = 225
    app.cardBRectTop = 200
    app.cardBRectWidth = 150
    app.cardBRectHeight = 200
    app.startRoundRectLeft = 250
    app.startRoundRectTop = 300
    app.startRoundRectWidth = 100
    app.startRoundRectHeight = 50
    app.continueRectLeft = 485
    app.continueRectWidth = 70
    app.continueRectTop = 545
    app.continueRectHeight = 30
    app.startRectLeft = 505
    app.startRectWidth =  70
    app.startRectTop = 25
    app.startRectHeight = 30
    app.nextRectLeft = 250
    app.nextRectWidth = 100
    app.nextRectTop = 505
    app.nextRectHeight = 50
    app.winner = None
    app.playStacks = []
    app.stackA = []
    app.stackB = []
    app.spitStackA = []
    app.mainStackA = []
    app.stackC = []
    app.stackD = []
    app.stackE = []
    app.stackF = []
    app.spitStackB = []
    app.mainStackB = []
    app.stackG = []
    app.stackH = []
    app.stackI = []
    app.stackJ = []
    app.playStackX = []
    app.playStackY = []
    app.stacksA = []
    app.stacksB = []
    app.spit = False
    app.cxA = app.width//2
    app.cyA = app.height//2
    app.cxB = app.width//2
    app.cyB = app.height//2
    app.noSpitCards = False
    app.i = 0
    app.j = 0
    app.currCardA = []
    app.currCardB = []
    app.stackAImages = [None, None, None, None, None]
    app.stackBImages = [None, None, None, None, None]
    app.playStacksImages = [None, None]
    app.images = ['AS.jpg', 'AC.jpg', 'AD.jpg', 'AH.jpg', 
                 '2S.jpg', '2C.jpg', '2D.jpg', '2H.jpg', 
                 '3S.jpg', '3C.jpg', '3D.jpg', '3H.jpg',
                 '4S.jpg', '4C.jpg', '4D.jpg', '4H.jpg',
                 '5S.jpg', '5C.jpg', '5D.jpg', '5H.jpg',
                 '6S.jpg', '6C.jpg', '6D.jpg', '6H.jpg',
                 '7S.jpg', '7C.jpg', '7D.jpg', '7H.jpg', 
                 '8S.jpg', '8C.jpg', '8D.jpg', '8H.jpg',
                 '9S.jpg', '9C.jpg', '9D.jpg', '9H.jpg',
                 '10S.jpg', '10C.jpg', '10D.jpg', '10H.jpg',
                 'JS.jpg', 'JC.jpg', 'JD.jpg', 'JH.jpg',
                 'QS.jpg', 'QC.jpg', 'QD.jpg', 'QH.jpg',
                 'KS.jpg', 'KC.jpg', 'KD.jpg', 'KH.jpg', 
                 'Back.jpg', 'White.jpg']


#------------------------------------------------------------------------------------------------------------

def redrawAll(app):
    if app.currentScene == 'spit':
        introPage(app)
    elif app.currentScene == 'instructions':
        instructionsPage(app)
    elif app.currentScene == 'beginning':
        beginning(app)
    elif app.currentScene == 'rounds':
        rounds(app)
    elif app.currentScene == 'transition':
        transition(app)
    elif app.currentScene == 'win':
        win(app)
    

#-------------------------------------------------------------------------------------------------------------

def introPage(app):
    drawRect(app.width//2, 400, 100, 50, align = 'center', fill = 'red', border = 'black', opacity = 70)
    drawLabel("Play", app.width//2, 400, size = 30, font = 'montserrat', bold = True)
    drawImage("SpitCards.jpg", 150, 200, width = 350, height = 350, align = 'center')
    drawImage('SpitCards2.jpg', 450, 200, width = 350, height = 350, align = 'center')
    #drawImage(app.url, 100, 100)
    drawLabel("Spit!!", app.width//2, 150, size = 100, font = 'montserrat', bold = True)

#-------------------------------------------------------------------------------------------------------------

def instructionsPage(app):
    if app.startA == True:
        drawLabel("Instructions:", app.width//2, 30, size = 30, font = 'montserrat', bold = True)
        drawRect(app.width//2, 330, 550, 520, align = 'center', border = 'black', fill = None)
        drawLabel("Layout:", 40, 95, font = 'montserrat', bold = True, size = 20, align = 'left-top')
        drawLabel("11 cards in the middle, one faced up. 2 cards on the left, 2 on the right. 15 in total.", 40, 130, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("You may spread out matching cards from the middle deck to on top of the outside", 40, 150, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("cards one by one.", 40, 170, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("The middle deck may not be flipped over out of order.", 40, 190, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("Start:", 40, 230, font = 'montserrat', bold = True, size = 20, align = 'left-top')
        drawLabel("Count down from 3 and press the space bar to spit.", 40, 265, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("The top card from each spit pile will be put into the center, starting the game.", 40, 285, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("Play Cards:", 40, 320, font = 'montserrat', bold = True, size = 20, align = 'left-top')
        drawLabel("Players simutaneously and quickly play their cards onto either center pile.", 40, 355, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("Only cards that are one rank higher or lower than the center pile's top card can", 40, 375, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("be played.", 40, 395, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("(ex. If the top card is 7, you can play 6 or 8; If the top card is K, you can play A or Q)", 40, 415, font = 'montserrat', align = 'left-top', italic = True)
        drawRect(520, 560, 70, 30, align = 'center', fill = 'white', border = 'black')
        drawLabel("Continue", 520, 560, align = 'center', font = 'montserrat')
        drawLabel("To Win:", 40, 445, font = 'montserrat', bold = True, size = 20, align = 'left-top')
        drawLabel("Continue to play cards until you run out then quickly select the center pile with", 40, 475, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("the least amount of cards.", 40, 495, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("Start new round and keep playing until someone has the least amount of cards", 40, 515, font = 'montserrat', align = 'left-top', bold = True)
        drawLabel("or no cards left", 40, 535, font = 'montserrat', align = 'left-top', bold = True)
    elif app.startB == True:
        drawLabel("Keys:", app.width//2, 30, size = 30, font = 'montserrat', bold = True)
        drawLabel("Player1:", 110, 70, size = 30, font = 'montserrat', bold = True)
        drawLabel("Player2:", 110, 560, size = 30, font = 'montserrat', bold = True)

        for i in range(5):
            drawRect(120 + 90*i, 470, 80, 110, fill = 'red', border = 'black', align = 'center', opacity = 5)
            drawRect(120 + 90*i, 170, 80, 110, fill = 'red', border = 'black', align = 'center', opacity = 5)
            
            drawImage(app.images[52], 120 + 90*i, 470, width = 80, height = 110, align = 'center', opacity = 75)
            drawImage(app.images[52], 120 + 90*i, 170, width = 80, height = 110, align = 'center', opacity = 75)

        for i in range(2):
            drawRect(140 + 320*i, 320, 80, 110, fill = 'red', border = 'black', align = 'center', opacity = 5)
            drawImage(app.images[52], 140+320*i, 320, width = 80, height = 110, align = 'center', opacity = 75)

        for i in range(2):
            drawRect(240 + 120*i, 320, 80, 110, fill = 'white', border = 'black', align = 'center', dashes = True)
       
        drawLabel("Use 'left' and 'right' keys to scroll through the play stacks", app.width//2, 130, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Use 'backspace' to select top card from stack", app.width//2, 150, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Use 'up' or 'down' to place cards onto respective center stacks", app.width//2, 170, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Use 'a' and 'd' keys to scroll through the play stacks", app.width//2, 430, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Use 'tab' to select top card from stack", app.width//2, 450, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Use 'w' or 's' to place cards onto respective center stacks", app.width//2, 470, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Use 'm' to fill in stacks, use '0' and '9' to capture respective center stacks", app.width//2, 190, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Use 'k' to switch top card of main playStack", app.width//2, 210, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Use 'c' to fill in stacks, use '1' and '2' to capture respective center stacks", app.width//2, 490, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Use 'g' to switch top card of main playStack", app.width//2, 510, align = 'center', font = 'montserrat', bold = True)
        
        drawLabel("Player1", 140, 320, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Player2", 460, 320, align = 'center', font = 'montserrat', bold = True)
        drawLabel("Either player can press the spacebar to spit when agreed apon", app.width//2, 395, font = 'montserrat', bold = True)
        drawLabel("P1: 'up, 9'                       P1: 'down, 0'", 220, 310, font = 'montserrat', bold = True, align = 'left-top', size = 10)
        drawLabel("P2: 'w, 1'                             P2: 's, 2'", 220, 330, font = 'montserrat', bold = True, align = 'left-top', size = 10)
        drawRect(540, 40, 70, 30, align = 'center', fill = 'white', border = 'black')
        drawLabel("START", 540, 40, align = 'center', font = 'montserrat')
    
#-------------------------------------------------------------------------------------------------------------
def beginning(app):
    drawImage(app.images[52], app.cxA, app.cyA, width = 150, height = 200, align = 'center')
    drawImage(app.images[52], app.cxB, app.cyB, width = 150, height = 200, align = 'center')
    drawRect(app.cxA, app.cyA, 150, 200, fill = None, border = "black", align = 'center')
    drawRect(app.cxB, app.cyB, 150, 200, fill = None, border = "black", align = 'center')
    drawLabel('Click on cards to shuffle, then press "enter" to distribute cards', app.width//2, 50, size = 15, font = 'montserrat', bold = True)
    if app.distributed == True:
        drawRect(app.width//2, 325, 100, 50, align = 'center', fill = rgb(255, 51, 51), border = 'black', opacity = 50)
        drawLabel('Start Round', app.width//2, 325, size = 13, font = 'montserrat', bold = True)
#-------------------------------------------------------------------------------------------------------------
def rounds(app):
    drawLabel(f'Round {app.rounds}', app.width//2, 30, size = 16, font = 'montserrat', bold = True)
    highlight(app)
    for i in range(5):
        drawRect(80 + 110*i, 470, 100, 130, fill = 'white', border = 'black', align = 'center' )
        drawImage(app.stackBImages[i], 80 + 110*i, 470, width = 100, height = 130, align = 'center')
        drawRect(80 + 110*i, 130, 100, 130, fill = 'white', border = 'black', align = 'center' )
        drawImage(app.stackAImages[i], 80 + 110*i, 130, width = 100, height = 130, align = 'center')
    for i in range(2):
        drawRect(100 + 400*i, app.height//2, 100, 130, fill = 'white', border = 'black', align = 'center', dashes = True)
    
    length1 = len(app.playStackX)
    length2 = len(app.playStackY)
    drawLabel(f"Cards: {length1}", 220, 220, font = 'montserrat', fill = rgb(255, 51, 51))
    drawLabel(f"Cards: {length2}", 380, 220, font = 'montserrat', fill = rgb(255, 51, 51))

    if len(app.spitStackA) > 0:
        image1 = app.images[52]
    else:
        image1 = app.images[53]
    if len(app.spitStackB) > 0:
        image2 = app.images[52]
    else:
        image2 = app.images[53]
    drawImage(image1, 100, app.height//2, width = 100, height = 130, align = 'center')
    drawImage(image2, 500, app.height//2, width = 100, height = 130, align = 'center')
    
    for i in range(2):
        drawRect(220 + 160*i, app.height//2, 100, 130, fill = 'white', border = 'black', align = 'center', dashes = True)
        if len(app.playStackX) > 0:
            drawImage(app.playStacksImages[i], 220 + 160*i, app.height//2, width = 100, height = 130, align = 'center')

#-------------------------------------------------------------------------------------------------------------
def onMousePress(app, mouseX, mouseY):
    #playButton ---------------------------
    right = app.playRectLeft + app.playRectWidth
    bottom = app.playRectTop + app.playRectHeight
    if (app.playRectLeft <= mouseX <= right) and (app.playRectTop <= mouseY <= bottom):
        app.currentScene = 'instructions'
        return True
    #playButton ----------------------------
    #shuffleCards --------------------------
    if app.distributed == False:
        right = app.cardBRectLeft + app.cardBRectWidth
        bottom = app.cardBRectTop + app.cardBRectHeight
        if (app.cardBRectLeft <= mouseX <= right) and (app.cardBRectTop <= mouseY <= bottom):
            shuffleCards(app)
            return True
    #startRound -----------------------------
    right = app.startRoundRectLeft + app.startRoundRectWidth
    bottom = app.startRoundRectTop + app.startRoundRectHeight
    if (app.startRoundRectLeft <= mouseX <= right) and (app.startRoundRectTop <= mouseY <= bottom):
        app.currentScene = 'rounds'
        startRound(app, app.stackA, app.stackB)
        image(app)
        return True
    #instructionsContinue -------------------
    right = app.continueRectLeft + app.continueRectWidth
    bottom = app.continueRectTop + app.continueRectHeight
    if (app.continueRectLeft <= mouseX <= right) and (app.continueRectTop <= mouseY <= bottom):
        app.startA = False
        app.startB = True
    #instructionsStart -----------------------
    right = app.startRectLeft + app.startRectWidth
    bottom = app.startRectTop + app.startRectHeight
    if (app.startRectLeft <= mouseX <= right) and (app.startRectTop <= mouseY <= bottom):
        app.startB = False
        app.currentScene = 'beginning'
    #nextRound -------------------------------- 
    right = app.nextRectLeft + app.nextRectWidth
    bottom = app.nextRectTop + app.nextRectHeight
    if (app.nextRectLeft <= mouseX <= right) and (app.nextRectTop <= mouseY <= bottom):
        if len(app.stackA) < 16:
            lastRounds(app, app.stackA, app.stackB)
        else:
            startRound(app, app.stackA, app.stackB)
        app.currentScene = 'rounds'

    
#-------------------------------------------------------------------------------------------------------------
def image(app):
    for x in range(5):
        for i in range(5):
                for j in range(1, 14):
                    if len(app.stacksA[i]) > 0:
                        if app.stacksA[i][0] == j:
                            app.stackAImages[i] = getImage(app, j, i % 4)
                    else:
                        app.stackAImages[i] = app.images[-1]
                
    for y in range(5):
        for k in range(5):
            for l in range(1, 14):
                if len(app.stacksB[k]) > 0:
                    if app.stacksB[k][0] == l:
                        app.stackBImages[k] = getImage(app, l, y % 4)
                else:
                    app.stackBImages[k] = app.images[-1]
                    
    if len(app.playStackX) > 0 and len(app.playStackY) > 0:
        for z in range(2):
            for m in range(2):
                for n in range(1, 14):
                    if app.playStacks[m][0] == n:
                        app.playStacksImages[m] = getImage(app, n, z % 4)
#-------------------------------------------------------------------------------------------------------------
def getImage(app, card, x):
    return app.images[x + (4*(card-1))]

#-------------------------------------------------------------------------------------------------------------
def transition(app):
    newRound = app.rounds + 1
    drawLabel(f"Round {newRound}", app.width//2, 150, font = 'montserrat', bold = True, size = 50)
    drawRect(190, 350, 150, 200, align = 'center', fill = 'white', border = 'black')
    drawRect(410, 350, 150, 200, align = 'center', fill = 'white', border = 'black')
    drawLabel("Player1", 190, 290, align = 'center', font = 'montserrat', size = 17, bold = True)
    drawLabel("Player2", 410, 290, align = 'center', font = 'montserrat', size = 17, bold = True)
    cards1 = len(app.stackA)
    cards2 = len(app.stackB)
    drawLabel(f"{cards1} cards", 190, 400, align = 'center', font = 'montserrat', size = 17, bold = True)
    drawLabel(f"{cards2} cards", 410, 400, align = 'center', font = 'montserrat', size = 17, bold = True)
    drawRect(300, 530, 100, 50, align = 'center', fill = 'lightYellow', border = 'black')
    drawLabel("Next Round", 300, 530, align = 'center', font = 'montserrat', bold = True)
#-------------------------------------------------------------------------------------------------------------
def highlight(app):
    if -1 < app.i < 5:
        drawRect(80 + 110*app.i, 470, 110, 140, fill = 'red', align = 'center')
    if -1 < app.j < 5:
        drawRect(80 + 110*app.j, 130, 110, 140, fill = 'red', align = 'center')
        
#-------------------------------------------------------------------------------------------------------------
    
def onKeyPress(app, key):
    if key == 'enter':
        if app.currentScene == "beginning":
            divideIntoTwo(app)
            app.distributed = True
    if key == 'space':
        if app.currentScene == "rounds":
            if app.lastRounds == False:
                spit(app)
            else:
                lastSpit(app)
    #stackA ------------------------
    if key == 'backspace':
        #select #edittttt
        if app.j == 2:
            if len(app.mainStackA) > 0:
                app.currCardA = app.mainStackA[0]
                print(f"app.currCardA: {app.currCardA}")
                print(f"mainStackA: {app.mainStackA}")
        elif app.j == 1: #if stack len == 0 do sum
            if len(app.stackD) > 0:
                app.currCardA = app.stackD[0]
                print(f"app.currCardA: {app.currCardA}")
                print(f"stackD: {app.stackD}")
        elif app.j == 0:
            if len(app.stackC) > 0:
                app.currCardA = app.stackC[0]
                print(f"app.currCardA: {app.currCardA}")
                print(f"stackC: {app.stackC}")
        elif app.j == 3:
            if len(app.stackE) > 0:
                app.currCardA = app.stackE[0]
                print(f"app.currCardA: {app.currCardA}")
                print(f"stackE: {app.stackE}")
        elif app.j == 4:
            if len(app.stackF) > 0:
                app.currCardA = app.stackF[0]
                print(f"app.currCardA: {app.currCardA}")
                print(f"stackF: {app.stackF}")
    if key == 'left':
        app.j -= 1
        if app.j < 0:
            app.j = 4
    if key == 'right':
        app.j += 1
        if app.j > 4:
            app.j = 0
    if key == 'up':
        #playStackX
        if len(app.stacksA[app.j]) > 0:
            playMainRow(app, app.currCardA, app.playStackX, app.stacksA)
            print(f"playStackX: {app.playStackX}")
    if key == 'down':
        #playStackY
        if len(app.stacksA[app.j]) > 0:
            playMainRow(app, app.currCardA, app.playStackY, app.stacksA)
            print(f"playStackY: {app.playStackY}")
    if key == '0':
        if app.allowed == True:
            if (all(len(sublist) == 0 for sublist in app.stacksA)) or (all(len(sublist) == 0 for sublist in app.stacksB)):
                capturePlayStack(app, app.playStackY, app.playStackX, app.stacksA)
                if len(app.stackA) == 0:
                    app.currentScene = 'win'
                    app.winner = 'Player1'
                    app.allowed = False
    if key == '9':
        if app.allowed == True:
            if (all(len(sublist) == 0 for sublist in app.stacksA)) or (all(len(sublist) == 0 for sublist in app.stacksB)):
                capturePlayStack(app, app.playStackX, app.playStackY, app.stacksA)
                if len(app.stackA) == 0:
                    app.currentScene = 'win'
                    app.winner = 'Player1'
                    app.allowed = False
    if key == 'k':
        if len(app.mainStackA) >= 2:
            switchTop(app, app.mainStackA)
    if key == 'm':
        spreadOut(app, app.mainStackA, app.stacksA)
    
    #stackB ------------------------
    if key == 'tab':
        #mainStackB select
        if app.i == 0:
            if len(app.stackG) > 0:
                app.currCardB = app.stackG[0]
                print(f"app.currCardB: {app.currCardB}")
                print(f"stackG: {app.stackG}")
        elif app.i == 1:
            if len(app.stackH) > 0:
                app.currCardB = app.stackH[0]
                print(f"app.currCardB: {app.currCardB}")
                print(f"stackH: {app.stackH}")
        elif app.i == 2:
            if len(app.mainStackB) > 0:
                app.currCardB = app.mainStackB[0]
                print(f"app.currCardB: {app.currCardB}")
                print(f"mainStackB: {app.mainStackB}")
        elif app.i == 3:
            if len(app.stackI) > 0:
                app.currCardB = app.stackI[0]
                print(f"app.currCardB: {app.currCardB}")
                print(f"stackI: {app.stackI}")
        elif app.i == 4:
            if len(app.stackJ) > 0:
                app.currCardB = app.stackJ[0]
                print(f"app.currCardB: {app.currCardB}")
                print(f"stackJ: {app.stackJ}")
    if key == "d":
        app.i += 1
        if app.i > 4:
            app.i = 0
    if key == 'a':
        app.i -= 1
        if app.i < 0:
            app.i = 4
    if key == 'w':
        #playStackX
        if len(app.stacksB[app.i]) > 0:
            playMainRow(app, app.currCardB, app.playStackX, app.stacksB)
            print(f"playStackX: {app.playStackX}")
    if key == 's':
        #playStackY
        if len(app.stacksB[app.i]) > 0:
            playMainRow(app, app.currCardB, app.playStackY, app.stacksB)
            print(f"playStackY: {app.playStackY}")
    if key == '2':
        if app.allowed == True:
            if (all(len(sublist) == 0 for sublist in app.stacksB)) or (all(len(sublist) == 0 for sublist in app.stacksA)):
                capturePlayStack(app, app.playStackY, app.playStackX, app.stacksB)
                if len(app.stackB) == 0:
                    app.currentScene = 'win'
                    app.winner = 'Player2'
                    app.allowed = False
    if key == '1':
        if app.allowed == True:
            if (all(len(sublist) == 0 for sublist in app.stacksB)) or (all(len(sublist) == 0 for sublist in app.stacksA)):
                capturePlayStack(app, app.playStackX, app.playStackY, app.stacksB)
                if len(app.stackB) == 0:
                    app.currentScene = 'win'
                    app.winner = 'Player2'
                    app.allowed = False
    if key == 'g':
        if len(app.mainStackB) >= 2:
            switchTop(app, app.mainStackB)
    if key == 'c':
        spreadOut(app, app.mainStackB, app.stacksB)

    
#-------------------------------------------------------------------------------------------------------------
def isLegal(currCard, playStack):
    if len(playStack) == 0:
        return True
    elif (playStack[0] + 1 == currCard or playStack[0] - 1 == currCard):
        return True
    elif (currCard == 1 and playStack[0] == 13 or currCard == 13 and playStack[0] == 1) :
        return True
    return False
#-------------------------------------------------------------------------------------------------------------
    
def switchTop(app, mainStack):
    temp = mainStack[0]
    mainStack[0] = mainStack[1]
    mainStack[1] = temp
    image(app)
    print(mainStack)
    
def firstRowDuplicates(app, stacks):
    nonEmptyStacks = []
    for stack in stacks:
        if len(stack) > 0:
            nonEmptyStacks.append(stack)
    firstElems = []
    for stack in nonEmptyStacks:
        firstElems.append(stack[0])
        
    if len(set(firstElems)) != len(firstElems):
        return True
    return False
    
    
def spreadOut(app, mainStack, stacks):
    print(stacks)
    while len(mainStack) > 0 and firstRowDuplicates(app, stacks):
        for i in range(len(stacks)):
            for j in range(i + 1, len(stacks)):
                if len(stacks[i]) > 0 and len(stacks[j]) > 0 and stacks[i][0] == stacks[j][0]:
                    if j == 2:
                        stacks[i].insert(0, stacks[j][0])
                        stacks[j].pop(0)
                    else:
                        stacks[j].insert(0, stacks[i][0])
                        stacks[i].pop(0)
    count = 0
    for stack in stacks:
        if len(stack) == 0:
            count += 1

    if len(mainStack) > count:
        for i in range(len(stacks)):
            if len(stacks[i]) == 0: 
                stacks[i].append(mainStack[0])
                mainStack.pop(0)
    print(stacks)
    image(app)
    

def capturePlayStack(app, playStack1, playStack2, playerStack):
    if len(playerStack) < 25:
        combineStacks(app, playStack1, playStack2)
        app.currentScene = 'transition'
    else:
        noSign(app) ###

def noSign(app):
    pass 

def combineStacks(app, playStack1, playStack2):
    app.stackAImages = [None, None, None, None, None]
    app.stackBImages = [None, None, None, None, None]
    app.playStacksImages = [None, None]
    stackA = playStack1 + app.stacksA + app.spitStackA
    app.stackA = flatten(stackA)
    random.shuffle(app.stackA)
    stackB = playStack2 + app.stacksB + app.spitStackB
    app.stackB = flatten(stackB)
    random.shuffle(app.stackB)
    app.playStackX = []
    app.playStackY = []
    print(app.stackA)
    print(app.stackB)
    print(app.playStackX)
    print(app.playStackY)
    app.currentScene = 'transition'
    
def flatten(L):
    newList = [elem for sublist in L for elem in (sublist if isinstance(sublist, list) else [sublist])]
    return newList
    
#-------------------------------------------------------------------------------------------------------------
def shuffleCards(app):
    oldList = copy.deepcopy(app.cards)
    random.shuffle(app.cards)
    app.shuffled = True
    print(f"OriginalCards: {app.cards}")
    return app.cards
    
#-------------------------------------------------------------------------------------------------------------
def divideIntoTwo(app):
    for i in range(len(app.cards)):
        if i % 2 == 0:
            app.stackA += [app.cards[i]]
            app.cxA = app.width//2
            app.cyA = 175
        else:
            app.stackB += [app.cards[i]]
            app.cxB = app.width//2
            app.cyB = 475
    print(f"FullStackA: {app.stackA}")
    print(f"FullStackB: {app.stackB}")
    
#-------------------------------------------------------------------------------------------------------------
def startRound(app, stackA, stackB):
    app.allowed = True
    if app.lastRounds == False:
        app.rounds += 1
        app.i = 0
        app.j = 0
        app.spitStackA = stackA[15:]
        app.mainStackA = stackA[:11]
        app.stackC = [stackA[11]]
        app.stackD = [stackA[12]]
        app.stackE = [stackA[13]]
        app.stackF = [stackA[14]]
        app.spitStackB = stackB[15:]
        app.mainStackB = stackB[:11]
        app.stackG = [stackB[11]]
        app.stackH = [stackB[12]]
        app.stackI = [stackB[13]]
        app.stackJ = [stackB[14]]
        app.stacksA = [app.stackC, app.stackD, app.mainStackA, app.stackE, app.stackF]
        app.stacksB = [app.stackG, app.stackH, app.mainStackB, app.stackI, app.stackJ]
        app.playStacks = [app.playStackX, app.playStackY]
        print(f"StacksA: {app.stacksA}")
        print(f"StacksB: {app.stacksB}")
        print(f"SpitA: {app.spitStackA}")
        print(f"SpitB: {app.spitStackB}")
        print(f"MainA {app.mainStackA}")
        print(f"MainB: {app.mainStackB}")
        image(app)
    else:
        app.rounds += 1
        app.i = 0
        app.j = 0
        if len(stackA) < 16:
            app.mainStackA = stackA[1:]
            app.spitStackA = stackA[0]
            app.stackC = []
            app.stackD = []
            app.stackE = []
            app.stackF = []
            app.spitStackB = stackB[15:]
            app.mainStackB = stackB[:11]
            app.stackG = [stackB[11]]
            app.stackH = [stackB[12]]
            app.stackI = [stackB[13]]
            app.stackJ = [stackB[14]]
            
        if len(stackB) < 16:
            app.mainStackB = stackB[1:]
            app.spitStackB = stackB[0]
            app.stackG = []
            app.stackH = []
            app.stackI = []
            app.stackJ = []
            app.spitStackA = stackB[15:]
            app.mainStackA = stackB[:11]
            app.stackC = [stackB[11]]
            app.stackD = [stackB[12]]
            app.stackE = [stackB[13]]
            app.stackF = [stackB[14]]
        app.stacksA = [app.stackC, app.stackD, app.mainStackA, app.stackE, app.stackF]
        app.stacksB = [app.stackG, app.stackH, app.mainStackB, app.stackI, app.stackJ]
        app.playStacks = [app.playStackX, app.playStackY]
        print(f"StacksA: {app.stacksA}")
        print(f"StacksB: {app.stacksB}")
        print(f"SpitA: {app.spitStackA}")
        print(f"SpitB: {app.spitStackB}")
        print(f"MainA {app.mainStackA}")
        print(f"MainB: {app.mainStackB}")
        image(app)
 
#-------------------------------------------------------------------------------------------------------------
def spit(app):
    if len(app.spitStackA) > 0 and len(app.spitStackB) > 0:
        app.playStackX.insert(0, app.spitStackA.pop(0))
        app.playStackY.insert(0, app.spitStackB.pop(0))
        print(f"StackX: {app.playStackX}")
        print(f"StackY: {app.playStackY}")
        print(f"SpitA: {app.spitStackA}")
        print(f"SpitB: {app.spitStackB}")
    else:
        if len(app.spitStackA) > 0:
            app.playStackX.insert(0, app.spitStackA.pop(0))
        elif len(app.spitStackB) > 0:
            app.playStackY.insert(0, app.spitStackB.pop(0))
        else:
            app.noSpitCards == True
    image(app)
    
    
def lastSpit(app):
    if len(app.stackA) < 16 and len(app.spitStackB) > 0:
        app.playStackY.insert(0, app.spitStackB.pop(0))
    elif len(app.stackB) < 16 and len(app.spitStackA) > 0:
        app.playStackX.insert(0, app.spitStackA.pop(0))
        
    #do on step for animation
#-------------------------------------------------------------------------------------------------------------
def lastRounds(app, stackA, stackB):
    #do animation for one card being given to other side
    app.lastRounds = True
    winStack = None
    otherStack = None
    if len(app.stackA) < 16:
        winStack = app.spitStackA
        otherStack = app.spitStackB
    else:
        winStack = app.spitStackB
        otherStack = app.spitStackA
        
    winStack.insert(0, otherStack.pop(0))
    startRound(app, stackA, stackB)
    
def win(app):
    drawLabel(f"{app.winner} Wins!!!!", app.width//2, app.height//2, font = 'montserrat', bold = True, align = 'center', size = 40)
    drawRect(520, 550, 100, 50, align = 'center', fill = rgb(255, 51, 51), border = 'black')
    drawLabel("Restart", 520, 550, align = 'center', font = 'montserrat', bold = True, size = 17)
    
    
    
#-------------------------------------------------------------------------------------------------------------
def playMainRow(app, currCard, playStack, stack):
    if currCard != [] and isLegal(currCard, playStack):
        playStack.insert(0, currCard)
        if stack == app.stacksA:
            stack[app.j].pop(0)
            print(stack)
        else:
            stack[app.i].pop(0)
            print(stack)
    else:
        print('nono')
    image(app)

#-------------------------------------------------------------------------------------------------------------


def main():
    runApp(width = 600, height = 600)

main()   

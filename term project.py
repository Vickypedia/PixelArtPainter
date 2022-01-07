########################################################################
#Name: Yufei Wang
#Andrew ID: yufeiwan
#section: A
#mentor: Gabriel
##########################imports######################################
import random
from tkinter import *
import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter import ttk, colorchooser
#######################################################################    
#######################################################################
def init(data):
    data.mode = "splashScreen" #splashScreen

    data.startAnimation = False
    data.colorPick = False
    data.eraser = False
    data.pen = "black"
    data.emptyColor1 = "white"
    data.emptyColor2 = "grey95"
    data.backGround = "grey36"
    data.cols = 70
    data.rows = 50
    data.margin = 100
    data.cellSize = 10
    data.timer = 0
    
    #circular button radius
    data.r = 25
    
    #draw the art board
    data.board = [([data.emptyColor1]*data.cols) for row in range(data.rows)]
    
    #store the grids that had assigned a special color
    data.selectionDict = {}

    #data.individualCell = []
    data.layer = []
    data.layers = [] 
    
    #here is the data that controls the animation
    data.i = 0
    data.y = 0
    data.animationList = []      
    #data.presentFrame = []

    #drawing a board that can save the color choosed
    data.saveColorCols = 7
    data.saveColorRows = 25
    data.saveColorBoard = [([data.emptyColor1]*data.saveColorCols) \
    for row in range(data.saveColorRows)]
    data.saveColor = {}

    f = open("frame.txt","w")
    #f.write("")


def mousePressed(event, data):
    if (data.mode == "splashScreen"): 
        splashScreenMousePressed(event, data)
    elif(data.mode == "drawingBoard"): 
        drawingBoardMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode == "splashScreen"): 
        splashScreenKeyPressed(event, data)
    elif(data.mode == "drawingBoard"): 
        drawingBoardKeyPressed(event, data)

def timerFired(data):
    #if (data.mode == "splashScreen"): 
        #splashScreentimerFired(data)
    if(data.mode == "drawingBoard"): 
        drawingBoardtimerFired(data)
    pass

def redrawAll(canvas, data):
    if (data.mode == "splashScreen"): 
        splashScreenRedrawAll(canvas, data)
    elif(data.mode == "drawingBoard"): 
        drawingBoardRedrawAll(canvas, data)
        
def mouseDragged(event, data):
    if (data.mode == "splashScreen"): 
        splashScreenMouseDragged(event, data)
    elif(data.mode == "drawingBoard"): 
        drawingBoardMouseDragged(event, data)
def mouseReleased(event, data): 
    if (data.mode == "splashScreen"): 
        splashScreenMouseReleased(event, data)
    elif(data.mode == "drawingBoard"): 
        drawingBoardMouseReleased(event, data)
        
###############################################################################

#splashscreen info
def splashScreentimerFired(data):
    pass

def splashScreenMouseDragged(event, data):
    pass

def splashScreenMousePressed(event, data):
    data.mode = "drawingBoard"
    
def splashScreenMouseReleased(event, data):
    pass
    
def splashScreenKeyPressed(event, data):
    pass

def splashScreenRedrawAll(canvas, data):
    width = data.margin * 2 + data.cellSize * data.cols
    height = data.margin * 2 + data.cellSize * data.rows
    canvas.create_rectangle(0,0,width,height, fill = data.backGround)
    canvas.create_text(data.width/4, data.height/2-data.height/5,\
        text="Pixel Art Painter", font="Arial 26 bold", fill = "white")
    canvas.create_text(data.width/2, data.height/2+data.height/4,\
        text="mouse click to start", font="Arial 12 bold", fill = "white")
    
#########################################################################

def playDrawing(rows=50,cols=70): #general info for this game
    cellSize = 10
    margin = 100
    width = margin * 2 + cellSize * cols
    height = margin * 2 + cellSize * rows
    return (width,height) 
    
def drawingBoard(canvas,data):
    #assigning the second empty color to the board
    for i in range(0,len(data.board),2):
        for j in range(0,len(data.board[0]),2):
            data.board[i][j] = data.emptyColor2
            
    for i in range(1,len(data.board),2):
        for j in range(1,len(data.board[0]),2):
            data.board[i][j] = data.emptyColor2
    #drawing the board with the colors
    for i in range(len(data.board)):
        for j in range(len(data.board[0])):
            color = data.board[i][j]
            drawCell(canvas,data,i,j,color)
            
def drawCell(canvas,data,rows,cols,color):
    #drawing the individual cells
    left = data.margin + data.cellSize * cols
    top = data.margin + data.cellSize * rows
    right = left + data.cellSize
    bottom = top + data.cellSize
    
    canvas.create_rectangle( left, top, right, bottom, fill = color, \
        outline = "")
        
def drawingSaveColorBoard(canvas,data):
    #assigning the second empty color to the board
    for i in range(0,len(data.saveColorBoard),2):
        for j in range(0,len(data.saveColorBoard[0]),2):
            data.saveColorBoard[i][j] = data.emptyColor2
            
    for i in range(1,len(data.saveColorBoard),2):
        for j in range(1,len(data.saveColorBoard[0]),2):
            data.saveColorBoard[i][j] = data.emptyColor2
            
    #drawing the board with the colors
    for i in range(len(data.saveColorBoard)):
        for j in range(len(data.saveColorBoard[0])):
            color = data.saveColorBoard[i][j]
            drawSaveColorCell(canvas,data,i,j,color)
    
    canvas.create_text(data.margin/2,610,\
        text = "color palette", fill = "white", font = "arial 10 ")
            
def drawSaveColorCell(canvas,data,rows,cols,color):
    #drawing the individual cells
    left = 15 + data.cellSize * cols
    top = 350 + data.cellSize * rows
    right = left + data.cellSize
    bottom = top + data.cellSize
    
    canvas.create_rectangle( left, top, right, bottom, fill = color, \
        outline = "")

###############################################################################        
#helper functions for knowing which cell to color(which cell got clicked)
    
def clickInGrid(x, y, data):
    # checking if the click of the cursor is outside of the board
    return ((data.margin <= x <= data.width-data.margin) and
            (data.margin <= y <= data.height-data.margin))

def clickInSaveColorGrid(x, y, data):
    # checking if the click of the cursor is outside of the save color board
    return ((15 <= x <= 85) and
            (350 <= y <= data.height-data.margin))

def getCell(x, y, data):
    # get the location of the cell in the board (which row, which column)
    if (not clickInGrid(x, y, data)):
        return (None, None)
    cellSize  = data.cellSize
    row = (y - data.margin) // cellSize
    col = (x - data.margin) // cellSize
    return (row, col)

def getSaveColorCell(x, y, data):
    # get the location of the cell in the board (which row, which column)
    if (not clickInSaveColorGrid(x, y, data)):
        return (None, None)
    cellSize  = data.cellSize
    row = (y - 350) // cellSize
    col = (x - 15) // cellSize
    return (row, col)
    
def getCellBounds(row, col, data):
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    cellSize = data.cellSize
    x0 = data.margin + col * cellSize
    x1 = data.margin + (col+1) * cellSize
    y0 = data.margin + row * cellSize
    y1 = data.margin + (row+1) * cellSize
    return (x0, y0, x1, y1)
    
def getSaveColorCellBounds(row, col, data):
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    cellSize = data.cellSize
    x0 = 15 + col * cellSize
    x1 = 15 + (col+1) * cellSize
    y0 = 350 + row * cellSize
    y1 = 350 + (row+1) * cellSize
    return (x0, y0, x1, y1)
    
#change the color of the pen by using the color chooser

def getColor(data):
    #set the color of the pen to the new color selected
    data.pen = askcolor(color = data.pen)[1]
    
######################################################    

#detect if cursor clicked inside these buttons

def clickInsideOvalButton(x0,y0,x1,y1,r):
    return (((x1-x0)**2 + (y1-y0)**2)**0.5 <= r)
    
    
def clickInsideRecButton(x0,y0,x1,y1,x2,y2):
    return (x1 <= x0 <= x2) and (y1 <= y0 <= y2)
    
###############################################################################


def writeFile(path,content,data):
    with open(path, "a") as f:
        f.write(str(data.layers))
        
def readFile(path,content,data):
    with open(path, "r") as f:
        return f.read()

def addNewFrame(data):
    data.layer = []
    #contentsToWrite = data.layers
    #writeFile("frame.txt",contentsToWrite,data)
    individualCell = []
    for key in data.selectionDict:
        individualCell.append(key[0])
        individualCell.append(key[1])
        individualCell.append(data.selectionDict[key])
        data.layer.append(individualCell)
        individualCell = []
    if (data.layer not in data.layers) or (data.layer == []):
        data.layers.append(data.layer)

    #print(data.layers)
    data.selectionDict.clear()
    
'''
def deleteFrame(data):
    if data.layers[data.i] == data.presentFrame:
        data.layers = data.layers.pop(data.i)
    elif data.layers[data.i] != data.presentFrame:
        data.layers = data.layers.pop(data.i-1)
    pass
'''

def copyFrame(data):
    data.layer = []
    individualCell = []
    for key in data.selectionDict:
        individualCell.append(key[0])
        individualCell.append(key[1])
        individualCell.append(data.selectionDict[key])
        data.layer.append(individualCell)
        individualCell = []
    data.layers.append(data.layer)
    
def GoingThroughFrame(data,i):
    return data.layers[i]

##############################################################################

#draw all the rectangular buttons on the left side
    
def drawAddButton(canvas,data):
    canvas.create_rectangle(data.margin/4-15,data.margin+5,\
         3*data.margin/4+15,data.margin + 35,\
        outline = "white", width = 2)
    canvas.create_text(data.margin/2,data.margin+20,\
        text = "add frame", fill = "white", font = "arial 10")    
        
'''
def drawDeleteButton(canvas,data):
    canvas.create_rectangle(data.margin/4-15,data.margin+50,\
         3*data.margin/4+15,data.margin + 80,\
        outline = "white", width = 2)
    canvas.create_text(data.margin/2,data.margin+65,\
        text = "delete frame", fill = "white", font = "arial 10")    
'''

def drawCopyButton(canvas,data):
    canvas.create_rectangle(data.margin/4-15,data.margin+50,\
         3*data.margin/4+15,data.margin + 80,\
        outline = "white", width = 2)
    canvas.create_text(data.margin/2,data.margin+65,\
        text = "copy frame", fill = "white", font = "arial 10")  
        
def drawExportButton(canvas,data):
    canvas.create_rectangle(data.margin/4-15,data.margin+95,\
        3*data.margin/4+15,data.margin + 125,\
        outline = "white", width = 2)
    canvas.create_text(data.margin/2,data.margin+110,\
        text = "export", fill = "white", font = "arial 10")    

def drawClearAllButton(canvas,data):
    canvas.create_rectangle(data.margin/4-15,data.margin+140,\
        3*data.margin/4+15,data.margin + 170,\
        outline = "white", width = 2)
    canvas.create_text(data.margin/2,data.margin+155,\
        text = "clear all", fill = "white", font = "arial 10")   
        
def drawImportButton(canvas,data):
    canvas.create_rectangle(data.margin/4-15,data.margin+185,\
        3*data.margin/4+15,data.margin + 215,\
        outline = "white", width = 2)
    canvas.create_text(data.margin/2,data.margin+200,\
        text = "import", fill = "white", font = "arial 10")   

#################################

#draw all the rectangular buttons on the right side

def drawPenButton(canvas,data):
    canvas.create_rectangle(data.width-3*data.margin/4-15,data.margin+5,\
        data.width - data.margin/4+15,data.margin + 35,\
        outline = "white", width = 2)
    canvas.create_text(data.width - data.margin/2,data.margin+20,\
        text = "pen", fill = "white", font = "arial 10")
    
def drawColorButton(canvas,data):
    canvas.create_rectangle(data.width-3*data.margin/4-15,data.margin+50,\
        data.width - data.margin/4+15,data.margin + 80,\
        outline = "white", width = 2)
    canvas.create_text(data.width - data.margin/2,data.margin+65,\
        text = "color", fill = "white", font = "arial 10")
    
def drawEraserButton(canvas,data):
    canvas.create_rectangle(data.width-3*data.margin/4-15,data.margin+95,\
        data.width - data.margin/4+15,data.margin + 125,\
        outline = "white", width = 2)
    canvas.create_text(data.width - data.margin/2,data.margin+110,\
        text = "eraser", fill = "white", font = "arial 10")
    
def drawPickButton(canvas,data):
    canvas.create_rectangle(data.width - 3*data.margin/4-15,data.margin+140,\
        data.width - data.margin/4+15,data.margin + 170,\
        outline = "white", width = 2)
    canvas.create_text(data.width - data.margin/2,data.margin+155,\
        text = "eyedropper", fill = "white", font = "arial 10")
    
def drawClearButton(canvas,data):
    canvas.create_rectangle(data.width - 3*data.margin/4-15,data.margin+185,\
        data.width - data.margin/4+15,data.margin + 215,\
        outline = "white", width = 2)
    canvas.create_text(data.width - data.margin/2,data.margin+200,\
        text = "clear layer", fill = "white", font = "arial 10 ")

###################################

#draw all the circular buttons on the right side

def drawStartButton(canvas,data):
    #for the outline of the button
    cx = data.width - data.margin/2
    cy = data.margin+400
    r = data.r
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,outline = "white", width = 2)
    
    #for the triangle shape inside the button
    #that indicates that this is the start button
    x0, y0 = data.width - data.margin/2-7 , data.margin-15+400
    x1, y1 = data.width - data.margin/2-7 , data.margin+15+400
    x2, y2 = data.width - data.margin/2+15, data.margin+400
    canvas.create_polygon(x0,y0,x1,y1,x2,y2,\
        fill = "white",outline = "white", width = 1)
    
    
def drawStopButton(canvas,data):
    #for the outline of the button
    cx = data.width - data.margin/2
    cy = data.margin+325
    r = data.r
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r,outline = "white", width = 2)
    
    #for the two straight lines goes inside the button
    canvas.create_rectangle(data.width - data.margin/2-7,\
        data.margin-12+325,data.width - data.margin/2-4,\
        data.margin+10+325,fill = "white",outline = "white", width = 1)
    canvas.create_rectangle(data.width - data.margin/2+4,\
        data.margin-12+325,data.width - data.margin/2+7,\
        data.margin+10+325,fill = "white",outline = "white", width = 1)

###############################################################################

def drawFrameCollection(canvas,data):
    canvas.create_rectangle(data.margin,\
        data.height - 60,data.width - data.margin,\
        data.height - 45,fill = "",outline = "white", width = 1)
    canvas.create_text(data.width/2,data.height-25,\
        text = "t i m e l i n e", fill = "white", font = "arial 10 ")
        
def drawFrameIndicator(canvas,data):
    if len(data.layers) > 0:
        distanceBetweenIndicator = data.cellSize * data.cols /(len(data.layers))
        x0,y0 = 0,0
        x1,y1 = 2,5
    
        for i in range(len(data.layers)):
            canvas.create_rectangle(data.margin + i*distanceBetweenIndicator+x0,\
                data.height - 65 + y0, data.margin + i*distanceBetweenIndicator+x1,\
                data.height - 45 + y1, fill = "white",outline = "white", width = 1)
            
###############################################################################
def drawingBoardMousePressed(event, data):
    (row, col) = getCell(event.x, event.y, data)
    selection = (row, col)
    #eraser eraser any cells that got colored above the board
    if data.eraser:
        if selection in data.selectionDict:
            del data.selectionDict[selection]
        if clickInSaveColorGrid(event.x, event.y, data):
            (saveColorRow, saveColorCol) = getSaveColorCell(event.x, event.y, data)
            saveColorSelection = (saveColorRow, saveColorCol)
            if saveColorSelection in data.saveColor:
                del data.saveColor[saveColorSelection]
            
    #color picker pick the color the mouse clicked on
    #and return to the pen mode after mouse being clicked
    if data.colorPick:
        if clickInGrid(event.x, event.y, data):
            if selection in data.selectionDict:
                data.pen = data.selectionDict[selection]
                data.colorPick = False
            elif selection not in data.selectionDict:
                data.pen = None
                data.colorPick = False
        if clickInSaveColorGrid(event.x, event.y, data):
            (saveColorRow, saveColorCol) = getSaveColorCell(event.x, event.y, data)
            saveColorSelection = (saveColorRow, saveColorCol)
            if saveColorSelection in data.saveColor:
                data.pen = data.saveColor[saveColorSelection]
                data.colorPick = False
            elif saveColorSelection not in data.saveColor:
                data.pen = None
                data.colorPick = False
            
    #when neither eraser  nor color picker is functioning, default 
    #function is the pen tool
    if data.eraser == False and data.colorPick == False:
        if clickInGrid(event.x, event.y, data):
            data.selectionDict[selection] = data.pen
            
    #click inside the color chooser button will allow the user to use the 
    #color chooser
    if clickInsideRecButton(event.x,event.y,data.width-3*data.margin/4-15,\
    data.margin+50,data.width - data.margin/4+15,data.margin + 80):
        command = getColor(data)
        data.eraser = False
        data.colorPick = False
        data.startAnimation = False
        
    #click inside the pen button will switch the function to pen
    if clickInsideRecButton(event.x,event.y,data.width-3*data.margin/4-15,\
    data.margin+5,data.width - data.margin/4+15,data.margin + 35):
        data.eraser = False
        data.colorPick = False
        data.startAnimation = False
        
    #click inside the eraser button will switch the function to eraser
    if clickInsideRecButton(event.x,event.y,data.width-3*data.margin/4-15,\
    data.margin+95,data.width - data.margin/4+15,data.margin + 125):
        data.eraser = True
        data.startAnimation = False
        
    #click inside the eyedropper button will switch the function to eyedropper
    if clickInsideRecButton(event.x,event.y,data.width-3*data.margin/4-15,\
    data.margin+140,data.width - data.margin/4+15,data.margin + 170):
        data.colorPick = True
        data.eraser = False
        data.startAnimation = False
        
    #click inside the clear button will clear everything on the canvas
    if clickInsideRecButton(event.x,event.y,data.width-3*data.margin/4-15,\
    data.margin+185,data.width - data.margin/4+15,data.margin + 215):
        data.selectionDict.clear()
        data.eraser = False
        data.startAnimation = False
    
    #adding a new frame to the animation
    if clickInsideRecButton(event.x,event.y,data.margin/4-15,\
    data.margin+5,3*data.margin/4+15,data.margin + 35):
        addNewFrame(data)
        data.startAnimation = False
        
    '''
    #deleting a frame from the animation
    if clickInsideRecButton(event.x,event.y,data.margin/4-15,\
    data.margin+50,3*data.margin/4+15,data.margin + 80):
        deleteFrame(data)
        data.startAnimation = False
    '''
    
    #clicking the export button allows people to store the layer information 
    #into a txt file
    if clickInsideRecButton(event.x,event.y,data.margin/4-15,\
    data.margin+95,3*data.margin/4+15,data.margin + 125):
        contentsToWrite = data.layers
        writeFile("frame.txt",contentsToWrite,data)
        
    #copy previous frame from the animation
    if clickInsideRecButton(event.x,event.y,data.margin/4-15,\
    data.margin+50,3*data.margin/4+15,data.margin + 80):
        copyFrame(data)
        data.startAnimation = False
        
    #clear everything stored within the app
    if clickInsideRecButton(event.x,event.y,data.margin/4-15,\
    data.margin+140,3*data.margin/4+15,data.margin + 170):
        data.layer = []
        data.layers = []
        data.selectionDict = {}
        data.animationList = []
        data.i = 0
        data.startAnimation = False
        
    #click inside the start button will start the animation
    if clickInsideOvalButton(event.x,event.y,data.width - data.margin/2,data.margin+400,data.r):
        data.startAnimation = True
    
    #click inside the stop button will stop the animation
    if clickInsideOvalButton(event.x,event.y,data.width - data.margin/2,data.margin+325,data.r):
        data.startAnimation = False
        data.presentFrame = data.animationList
    
    #click inside the save color grid to saving colors 
    if clickInSaveColorGrid(event.x, event.y, data):
        (saveColorRow, saveColorCol) = getSaveColorCell(event.x, event.y, data)
        saveColorSelection = (saveColorRow, saveColorCol)
        if data.eraser == False and data.colorPick == False:
            data.saveColor[saveColorSelection] = data.pen
        
def drawingBoardMouseDragged(event, data):
    (row, col) = getCell(event.x, event.y, data)
    selection = (row, col)
    if data.eraser:
        if selection in data.selectionDict:
            del data.selectionDict[selection]
    if data.eraser == False and data.colorPick == False:
        if clickInGrid(event.x, event.y, data):
            data.selectionDict[selection] = data.pen

def drawingBoardMouseReleased(event, data):
    pass
    
def drawingBoardtimerFired(data):

    if not data.startAnimation:
        data.timer += 0
    
    if data.startAnimation:
        data.layer = []
        individualCell = []
        for key in data.selectionDict:
            individualCell.append(key[0])
            individualCell.append(key[1])
            individualCell.append(data.selectionDict[key])
            data.layer.append(individualCell)
            individualCell = []
        if data.layer not in data.layers:
            data.layers.append(data.layer)
        data.timer += 1
        if data.timer % 1 == 0:
            data.animationList = GoingThroughFrame(data,data.i)
            data.i += 1
            data.y += 1
        if data.i == len(data.layers):
            data.i = 0
        if data.y > len(data.layers):
            data.y = 1

def drawingBoardKeyPressed(event, data):
    pass
                
def drawingBoardRedrawAll(canvas,data):
    canvas.create_rectangle(0,0,playDrawing(rows=90,cols=160)[0],\
        playDrawing(rows=90,cols=160)[1], fill = data.backGround)
    drawingBoard(canvas,data)
    drawColorButton(canvas,data)
    drawPickButton(canvas,data)
    drawClearButton(canvas,data)
    drawPenButton(canvas,data)
    drawEraserButton(canvas,data)
    drawStartButton(canvas,data)
    drawStopButton(canvas,data)
    drawExportButton(canvas,data)
    #drawDeleteButton(canvas,data)
    drawCopyButton(canvas,data)
    drawAddButton(canvas,data)
    drawClearAllButton(canvas,data)
    drawFrameCollection(canvas,data)
    drawFrameIndicator(canvas,data)
    drawingSaveColorBoard(canvas,data)
    #drawImportButton(canvas,data)
    
    for cell in data.saveColor:
            (x0, y0, x1, y1) = getSaveColorCellBounds(cell[0], cell[1], data)
            canvas.create_rectangle(x0, y0, x1, y1, \
            fill = data.saveColor[cell], outline = "")
    
    if not data.startAnimation:
        canvas.create_text(data.margin + 40,data.margin-25,\
            text = "Frame %d" %(1 + len(data.layers)), fill = "white", font = "arial 15 bold ")
        for cell in data.selectionDict:
            (x0, y0, x1, y1) = getCellBounds(cell[0], cell[1], data)
            canvas.create_rectangle(x0, y0, x1, y1, \
            fill = data.selectionDict[cell], outline = "")
    
        for cell in data.layer:
            (x0, y0, x1, y1) = getCellBounds(cell[0], cell[1], data)
            canvas.create_rectangle(x0, y0, x1, y1, \
            fill = cell[2], stipple = "gray25",outline = "")
            
    if data.startAnimation:
        for cell in data.animationList:
            (x0, y0, x1, y1) = getCellBounds(cell[0], cell[1], data)
            canvas.create_rectangle(x0, y0, x1, y1, \
            fill = cell[2], outline = "")       
            canvas.create_text(data.margin + 40,data.margin-25,\
            text = "Frame %d" %data.y, fill = "white", font = "arial 15 bold ")
            
####################################
# use the run function as-is
####################################

#this run function is adapted from the run framework provided
#by instructor

def run(width=900, height=900):
    def redrawAllWrapper(canvas, data):
        root.unbind("<Motion>")
        root.unbind("<B1-Motion>")
        root.unbind("<B1-MotionRelease>")
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()
        root.bind("<Motion>", lambda event: callFn('mouseMoved', event))
        root.bind("<B1-Motion>", lambda event: callFn('mouseDragged', event))
        root.bind("<B1-ButtonRelease>", lambda event: callFn('mouseReleased', event))

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)
        
    def mouseMotionWrapper():
        if (((data._mouseIsPressed == False) and (data._mouseMovedDefined == True)) or
            ((data._mouseIsPressed == True ) and (data._mouseDragDefined == True))):
            event = Struct()
            event.x = root.winfo_pointerx() - root.winfo_rootx()
            event.y = root.winfo_pointery() - root.winfo_rooty()
            if ((data._lastMousePosn !=  (event.x, event.y)) and
                (event.x >= 0) and (event.x <= data.width) and
                (event.y >= 0) and (event.y <= data.height)):
                if(data._mouseIsPressed == True):
                    mouseDragged(event, data)
                else:
                    result = mouseMoved(event, data)
                #fn = 'mouseDragged' if (data._mouseIsPressed == True) else 'mouseMoved'
                #print(fn)
                #callFn(fn, event)
        data._afterId2 = root.after(data.mouseMovedDelay, mouseMotionWrapper)

    def callFn(fn, event=None):
        if (fn == 'mousePressed' or fn == 'mouseDragged'): data._mouseIsPressed = True
        elif (fn == 'mouseReleased'): data._mouseIsPressed = False
        if ('mouse' in fn): data._lastMousePosn = (event.x, event.y)
        if (fn in globals()):
            if (fn.startswith('key')):
                c = event.key = event.char
                if ((c in [None, '']) or (len(c) > 1) or (ord(c) > 255)):
                    event.key = event.keysym
                elif (c == '\t'): event.key = 'Tab'
                elif (c in ['\n', '\r']): event.key = 'Enter'
                elif (c == '\b'): event.key = 'Backspace'
                elif (c == chr(127)): event.key = 'Delete'
                elif (c == chr(27)): event.key = 'Escape'
                elif (c == ' '): event.key = 'Space'
                if (event.key.startswith('Shift')): return
            args = [data] if (event == None) else [event, data]
            globals()[fn](*args)
            redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    data.mouseMovedDelay = 30
    data._mouseIsPressed = False
    data._lastMousePosn = (-1, -1)
    data._mouseMovedDefined = 'mouseMoved' in globals()
    data._mouseDragDefined = 'mouseDragged' in globals()
    data._afterId1 = data._afterId2 = None
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<Motion>", lambda event: callFn('mouseMoved', event))
    root.bind("<B1-Motion>", lambda event: callFn('mouseDragged', event))
    root.bind("<B1-ButtonRelease>", lambda event: callFn('mouseReleased', event))
    callFn('init')
    if ('timerFired' in globals()): timerFiredWrapper(canvas, data)
    if (data._mouseMovedDefined or data._mouseDragDefined): mouseMotionWrapper()
    # and launch the app
    root.mainloop()  # blocks until window is closed
    if (data._afterId1): root.after_cancel(data._afterId1)
    if (data._afterId2): root.after_cancel(data._afterId2)
    print("bye!")


width = playDrawing()[0]
height = playDrawing()[1]
run(width, height)

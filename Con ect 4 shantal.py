blackCircle ="\u23FA"
whiteCircle="\u26AA"
print(blackCircle)
print(whiteCircle)
#make a board
board = [[" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "]
         ]

def printboard():
    for i in range(6):        
        print("|",end = " ")
        for j in range(7):
            if board[i][j] == "":
                print(board[i][j],end = "")
                print("|",end = " ")
            else:
                print(board[i][j],end = "")
                print("|",end = " ")                
        print("")
    
    

def printboard2():
    for i in range(6):
        print(board[i])
    numbers = ["1", "2", "3", "4", "5","6","7"]
    print(numbers)

printboard2()


def playermove(player,col):
    for i in range(5,0,-1):
        if(board[i][col-1]==" "):
            board[i][col-1] = player
            return(True)
        
        if(board[0][col-1]!=" "):
            return(False)
        
def checkhorizontal ():
    for i in range (5,0,-1):
        for j in range (4):
            if board[i][j]!=" " :
                if board[i][j]==board[i][j+3]:
                    if board[i][j]==board[i][j+1] and board[i][j]==board[i][j+2] and board[i][j] != " ":
                        print ("You Win!")
                        return (True)
               
    return (False)

def checkvertical ():
    for j in range (7):
        for i in range (5,3,-1):
            if board[i][j]!=" " :
                if board[i][j]==board[i-3][j]:
                    if board[i][j]==board[i-1][j] and board[i][j]==board[i-2][j] and board[i][j] != " ":
                        print ("You Win!")
                        return (True)
def checkdiagonal ():
    for j in range (3):
        for i in range (5,3,-1):
            if board[i][j]!=" " :
                if board[i][j]==board[i-3][j+3]:
                    if board[i][j]==board[i-1][j+1] and board[i][j]==board[i-2][j+2] and board[i][j] != " ":
                        print ("You Win!")
                        return True

    for i in range (5,3,-1):
        for j in range (4):    
            if board[i][j]!=" " :
                if board[i][j]==board[i-3][j+3]:
                    if board[i][j]==board[i-1][j+1] and board[i][j]==board[i-2][j+2] and board[i][j] != " ":
                        print ("You Win!")
                        return True

    #reverse direction
    for j in range (6,3,-1):
        for i in range (5,3,-1):
            if board[i][j]!=" " :
                if board[i][j]==board[i-3][j-3]:
                    print("possible win")
                    if board[i][j]==board[i-1][j-1] and board[i][j]==board[i-2][j-2] and board[i][j] != " ":
                        print ("You Win!")
                        return True

    for i in range (5,3,-1):
        for j in range (6,3,-1):    
            if board[i][j]!=" " :
                if board[i][j]==board[i-3][j-3]:
                    if board[i][j]==board[i-1][j-1] and board[i][j]==board[i-2][j-2] and board[i][j] != " ":
                        print ("You Win!")
                        return True


        
valid = False        
win = False
while(win == False):

    while (valid == False):
        movechoice = input("Hello player 1, where do you want to go?")   

        if (int(movechoice) < 1 or int(movechoice) > 7):
            print("That isn't a option, please try again.")
##        else:
##            if (" "

        valid = playermove("x", int(movechoice))
        printboard2()
        numbers = (" 1  2  3  4  5  6  7")
        print(numbers)

    valid = False
    
    win = checkvertical()
    if win == True:
        break
    win = checkhorizontal()
    if win == True:
        break
    win = checkdiagonal()
    if win == True:
        break
    
    
    while (valid == False):
        
        movechoice2 = input("Hello player 2, where do you want to go?")

        if (int(movechoice2) < 1 or int(movechoice2) > 7):
            print("That isn't a option, please try again.")
        else:
            valid = playermove("o", int(movechoice2))
        
    printboard2()
    print(numbers)

    
    valid = False
    win = checkvertical()
    if win == True:
        break
    win = checkhorizontal()
    if win == True:
        break
    win = checkdiagonal()
    if win == True:
        break
    
    win = checkhorizontal()



            

import numpy
import math

def initializeGame():
    cards=numpy.random.permutation([math.ceil((x+1)/4)+1 for x in range(52)])
    print (cards)
    player1=list(cards[:26])
    player2=list(cards[26:])
    return player1,player2

def playRound(player1, player2):
    currentBattle=[[player1.pop(0)],[player2.pop(0)]]
    while(1):
        print("New play: ", currentBattle[0],currentBattle[1],player1, player2)
        if currentBattle[0][len(currentBattle[0])-1]>currentBattle[1][len(currentBattle[1])-1]:player1+=list(numpy.random.permutation(currentBattle[0]+currentBattle[1]));break
        elif currentBattle[0][len(currentBattle[0])-1]<currentBattle[1][len(currentBattle[1])-1]:player2+=list(numpy.random.permutation(currentBattle[0]+currentBattle[1]));break
        if len(player1)==0 or len(player2)==0: break
        for x in range(4):
            if len(player1)>0 and len(player2)>0:
                currentBattle[0].append(player1.pop(0))
                currentBattle[1].append(player2.pop(0))
            else:break
    return player1,player2

def playGame():
    player1, player2 = initializeGame()
    while(1):
        player1, player2=playRound(list(player1), list(player2))
        if len(player1)== 0 and len(player2)== 0: return "You both lose! jk, it is a draw!"
        if len(player1)== 0: return "Player TWO wins!"
        if len(player2)== 0: return "Player ONE wins!"

print(playGame())



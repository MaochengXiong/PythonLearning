import random
# color = ["H","S","C","D"]

def getDeck(number):
    deck = []
    for i in range(4):
        for j in range(len(number)):
            deck.append(number[j])
        deck.append("J")
        deck.append("Q")
        deck.append("K")
        deck.append("A")            
    deck.append("joker")
    deck.append("Joker")
    random.shuffle(deck)    
    return deck
# print (deck[0][1])


def changeCardToNum(card):
    c = []
    c = card.copy()
    for i in range(len(c)):
        if(c[i]=="J"):
            c[i]=11
        elif(c[i]=='Q'):
            c[i]=12
        elif(c[i]=='K'):
            c[i]=13
        elif(c[i]=='A'):
            c[i]=14
        elif(c[i]==2):
            c[i]=15
        elif(c[i]=='joker'):
            c[i]=16
        elif(card[i]=='Joker'):
            c[i]=17
    return c

def changeNumToCard(card):
    c = []
    c = card.copy()
    for i in range(len(card)):
        if(c[i]==11):
            c[i]='J'
        elif(c[i]==12):
            c[i]='Q'
        elif(c[i]==13):
            c[i]='K'
        elif(c[i]==14):
            c[i]='A'
        elif(c[i]==15):
            c[i]=2
        elif(c[i]==16):
            c[i]='joker'
        elif(c[i]==17):
            c[i]='Joker'
    return c

def isSingle(card):
    if(len(card)==1):
        return True
    return False

def isDouble(card):
    
    if (len(card)==2 and card[0]==card[1]):
        return True
    return False

def isThreeWithOne(card):
    count = 0
    count2 = 0
    if (len(card)!=4):
        return False
    for i in range(3):
        if(card[i]==card[3]):
            count = count+1
    for j in range(3):  
        if(card[1]==card[3-j]):
            count2 = count2+1
    if (count==2 or count2 == 2):
        return True
    return False

def isBomb(card):
    count = 0
    if (len(card)!=4):
        return False
    for i in range(3):
        if(card[i]==card[3]):
            count = count+1
    if (count==3):
        return True
    return False

def isOneCardSeq(card):
    a = changeCardToNum(card)
    temp = sorted(a)
    if(len(a)<5):
        return False
    for j in range(len(temp)-1):
        if(temp[j]+1!=temp[j+1]):
            return False
    return True

def isTwoCardSeq(card):
    a = changeCardToNum(card)
    if(len(a)<6 and len(a)%2!=0):
        return False
    temp = []  
    temp = sorted(a)
    for j in range(0,len(temp)-4,2):
        if(temp[j]!=temp[j+1] or temp[j]+1!=temp[j+2]):
            return False
    if(temp[-1]!=temp[-2]):
        return False
    return True

def isRocket(card):
    if(len(card)!=2):
        return False
    a = changeCardToNum(card)
    if(a[0]+a[1]!=33):
        return False
    return True

def isLegal(card):
    string = "it is illegal"
    if(isSingle(card)):
        return "it is single"
    elif(len(card)==2):      
        if(isRocket(card)):
            return "it is rocket"
        elif(isDouble(card)):
            return "it is double"
    elif(len(card)==4):
        if(isBomb(card)):
            return "it is bomb"
        elif(isThreeWithOne(card)):
            return "it is ThreeWith"
    elif(len(card)>=5):
        if(isOneCardSeq(card)):
            return "it is one card sequence"
        elif(isTwoCardSeq(card)):
            return "it is two cards sequence"
    else:
        return string

# print (isBomb(['♠2', '♠3']))
# print(isLegal(['♠10', '♦9', '♠8', '♠7','♠6']))

# print(isThreeWithOne([2,2,2,4]))
# print(getDeck(number))
def comparison(card):
    tempCard = []
    tempCard = sorted(changeCardToNum(card.copy()))
    if (isThreeWithOne(tempCard)):
        for i in range(len(tempCard)):
            if(tempCard[i]==tempCard[i+1]):
                return (int)(tempCard[i])
    elif(isBomb(tempCard)):
        return (int)(tempCard[0]*10)
    elif(isRocket(tempCard)):
        return 1000000
    else:
        return (int)(tempCard[0])

def isSame(previousCard, currentCard):
    a = isLegal(previousCard)
    b = isLegal(currentCard)
    
    if (isBomb(previousCard) or isBomb(currentCard) or isRocket(previousCard) or isRocket(currentCard)):
        return True
    elif(len(previousCard)==len(currentCard) and (a == b)):
        return True
    return False



    
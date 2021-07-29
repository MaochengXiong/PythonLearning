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
    for i in range(len(card)):
        if(card[i]=="J"):
            card[i]=11
        elif(card[i]=='Q'):
            card[i]=12
        elif(card[i]=='K'):
            card[i]=13
        elif(card[i]=='A'):
            card[i]=14
        elif(card[i]==2):
            card[i]=15
        elif(card[i]=='joker'):
            card[i]=16
        elif(card[i]=='Joker'):
            card[i]=17
    return card

def changeNumToCard(card):
    for i in range(len(card)):
        if(card[i]==11):
            card[i]='J'
        elif(card[i]==12):
            card[i]='Q'
        elif(card[i]==13):
            card[i]='K'
        elif(card[i]==14):
            card[i]='A'
        elif(card[i]==15):
            card[i]=2
        elif(card[i]==16):
            card[i]='joker'
        elif(card[i]==17):
            card[i]='Joker'
    return card

def isSingle(card):
    if(len(card)==1):
        return True
    return False

def isDouble(card):
    if (card[0]==card[1]):
        return True
    return False

def isThreeWithOne(card):
    count = 0
    count2 = 0
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
    for i in range(3):
        if(card[i]==card[3]):
            count = count+1
    if (count==3):
        return True
    return False

def isOneCardSeq(card):
    a = changeCardToNum(card)
    temp = sorted(a)
    for j in range(len(temp)-1):
        if(temp[j]+1!=temp[j+1]):
            return False
    return True

def isTwoCardSeq(card):
    a = changeCardToNum(card)
    if(len(a)%2!=0):
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

    
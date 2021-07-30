def getValuesOfCards(cards):
    values = cards.copy()
    for i in range(len(values)):
        if values[i] == "J":
            values[i] = 11
        elif values[i] == 'Q':
            values[i] = 12
        elif values[i] == 'K':
            values[i] = 13
        elif values[i] == 'A':
            values[i] = 14
        elif values[i] == '2':
            values[i] = 15
        elif values[i] == 'joker':
            values[i] = 16
        elif cards[i] == 'Joker':
            values[i] = 17
        else:
            values[i] = int(cards[i])
    return values


def isSingle(value):
    if len(value) == 1:
        return True
    return False


def isDouble(value):
    if len(value) == 2 and value[0] == value[1]:
        return True
    return False


def isThreeWithOne(value):
    count = 0
    count2 = 0
    if len(value) != 4:
        return False
    for i in range(3):
        if value[i] == value[3]:
            count = count + 1
    for j in range(3):
        if value[1] == value[3 - j]:
            count2 = count2 + 1
    if count == 2 or count2 == 2:
        return True
    return False


def isBomb(value):
    count = 0
    if len(value) != 4:
        return False
    for i in range(3):
        if value[i] == value[3]:
            count = count + 1
    if count == 3:
        return True
    return False


def isOneCardSeq(value):
    temp = sorted(value)
    if len(value) < 5:
        return False
    for j in range(len(temp) - 1):
        if temp[j] + 1 != temp[j + 1]:
            return False
    return True


def isTwoCardSeq(value):
    if len(value) < 6 and len(value) % 2 != 0:
        return False
    temp = []
    temp = sorted(value)
    for j in range(0, len(temp) - 4, 2):
        if temp[j] != temp[j + 1] or temp[j] + 1 != temp[j + 2]:
            return False
    if temp[-1] != temp[-2]:
        return False
    return True


def isRocket(value):
    if len(value) != 2:
        return False
    if value[0] + value[1] != 33:
        return False
    return True


def getTypeOfValues(values):
    string = "it is illegal"
    if isSingle(values):
        return "it is single"
    elif len(values) == 2:
        if isRocket(values):
            return "it is rocket"
        elif isDouble(values):
            return "it is double"
    elif len(values) == 4:
        if isBomb(values):
            return "it is bomb"
        elif isThreeWithOne(values):
            return "it is ThreeWith"
    elif len(values) >= 5:
        if isOneCardSeq(values):
            return "it is one card sequence"
        elif isTwoCardSeq(values):
            return "it is two cards sequence"
    else:
        return string


def isSame(previousValues, currentValues):
    previousType = getTypeOfValues(previousValues)
    currentType = getTypeOfValues(currentValues)

    if isBomb(previousValues):
        return isBomb(currentValues) or isRocket(currentValues)

    if isRocket(previousValues):
        return False

    if len(previousValues) == len(currentValues) and (previousType == currentType):
        return True
    return False


def getPointOfValues(values):
    temp = sorted(values.copy())
    if isThreeWithOne(temp):
        for i in range(len(temp)):
            if temp[i] == temp[i + 1]:
                return int(temp[i])
    elif isBomb(temp):
        return int(temp[0] * 10)
    elif isRocket(temp):
        return 1000000
    else:
        return int(temp[0])

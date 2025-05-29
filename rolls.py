
import random
import dice

def roll(username, diceexpression:str, reason:str):
    try:
        roll = dice.roll(diceexpression)
        result = username + " rolled " + str(diceexpression) 
        if reason:
            result = result + " for " + reason 
        result = result + "\nResult: " + str(roll)
        return result
    except dice.DiceBaseException as e:
        print(e)
        return "Error: " + str(e)

def getDDRoll(rollF:int, rollH:int, modifier:int):
    r = str(rollF) + "F and " + str(rollH) + "H with modifier " + str(modifier) + ", resulting in "
    if rollF == rollH:
        r = r + "a critical hit!"
    else:
        total = rollF + rollH + modifier
        r = r + str(total) + " with "
        if rollF > rollH:
            r = r + "Fear!"
        else:
            r = r + "Hope!"
    return r

def getRRRoll(rollF:int, rollH:int, modifier:int):
    r = str(rollF) + "F and " + str(rollH) + "H with modifier " + str(modifier) + ", resulting in "
    if rollF == rollH:
        r = r + "a critical hit!"
    else:
        total = rollF + rollH + modifier
        r = r + str(total)
    return r

def dd(username, modifier:int):
    try:
        rollF = random.randint(1, 12)
        rollH = random.randint(1, 12)
        result = username + " rolled " + getDDRoll(rollF, rollH, modifier)
        return result
    except dice.DiceBaseException as e:
        print(e)
        return "Error: " + str(e)
    
def rr(username, modifier:int):
    try:
        rollF = random.randint(1, 12)
        rollH = random.randint(1, 12)
        result = username + " rolled " + getRRRoll(rollF, rollH, modifier)
        return result
    except dice.DiceBaseException as e:
        print(e)
        return "Error: " + str(e)
## CIT 591 Lab 3 assignment
## openingBid.py
## Tan, Zhou; Hu, Ruogu


def processHand(hand):
    '''Convert user's hands into detail cards info.'''
    values = {"2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8",
              "9":"9", "10":"10", "J":"Jack", "Q":"Queen", "K":"King", "A":"Ace"}
    suit = {"C":"Club", "D":"Diamond", "H":"Heart", "S":"Spade"}
    splithand = hand.split()
    #cards = [[string1, values1, suit1], ....]
    cards = []                                          
    for i in range(0, 13):
        cards.append([splithand[i]])
        if "10" in cards[i][0]:
            cards[i].append("10")       #'10' has two chars, deal with caution
            cards[i].append(suit[splithand[i][2]])
        else:
            cards[i].append(values[splithand[i][0]])
            cards[i].append(suit[splithand[i][1]])
    return cards

def highCardPoints(hand):
    '''Stats the total high card points based on those from different suits.'''
    return highCardPointsClub(hand) + highCardPointsDiamond(hand) \
           + highCardPointsHeart(hand) + highCardPointsSpade(hand)

def highCardPointsClub(hand):
    '''Stats high card points for Clubs.'''
    cards = processHand(hand)
    jcount = qcount = kcount = acount = 0
    for i in range(13):
        if cards[i][2] == "Club":
            if cards[i][1] == "Jack":
                jcount += 1
            elif cards[i][1] == "Queen":
                qcount += 1
            elif cards[i][1] == "King":
                kcount += 1
            elif cards[i][1] == "Ace":
                acount += 1
            else:
                pass
    return jcount + qcount * 2 + kcount * 3 + acount * 4
             
def highCardPointsDiamond(hand):
    '''Stats high card points for Diamonds.'''
    cards = processHand(hand)
    jcount = qcount = kcount = acount = 0
    for i in range(13):
        if cards[i][2] == "Diamond":
            if cards[i][1] == "Jack":
                jcount += 1
            elif cards[i][1] == "Queen":
                qcount += 1
            elif cards[i][1] == "King":
                kcount += 1
            elif cards[i][1] == "Ace":
                acount += 1
            else:
                pass
    return jcount + qcount * 2 + kcount * 3 + acount * 4    

def highCardPointsHeart(hand):
    '''Stats high card points for Hearts.'''
    cards = processHand(hand)
    jcount = qcount = kcount = acount = 0
    for i in range(13):
        if cards[i][2] == "Heart":
            if cards[i][1] == "Jack":
                jcount += 1
            elif cards[i][1] == "Queen":
                qcount += 1
            elif cards[i][1] == "King":
                kcount += 1
            elif cards[i][1] == "Ace":
                acount += 1
            else:
                pass
    return jcount + qcount * 2 + kcount * 3 + acount * 4

def highCardPointsSpade(hand):
    '''Stats high card points for Spades.'''
    cards = processHand(hand)
    jcount = qcount = kcount = acount = 0
    for i in range(13):
        if cards[i][2] == "Spade":
            if cards[i][1] == "Jack":
                jcount += 1
            elif cards[i][1] == "Queen":
                qcount += 1
            elif cards[i][1] == "King":
                kcount += 1
            elif cards[i][1] == "Ace":
                acount += 1
            else:
                pass
    return jcount + qcount * 2 + kcount * 3 + acount * 4

def suitCount(hand):
    '''Stats the count from different suits.'''
    cards = processHand(hand)
    ccount = dcount = hcount = scount = 0
    for i in range(13): 
        if cards[i][2] == "Club":
            ccount += 1
        elif cards[i][2] == "Diamond":
            dcount += 1
        elif cards[i][2] == "Heart":
            hcount += 1
        elif cards[i][2] == "Spade":
            scount += 1
    return (ccount, dcount, hcount, scount)

def distributionPoints(hand):
    '''Count the distribution points.'''
    count = suitCount(hand)
    distributionpoint = 0
    for i in range(len(count)):
        if count[i] > 4:
            distributionpoint += count[i] - 4
    return distributionpoint

def balancedHand(hand):
    '''Determine if the given hand is balanced.'''
    count = suitCount(hand)
    #if every suit has cards more than 2 and less than 4
    if count[0] in range(2, 5) and count[1] in range(2, 5) \
       and count[2] in range(2, 5) and count[3] in range(2, 5):
        return True
    #for minor suit, 5-3-3-2 is allowed
    elif count[0] == 5 and \
         ((count[1] == 3 and count[2] ==3 and count[3] ==2) or 
          (count[1] == 3 and count[2] ==2 and count[3] ==3) or \
          (count[1] == 2 and count[2] ==3 and count[3] ==3)):
        return True
    elif count[1] == 5 and \
         (
         (count[0] == 3 and count[2] ==3 and count[3] ==2) or \
         (count[0] == 3 and count[2] ==2 and count[3] ==3) or \
         (count[0] == 2 and count[2] ==3 and count[3] ==3)
         ):
        return True
    else:
        return False

def openingBid(hand):
    '''Determine the final bid the player should make.''' 
    count = suitCount(hand)
    highscore = highCardPoints(hand)
    distributionscore = distributionPoints(hand)
    total = highscore + distributionscore
    isbalanced = balancedHand(hand)

    #1NT: Exactly 16-18 high card points, a balanced hand
    if highscore in range(16, 19) and isbalanced:       
        return "1NT"
    #1H: 13-21 points and 5 or more cards in Hearts
    if total in range(13, 22) and (count[2] >=5 or count[3] >=5):     
        if count[2] > count[3]:
            return "1H"
        #1S: 13-21 points and 5 or more cards in Spades
        else:                                           
            return "1S"
    #13-21 points, bid on longer suit
    if total in range(13, 22) and (not isbalanced):       
        if count[0] >= count[1]:                             
            return "1C"
        else:
            return "1D"
    #A balanced hand with 19-20 high card points. Bid the longest minor suit
    if isbalanced and highscore in range(19, 21):         
        #if 3-3, bid Club
        if count[0] > count[1] or (count[0]==3 and count[1]==3):    
            return "1C"
        #if 4-4, bid Diamond
        else:                                               
            return "1D"
    #2NT: Exactly 21-23 high card points and a balanced hand
    if highscore in range(21, 24) and isbalanced:         
        return "2NT"
    if total >= 22:                                       
    #2 of a suit: strong hand (22+ points) with 5 or more cards in some suit
        suittype = []
        for i in range(4):
            if count[i] >= 5:
                suittype.append(i)
        #only 1 suit with 5 or more cards
        if len(suittype) == 1:                              
            if suittype[0] == 0:
                return "2C"
            elif suittype[0] == 1:
                return "2D"
            elif suittype[0] == 2:
                return "2H"
            else:
                return "2S"
        #2 suits with 5 or more cards
        elif len(suittype) == 2:                            
            #1 major suit and 1 minor suit, bid the major suit
            if suittype == [0, 2] or suittype == [1, 2]:    
                return "2H"
            elif suittype == [0, 3] or suittype == [1, 3]:
                return "2S"
            #Club and Diamond
            elif suittype == [0, 1]:                        
                clubpoints = highCardPointsClub(hand)
                diamondpoints = highCardPointsDiamond(hand)
                if clubpoints > diamondpoints:      
                    return "2C"
                elif clubpoints < diamondpoints:
                    return "2D"
                #compare the length of suit
                elif count[0] < count[1]:                   
                    return "2D"
                #if equal, bid on lower-ranking suit
                else:                                       
                    return "2C"
            #Heart and Spade
            else:                                           
                heartpoints = highCardPointsHeart(hand)
                spadepoints = highCardPointsSpade(hand)
                if heartpoints > spadepoints:
                    return "2H"
                if heartpoints < spadepoints:
                    return "2S"
                elif count[2] < count[3]:
                    return "2S"
                else:
                    return "2H"
        #otherwise bid None
        else:                                               
            return None
    #3 of a suit: weak hand (5-9 high card points) with a 7-card suit
    if highscore in range(5, 10):     
        if count[0] == 7:
            return "3C"
        elif count[1] == 7:
            return "3D"
        elif count[2] == 7:
            return "3H"
        elif count[3] == 7:
            return "3S"
        else:
            pass
    #4 of a suit: 6-8 high card points with an 8-card suit 
    if highscore in range(6, 9):     
        if count[0] == 8:
            return "4C"
        elif count[1] == 8:
            return "4D"
        elif count[2] == 8:
            return "4H"
        elif count[3] == 8:
            return "4S"
        else:
            return None        
    return None
    



    

    


    

    
    
    
    

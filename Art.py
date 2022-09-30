def mainMenu():
    return'''
    -----------------------------------------\n      
            Welcome to Love letter     !\n
    -----------------------------------------\n
    Show menu          (type m)\n
    History and Rules  (type rul)\n
    Card action        (type card)\n
    Super Chat         (type chat)\n
    Create room        (type 0)\n
    Join Room          (type room id)\n
    '''

def rules():
    return '''
    __________________________________________________________________

                           L O V E   L E T T E R                      
    __________________________________________________________________ 
                                                                      
                             -- Setup --                             

    We shuffle the 16 cards to form a face-down draw deck. Remove     
    the top card of the deck from the game without looking at it.     
    Each player get one card from the deck. This is the player's      
    hand, and is kept secret from the others.                         


                          -- Object of the Game --                    

    In the wake of the arrest of Queen Marianna for high treason,     
    none was more heartbroken than her daughter, Princess Annette.    
    Suitors throughout the City-State of Tempest sought to ease       
    Annette's sorrow by courting her to bring some joy into her life. 
                                                                      
    You are one of these suitors, trying to get your love letter      
    to the princess. Unfortunately, she has locked herself in the     
    palace, so you must rely on intermediaries to carry your message. 
    During the game, you hold one secret card in your hand. This is   
    who currently carries your message of love for the princess.      
                                                                      
    Make sure that the person closest to the princess holds your      
    love letter at the end of the day, so it reaches her first!       


                          -- Game Play --                             

    Love Letter is played in a series of rounds. Each round           
    represents one day. At the end of each round, one player's        
    letter reaches Princess Annette, and she reads it.                
    When she reads enough letters from one suitor, she becomes        
    enamored and grants that suitor permission to court her.          
    That player wins the princess's heart and the game.               


                          -- Taking a Turn   --            

    On your turn, you get the top card from the deck and add it to    
    your hand. Then choose one of the two cards in your hand and      
    discard it face up in front of you. Apply any effect on the card  
    you discarded. You must apply its effect, even if it is bad       
    for you.                                                          
                                                                      
    All discarded cards remain in front of the player who discarded   
    them. Overlap the cards so that it's clear in which order they    
    were discarded. This helps players to figure out which cards other
    players might be holding. Once you finish applying the            
    card's effect, the turn passes to the player on your left.        


                          -- Out of the Round --      

    If a player is knocked out of the round, that player discards     
    the card in his or her hand face up (do not apply the card's      
    effect) and takes no more turns until next round.                 


                          -- End of a Round -- 

    A round ends if the deck is empty at the end of a turn. The       
    royal residence closes for the evening, the person closest to     
    the princess delivers the love letter, and Princess Annette       
    retires to her chambers to read it.                               
                                                                      
    All players still in the round reveal their hands. The player     
    with the highest ranked person wins the round. In case of a tie,  
    the player who discarded the highest total value of cards wins.   
    A round also ends if all players but one are out of the round,    
    in which case the remaining player wins.                          
    The winner receives a token of affection.                         
    We shuffle all 16 cards together, and play a new round following  
    all of the setup rules.                                           


                          -- End of the game --                       

    A player wins the game after winning a number of tokens based     
    on the server rules.
                                          
    PD: A typing error can cost you dear... so be extremely careful!  
    __________________________________________________________________ 
    __________________________________________________________________
    '''

def card():
    return '''

    -----------------------------------------\n      
                Love letter Cards\n
    -----------------------------------------\n

    Card      ST  #   Effects\n
    
  - Guard      1  5   Player designates another player and names a\n
                      type of card. If that player's hand matches\n
                      the type of card specified, that player is \n
                      eliminated from the round. However, Guard cannot\n
                      be named as the type of card.\n
    
  - Priest     2  2   Player is allowed to see another player's hand.\n
    
  - Baron      3  2   Player will choose another player and privately\n
                      compare hands. The player with the lower-strength\n
                      hand is eliminated from the round.\n
    
  - Handmaid   4  2   Player cannot be affected by any other player's\n
                      card until the next turn.\n
    
  - Prince     5  2   Player can choose any player (including themselves)\n
                      to discard their hand and draw a new one. If the\n
                      discarded card is the Princess, the discarding player\n
                      is eliminated.\n
    
  - King       6  1   Player trades hands with any other player.\n
    
  - Countess   7  1   If a player holds both this card and either the King\n
                      or Prince card, this card must be played immediately.\n
    
  - Princess   8  1   If a player plays this card for any reason, they are \n
                      eliminated from the round.\n
    '''

def welcome_to_super_chat():
    '''Super chat header'''

    return '''
    __________________________________________________________________

                            WELCOME TO SUPER CHAT                      
                            (type 'exit' to leave)
    __________________________________________________________________
    '''

def simbolo():
    print("hey")

#rules()
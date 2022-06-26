import random
from replit import clear
from art import logo
#deals random card from deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #choosing random card from list cards, random.choice is an output and need to save it under a variable and return the value
    card = random.choice(cards)
    return card

    #defining calculate_score with cards as input and return the sum of cards in list
def calulate_score(cards):
    #if statement for getting the sum of 21 in 2 cards...returning 0 indicates either user or computer has blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #if statement to state if 11 in cards makes the sum of cards greater than 21 then remove 11 and replace it with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
#defining a function to figure out situations where the user and computer wins or loses
def compare(user_score, computer_score):
    #if both go over, user loses
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose"
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "Computer wins, Blackjack!"
    elif user_score == 0:
        return "You win, Blackjack!"
    elif user_score > 21:
        return "You lose, you went over!"
    elif computer_score > 21:
        return "Computer loses, they went over"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"
#defining play() to print logo and to put in all conditions of game, meaning when user says yes to game under play() function the user will go though every aspect of the game until they get to the end where it asks if they want to play again
def play():
    print(logo)
    
    user_cards = []
    computer_cards = []
    end_of_game = False
    
       #for loop is used so range can say its running the for loop twice.  Underscore is used because you don't need the variable. 2 cards will be added to blank user_cards list and blank computer_cards list and calculating sum of 2 cards
    for _ in range(2):
            #calling deal_card() and using it to add a new card to the user_cards list...append is used when you want to add a single item to the list
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    #calling calculate_score() after we dealt user and computer cards...user_cards and computer_cards are passed as output of function to get the score of each list of cards dealt
    while not end_of_game:
        user_score = calulate_score(user_cards)
        computer_score = calulate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score {user_score}")
        #print statement only printing 1 random card at a time and square brackets indicates the position of card e.g. [10, 2] 10 is at position zero and 2 is at position 1.
        print(f"Computer's first card: {computer_cards[0]}")
    #if statement determining if either computer or user gets blackjack(0) or if user goes over with initial drawing of the cards
        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_of_game = True
    #else is giving the options if not end of game...inside the while loop the user will continue to get the choices until they say no
        else:
            another_card = input("Type 'y' to get another card or 'n' to pass: ")
            if another_card == "y":
                #when appending we are adding 1 card at a time back through original print statement with user's hand and user's score and updating with new card
                user_cards.append(deal_card())
            else:
                end_of_game = True
#using while loop to update computer cards and score          
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calulate_score(computer_cards)
    #printing final score including any appends from while not end_of_game loop
    print(f"Your final hand is: {user_cards}, final score: {user_score}") 
    #printing computer's final score including appends from while computer_score loop
    print(f"Computer's final hand is: {computer_cards}, final score: {computer_score}") 
    #printing compare function to run through which scenario is true from that function to determine who wins the game
    print(compare(user_score, computer_score))
#calling play() and clear() import to start the game over if user says yes...put in a while loop to keep asking at end of each game
while input("Type 'y' if you want to play Blackjack or 'n' to decline. ") == "y":
    clear()
    play()
            
        
        
        

            

            
                
            
            






















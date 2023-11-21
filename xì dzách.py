
import random 

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,'J'
,'Q', 'K', 'A', 'J','Q', 'K', 'A', 'J','Q', 'K', 'A', 'J','Q', 'K', 'A']


random.shuffle(cards)
#cards[random.randint(0, 52)]



player_card = []
dealer_card = []


player_in = True 
dealer_in = True 


def card_throw(card_have):
    card = random.choice(cards)
    card_have.append(card)
    cards.remove(card)


def total(turn):
    total = 0 
    face = ['J', 'K', 'Q'] # j king queen 
    for card in turn:
        if card in range(1, 11):
            total += card 
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1 
            else:
                total += 11 
    return total 

def reveal_card_dealer():
    if len(dealer_card) == 2:
        return dealer_card[0]
    elif len(dealer_card) > 2:
        return dealer_card[0], dealer_card[1]


for _ in range(3):
    card_throw(dealer_card)
    card_throw(player_card)

#print(dealer_card)
#print(player_card)    


while player_in or dealer_in:
    print(f"dealer has {reveal_card_dealer()} and X" )
    print(f"you have {player_card} and total is {total(player_card)}" )
    if player_in:
        stayorhit = int(input("1: stay or 2: hit"))
    if total(dealer_card) > 16:
        dealer_in = False 
    else:
        card_throw(dealer_card)
    if stayorhit == 1:
        player_in = False
    else:
        card_throw(player_card)
    if total(player_card) >= 21:
        break
    elif total(dealer_card) >= 21:
        break




if total(player_card) == 21:
    print(f" you have {player_card} for a {total(player_card)} and the dealer has {dealer_card} and total of dealer_card is {total(dealer_card)}")
    print('blackjack! you win')

if total(dealer_card) and total(player_card) > 21:
    print("it's a tie")
    

if total(dealer_card) == 21:
    print(f" you have {player_card} for a {total(player_card)} and the dealer has {dealer_card} and total of dealer_card is {total(dealer_card)}")
    print('blackjack! dealer wins')

if total(player_card) > 21:
    print(f" you have {player_card} for a {total(player_card)} and the dealer has {dealer_card} and total of dealer_card is {total(dealer_card)}")
    print('dealer wins because your cards exceed 21')

if total(dealer_card) > 21:
    print(f" you have {player_card} for a {total(player_card)} and the dealer has {dealer_card} and total of dealer_card is {total(dealer_card)}")
    print('you win because dealer_card exceed 21 ')



elif 21 - total(dealer_card) < 21 - total(player_card):
    print(f" you have {player_card} for a {total(player_card)} and the dealer has {dealer_card} and total of dealer_card is {total(dealer_card)}")
    print('dealer wins')

elif 21 - total(dealer_card) > 21 - total(player_card):
    print(f" you have {player_card} for a {total(player_card)} and the dealer has {dealer_card} and total of dealer_card is {total(dealer_card)}")
    print('you win')

elif 21 - total(dealer_card) > 21 - total(player_card) and len(player_card) == 2 and stayorhit == 1 and total(player_card) < 15:
    print(f" you have {player_card} for a {total(player_card)} and the dealer has {dealer_card} and total of dealer_card is {total(dealer_card)}")
    print('you lose because you stay the card too low < 16')

if len(player_card) == 2 and stayorhit == 1 and total(player_card) < 15:
    print("you lose because you stay the card too low < 16")

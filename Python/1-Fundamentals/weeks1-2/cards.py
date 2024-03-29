import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user = input("please pick a card, or Q plus enter to quit")
    if user == "q":
     break

    else:
        random_card = random.choice(diamonds)
        diamonds.remove(random_card)
        hand.append(random_card)

        print("Diamonds Deck:", diamonds)
        print("Your Hand:", hand)

if not diamonds:
    print("There are no more cards to pick.")
   









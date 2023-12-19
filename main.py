from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title('Welcome to War Of Cards!')
root.iconbitmap('cards.ico')
root.geometry("900x550")
root.configure(background="green")

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

deck = []

dealer = []
player = []
dscore = []
pscore = []

# Resize Cards
def resize_cards(card):
    our_card_img = Image.open(card)

    our_card_resize_image = our_card_img.resize((150, 218))

    global our_card_image
    our_card_image = ImageTk.PhotoImage(our_card_resize_image)

    return our_card_image


# Shuffle The Cards
def shuffle():
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')

    dealer_card = random.choice(deck)
    deck.remove(dealer_card)
    dealer.append(dealer_card)
    global dealer_image
    dealer_image = resize_cards(f'cards/{dealer_card}.png')
    dealer_label.config(image=dealer_image)

    player_card = random.choice(deck)
    deck.remove(player_card)
    player.append(player_card)
    global player_image
    player_image = resize_cards(f'cards/{player_card}.png')
    player_label.config(image=player_image)

    root.title(f'{len(deck)} Cards Left')

    score(dealer_card, player_card)


# Deal Out Cards
def deal_cards():
    try:
        dealer_card = random.choice(deck)
        deck.remove(dealer_card)
        dealer.append(dealer_card)
        global dealer_image
        dealer_image = resize_cards(f'cards/{dealer_card}.png')
        dealer_label.config(image=dealer_image)

        player_card = random.choice(deck)
        deck.remove(player_card)
        player.append(player_card)
        global player_image
        player_image = resize_cards(f'cards/{player_card}.png')
        player_label.config(image=player_image)

        score(dealer_card, player_card)

    except:
        if dscore.count("x") == pscore.count("x"):
            root.title(f'Game Over! Tie! {dscore.count("x")} to {pscore.count("x")}')

        elif dscore.count("x") > pscore.count("x"):
            root.title(f'Game Over! Dealer Wins! {dscore.count("x")} to {pscore.count("x")}')

        else:
            root.title(f'Game Over! Player Wins! {pscore.count("x")} to {dscore.count("x")}')


def score(dealer_card, player_card):
    dealer_card = values[dealer_card.split(" ", 1)[0]]
    player_card = values[player_card.split(" ", 1)[0]]


    if dealer_card == player_card:
        score_label.config(text="Tie! Play Again!")

    elif dealer_card > player_card:
        score_label.config(text="Dealer Wins!")
        dscore.append("x")

    else:
        score_label.config(text="Player Wins!")
        pscore.append("x")

    root.title(f'{len(deck)} Cards Left |    Dealer: {dscore.count("x")}     Player: {pscore.count("x")}')


my_frame = Frame(root, bg="green")
my_frame.pack(pady=20)

dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.grid(row=0, column=1, ipadx=20)

dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

score_label = Label(root, text="", font=("Helvetica", 14), bg="green")
score_label.pack(pady=20)

new_game_button = Button(root, text="New Game", font=("Helvetica", 14), command=shuffle)
new_game_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command=deal_cards)
card_button.pack(pady=20)

root.mainloop()
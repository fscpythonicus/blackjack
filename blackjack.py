'''
Blackjack!

A game of blackjack made with Tkinter for CSC1980 and CSC2280's final project.
'''


# Imports #

import random
import tkinter as tk

window = tk.Tk()  # Window must start up here, or nothing else will work

# Game Code #

user_hand = 0  # This is placed outside of the code so each function
# will be able to write to it, without having to define it
# for each individual function.

suits = {
    'Hearts': "♡",
    'Clubs': "♧",
    'Diamonds': "♢",
    'Spades': "♤",
}  # Used for the deck function to differentiate which suit you are drawing
# from for more immersive gameplay


def start():
    global user_hand
    global card_in_hand
    play_again_button.place_forget()  # As a general rule of thumb,
    # I have written "place_forget()" into many lines so it cleans up between
    # the "scenes" so to speak. It makes the game look a lot cleaner!
    draw_button.place(x=370, y=395)
    stop_button.place(x=368, y=425)
    card_value = random.randint(1, 11)
    card_suit = random.choice(list(suits.items()))
    card_name, card_icon = card_suit  # Used to divide the card suits list
    # into individually callable random values that are paired together.
    # In essence, it's so I can make the suits look like this in text: ♡Hearts♡
    card_in_hand = f"{card_value} of {card_icon}{card_name}{card_icon}"
    if card_value > 1 and card_value < 11:  # Between 1 and 11 to prepare for
        # the Ace elif
        text_label.configure(text=f"You have pulled a {card_in_hand}.")
        user_hand += card_value
    elif card_value == 1 or card_value == 11:  # In Blackjack, Aces can be
        # defined as either 1 or 11, so you have to plan for that
        # or else the program won't work.
        text_label.configure(
            text=f"You've pulled an Ace of {card_icon}{card_name}{card_icon}! "
                 f"What would you like this Ace to be read as?")
        ace_1_button.place(x=340, y=335)
        ace_11_button.place(x=440, y=335)
        draw_button.place_forget()
    cards_in_hand.configure(text=f"Current Hand: {user_hand}")  # Adds the
    # current card value to the user's "hand"
    game_state_check()
    start_button.place_forget()


def ace_1():
    global card_value
    global user_hand
    global card_in_hand
    global card_name
    global card_icon
    card_suit = random.choice(list(suits.items()))
    card_name, card_icon = card_suit
    card_value = 1
    text_label.configure(text="The Ace will be read as 1.")
    user_hand += card_value
    cards_in_hand.configure(text=f"Current Hand: {user_hand}")
    ace_1_button.place_forget()
    ace_11_button.place_forget()
    draw_button.place(x=370, y=395)
    if user_hand >= 21:
        game_state_check()


def ace_11():
    global card_value
    global user_hand
    global card_in_hand
    global card_name
    global card_icon
    card_suit = random.choice(list(suits.items()))
    card_name, card_icon = card_suit
    card_value = 11
    card_in_hand = f"{card_value} of {card_icon}{card_name}{card_icon}"
    text_label.configure(text="The Ace will be read as 11.")
    user_hand += card_value
    cards_in_hand.configure(text=f"Current Hand: {user_hand}")
    ace_1_button.place_forget()
    ace_11_button.place_forget()
    draw_button.place(x=370, y=395)
    if user_hand >= 21:
        game_state_check()


def draw():  # Despite this function being simple,
    # it's used to separate the "Play" and "Draw Card" buttons into
    # different functions.
    global user_hand
    if user_hand < 21:
        start()
    game_state_check()


def game_state_check():  # This function makes it easier to handle win and
    # loss states for both the start and draw functions.
    # Before I added this, I had to implement it into both.
    # Separating it cleaned up the aforementioned functions
    # and made my life easier, so to speak.
    global card_in_hand
    if user_hand == 21:
        text_label.configure(text=f"You have pulled a {card_in_hand}. "
                             f"Congratulations, you win!")
        start_button.place_forget()
        draw_button.place_forget()
        play_again_button.place(x=372, y=315)
    elif user_hand > 21:
        text_label.configure(text=f"You have pulled a {card_in_hand}. "
                             f"Bust! Your ending value was {user_hand}.")
        start_button.place_forget()
        draw_button.place_forget()
        play_again_button.place(x=372, y=315)


def play_again():  # Provides a clean slate for the user to begin a new game.
    global user_hand
    user_hand = 0
    cards_in_hand.configure(text=f"Current Hand: {user_hand}")
    play_again_button.pack_forget()
    start()


def play():
    play_button.place_forget()
    quit_button.place(x=725, y=550)
    blackjack_label.place(x=314, y=18)
    blackjack_label.configure(font=("Arial", 18))
    hand_label.place(x=50, y=20)
    cards_in_hand.place(x=50, y=45)
    text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    # This is formatted so the text will remain in the center of the screen at
    # all times, instead of being off-center when the textbox changes.
    start_button.place(x=385, y=315)


def stop():
    global user_hand
    user_hand = 0
    text_label.configure(text="Click 'Start' to begin")
    cards_in_hand.configure(text="Current Hand: 0")
    for widget in window.winfo_children():  # Just a for loop to remove all
        # the widgets from the screen.
        widget.place_forget()
    blackjack_label.configure(font=("Arial", 25))  # Below lines replace the
    # labels and buttons. It was easier to do this than to
    # # delete every individual widget.
    blackjack_label.place(x=283, y=175)
    play_button.place(x=321, y=350)
    quit_button.place(x=421, y=350)


# Window Properties #
# You have to place most of the things below after the game code so it can #
# refer back to the code and call upon it. #


blackjack_label = tk.Label(text="Blackjack", height=2, width=12, bg="black",
                           fg="white", font=("Arial", 25))
hand_label = tk.Label(text="Player Hand")
cards_in_hand = tk.Label(text=f"Current Hand: {user_hand}")
text_label = tk.Label(text="Click 'Start' to begin")  # The default value is
# set like this because this is the first text the user will see in any game.

ace_1_button = tk.Button(text="1", command=ace_1)
ace_11_button = tk.Button(text="11", command=ace_11)
play_button = tk.Button(text="Play", command=play, height=2, width=7)
quit_button = tk.Button(text="Quit", command=exit, height=2, width=7)
start_button = tk.Button(text="Start", command=start)
draw_button = tk.Button(text="Draw Card", command=draw)
stop_button = tk.Button(text="Stop Game", command=stop)
play_again_button = tk.Button(text="Play Again", command=play_again)

blackjack_label.place(x=283, y=175)
play_button.place(x=318, y=350)
quit_button.place(x=418, y=350)

window.geometry("800x600")  # Predetermined window size
window.configure(bg="#313136")  # Sets background color
window.resizable(False, False)  # Makes it so the window cannot be resized
window.mainloop()

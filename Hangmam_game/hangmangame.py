import random
import hangman_images
import hints
# word_list=['apple','orange','mango']
lives=6
chosen_word=random.choice(hints.words)
print(chosen_word)
display=[]
for i in chosen_word:
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives>0:
            print(f"You only have {lives} lives.")
        else:
            game_over=True
            print("You lose.")
    if '_' not in display:
        game_over=True
        print("You won.")
    print(hangman_images.stages[lives])

import random
from hangman_art import logo, stages
from hangman_words import word_list



print(logo)
word_list = word_list
chosen_word = ""

display = []
chosen_word = random.choice(word_list)

for letter in chosen_word:
    display.append("_")

lives = 6
end_of_game = False
while not end_of_game:
 
  guess = input("Gess a letter: ").lower()

  if guess in display:
    print(f"You have alredy guessed {guess}")
  print()
  position = 0
  
  for letter in chosen_word:
      if guess == letter:
        display[position] = guess 
          
      position +=1
  if guess not in chosen_word:
    lives-=1
    print(f"you guessed {guess}, that's not in the word. You lose a life")
    
  print(display)

  if lives ==0:
    print("\n\nyou lose")
    print(f"The chosen word was {chosen_word}")
    end_of_game = True
  if "_" not in display:
      end_of_game = True
      print("you win")
  print(stages[lives])
      



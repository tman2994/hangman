import random
import words 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lifes = 6
choosen_word = random.choice(words.word_list) 
display = []
blank = '_'
end_of_game = False

for i in range(len(choosen_word)): 
        display  += '_'

print(display)

while end_of_game == False:
    choosen_letter = input("please choose letter:")

    if choosen_letter in display:
        print('you have already guess this letter')

    for i in range(len(choosen_word)):
        letter = choosen_word[i]
        if letter in  choosen_letter:
            print("you were correct")
            display[i] = choosen_letter
            print(display)
   
    if choosen_letter not in choosen_word:
            lifes -= 1
            #stages[9] -= stages[0]
            print("you where wrong")
            print(stages[lifes])



    if blank not in display[:]:
          end_of_game = True
          print('you have won')

    if lifes == 0: 
        print('you lose')
        end_of_game = True
          



'''for i in range(len(choosen_word)):
     if display[1] in display:
        display.pop()
        print(display)'''
#for i in range(len(choosen_word)): 
#        blank  += '_'
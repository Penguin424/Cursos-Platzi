# -*- econde: utf-8 -*-

import random as rd


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
        |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
    |   |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|   |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
        ==========''','''

    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
        ==========''','''
''']

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]

def random_word():
    num = rd.randint(0, (len(WORDS) - 1))
    word = WORDS[num]

    return word

def display_board(h, t):
    print('{}\n'.format(IMAGES[t]))
    print('{}\n'.format(h))
    print('--- * --- * --- * --- * --- * ---\n')

def run():

    result_word =  random_word()
    hiden_word = ['-'] * len(result_word)
    tires = 0

    while True:
        display_board(hiden_word, tires)
        current_letter = str(input('Escoje una letra: '))

        letter_indexes = []
        for i in range(len(result_word)):
            if result_word[i] == current_letter:
                letter_indexes.append(i)
                
        
        if len(letter_indexes) == 0:
            tires += 1

            if tires == 6:
                display_board(hiden_word, tires)
                print('\n Perdiste :( la plabara era {}\n'.format(result_word))

                break

        else:
            for idx in letter_indexes:
                hiden_word[idx] = current_letter
            
            letter_indexes = []

        try:
            hiden_word.index('-')
        except ValueError:
            display_board(hiden_word, tires)
            print('¡Felicidades! Ganaste. La palabra es: {}'.format(result_word))
            break

if __name__ == "__main__":
    print('\n\nB I E N V E N I D O S  A  A H O R C A D O S\n\n')
    run()
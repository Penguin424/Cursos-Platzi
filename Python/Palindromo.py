# -*- coding:utf-8 -*-

def palindrome2(p):
    reversed_p = p[:: -1]

    if reversed_p == p:
        return True
    
    return False

def palindrome(p):
    reversed_letters = []

    for i in p:
        reversed_letters.insert(0, i)

    reversed_word =  ''.join(reversed_letters)

    if p == reversed_word:
        return True


    return False

if __name__ == "__main__":
    word = str(input('Escribe una palabra: '))

    result = palindrome2(word)

    if result:
        print('La palabra {} es un palindromo'.format(word))
    else:
        print('La palabra {} no es un palindromo'.format(word))
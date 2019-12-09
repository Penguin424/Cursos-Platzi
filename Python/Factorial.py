# -*- econde: utf-8 -*-

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    number = int(input('Escribe un numero y te dire su facotrial: '))
 
    result = factorial(number)

    print(result)
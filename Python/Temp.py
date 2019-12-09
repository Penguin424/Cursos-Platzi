# -*- coding:utf-8 -*-

def average_temps(t):
    sum_of_temps = sum(t)

    return( sum_of_temps/len(t) )

if __name__ == "__main__":
    temp = [21, 24, 24, 22, 20, 23, 24]

    result = average_temps(temp)

    print('La temperatura promedio es de {}'.format(result))
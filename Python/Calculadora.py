# -*- econde: utf-8 -*-

def foreing_exchange_calculator(c):
    mex_to_usd = .052

    return mex_to_usd * c

def run():
    print('C A L C U L A D O R A D E D I V I S A S')
    print('Convierte pesos mecixanos a dolares. \n')

    ammount = float(input('Ingresa la cantidad en pesos mexicanos que deseas comvertir: '))
    result = foreing_exchange_calculator(ammount)

    print('{} pesos mexicanos son {} dolares'.format(ammount, result))



if __name__ == "__main__":
    run()
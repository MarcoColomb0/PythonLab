#!/usr/bin/env python3

def main():
    print('Che calcolo vuoi fare?\n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\nq. Esci')
    while True:
        job = input('Selezione: ')
        if job in ('1', '2', '3', '4'):
            num1 = float(input('Inserisci il primo numero: '))
            num2 = float(input('Inserisci il secondo numero: '))
            if job == '1':
                print(num1, '+', num2, '=', num1 + num2)
            elif job == '2':
                print(num1, '-', num2, '=', num1 - num2)
            elif job == '3':
                print(num1, '*', num2, '=', num1 * num2)
            elif job == '4':
                print(num1, '/', num2, '=', num1 / num2)
        elif job == 'q':
            break
        else:
            print('La selezione non è valida.\n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\nq. Esci')


# Execute
if __name__ == '__main__':
    main()

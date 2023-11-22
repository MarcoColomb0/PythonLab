#!/usr/bin/env python3
# Dependencies
import os

# Main function
def main():
    while True:
        # Lista dei calcoli supportati
        print('\nChe calcolo vuoi fare?\n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\nq. Esci')
        # Richiesta del calcolo da eseguire all'utente
        job = input('Selezione: ')
        # Pulizia shell con check di compatibilità
        os.system('cls' if os.name == 'nt' else 'clear')
        # Richiesta numeri con controllo errori
        if job in ('1', '2', '3', '4'):
            try:
                num1 = float(input('Inserisci il primo numero: '))
                num2 = float(input('Inserisci il secondo numero: '))
            except ValueError:
                print('Input non valido, inserisci un numero valido.\n')
                continue
            # Operazioni matematiche
            if job == '1':
                print(num1, '+', num2, '=', num1 + num2, '\n')
            elif job == '2':
                print(num1, '-', num2, '=', num1 - num2, '\n')
            elif job == '3':
                print(num1, '*', num2, '=', num1 * num2, '\n')
            elif job == '4':
                try:
                    result = num1 / num2
                    if num2 != 0:
                        print(num1, '/', num2, '=', result, '\n')
                    else:
                        print('Non puoi dividere per zero.\n')
                except ZeroDivisionError:
                    print('Non puoi dividere per zero.\n')
        # Quit script
        elif job == 'q':
            break
        # Errore in caso di selezione non valida
        else:
            print('La selezione non è valida.\n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\nq. Esci')


# Execute
if __name__ == '__main__':
    main()
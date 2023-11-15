#!/usr/bin/env python3

# Main function
def main():
    # Lista dei calcoli supportati
    print('Che calcolo vuoi fare?\n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\nq. Esci')
    while True:
        # Richiesta del calcolo da eseguire all'utente
        job = input('Selezione: ')
        if job in ('1', '2', '3', '4'):
            # Richiesta dei due numeri all'utente
            num1 = float(input('Inserisci il primo numero: '))
            num2 = float(input('Inserisci il secondo numero: '))
            # Somma
            if job == '1':
                print(num1, '+', num2, '=', num1 + num2)
            # Sottrazione
            elif job == '2':
                print(num1, '-', num2, '=', num1 - num2)
            # Moltiplicazione
            elif job == '3':
                print(num1, '*', num2, '=', num1 * num2)
            # Divisione
            elif job == '4':
                print(num1, '/', num2, '=', num1 / num2)
        # Quit script
        elif job == 'q':
            break
        # Errore in caso di selezione non valida
        else:
            print('La selezione non è valida.\n1. Somma\n2. Sottrazione\n3. Moltiplicazione\n4. Divisione\nq. Esci')


# Execute
if __name__ == '__main__':
    main()

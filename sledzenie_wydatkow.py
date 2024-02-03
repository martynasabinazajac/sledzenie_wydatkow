months={1:'Styczeń', 2:'Luty', 3:'Marzec', 4:'Kwiecień', 5:'Maj', 6:'Czerwiec', 7:'Lipiec', 8:'Sierpień', 9:'Wrzesień', 10: 'Październik', 11:'Listopad', 12: 'Grudzień'}
date={1:{'rachunki': 220,'jedzonko dla psów': 250}, 2:{'rachunki': 150, 'jedzonko dla psów': 130, 'wycieczka': 2500 }}


def expand_list(choosen_month):
    print('--------------------------------')
    print('Twoje wydatki:')
    for key,value in choosen_month.items():
        print(f'{key}:{value}')

def add_expenses(choosen_month):
    new_expenses=str(input('Wprowadź nazwę nowego wydatku: '))
    while True:
        try:
            cost=int(input('Wprowadź kwotę nowego wydatku: '))
            choosen_month[new_expenses]=cost
            break
        except ValueError:
            print('Podana wartość nie jest liczbą')

def delete_expenses(choosen_month):
        delete_expenses=str(input('Wpisz nazwę wydatku jaki ma zostać usuniety z listy dla wybranego miesiąca: '))
        if delete_expenses in choosen_month:
            choosen_month.pop(delete_expenses)
        else:
            print('Brak podanego wydatku.')


def expenses(month, month_name, expenses_list):
    if month not in expenses_list:
        print('Dla wskazanego miesiąca nie zostały wprowadzone dane. Lista jest pusta. W dalszych krokach możesz dodać wydatki.')
        expenses_list[month]={}
    choosen_month=expenses_list[month]
    while True:
        try:
            print('--------------------------------')
            print(f'Wybrany miesiąc: {month_name}')
            menu_list=int(input('Wybierz numer z menu.\n 0 - wyjdź z aplikacji.\n 1 - Pokaż wszystkie wydatki danego miesiąca.\n 2 - dodaj wydatek do wybranego miesiąca.\n 3 - usuń wydatek z wybranego miesiąca.\n Wybrana liczba: ' ))
            if menu_list == 0:
                exit('Wychodzimy z aplikacji.')
            elif menu_list == 1:
                expand_list(choosen_month)
            elif menu_list==2:
                add_expenses(choosen_month)
            elif menu_list == 3:
                delete_expenses(choosen_month)
            else:
                print('Wybrano wartość z pozalisty. Wybierz ponownie.')
        except ValueError:
            print('Wprowadzono niepoprawną wartość.')



while True:
    try:
        month=int(input('Wybierz miesiąc-wprowadź liczbę od 1-12. Jeżei chcesz wyjść wpisz 0: '))
        if  month < 0 or month > 12:
            print('Wybraeś nie poprawny numer. Wybierz jeszcze raz.')
        elif month == 0:
            exit('Wychodzimy')
        else:
            month_name=months[month]
            print(f'Wybrałeś miesiąc: {month_name}')
            expenses(month, month_name, date)
    except ValueError:
        print('Wprowadziłeś nie poprawne dane. Wprowadzone dane powinny być liczbą.')


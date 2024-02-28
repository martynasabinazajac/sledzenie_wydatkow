months={1:'Styczeń', 2:'Luty', 3:'Marzec', 4:'Kwiecień', 5:'Maj', 6:'Czerwiec', 7:'Lipiec', 8:'Sierpień', 9:'Wrzesień', 10: 'Październik', 11:'Listopad', 12: 'Grudzień'}

all_expenses={1:[("prąd", "rachunki", 250), ("karma sucha", "wydatki na pieski", 150)]}
expenses_data=("expense_name", "expense_type", "expense_cost")

def expand_list(choosen_month):
    print('--------------------------------')
    print('Twoje wydatki:')
    for date in choosen_month:
        print(f'{expenses_data[0]}:{date[0]}, {expenses_data[1]}:{date[1]}, {expenses_data[2]}:{date[2]}')

def add_expenses(choosen_month, add_new_expenses):
    choosen_month.append(add_new_expenses)

def delete_expenses(choosen_month, index_of_the_delete_expense):
    choosen_month.pop(index_of_the_delete_expense)



def expenses(month, month_name, expenses_list):
    if month not in expenses_list:
        print('Dla wskazanego miesiąca nie zostały wprowadzone dane. Lista jest pusta. W dalszych krokach możesz dodać wydatki.')
        expenses_list[month]=[]
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
                expense_name=input('Wprowadź nazwę nowego wydatku: ')
                expense_type=input('Wprowadź typ nowego wydatku: ')
                while True:
                    try:
                        expense_cost=int(input('Wprowadź kwotę nowego wydatku: '))
                        break
                    except ValueError:
                        print('Podana niepoprawną wartość dla kwoty.')
                add_new_expenses=(expense_name, expense_type, expense_cost)
                add_expenses(choosen_month, add_new_expenses)
            elif menu_list == 3:
                expense_name=str(input('Wpisz nazwę wydatku jaki ma zostać usuniety z listy dla wybranego miesiąca: '))
                expense_found = False
                for delete_expense in choosen_month:
                    if expense_name == delete_expense[0]:
                        index_of_the_delete_expense = choosen_month.index(delete_expense)
                        print(choosen_month[index_of_the_delete_expense])
                        delete_expenses(choosen_month, index_of_the_delete_expense)
                        expense_found = True
                if not expense_found:
                    print('Brak podanego wydatku.')     
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
            expenses(month, month_name, all_expenses)
    except ValueError:
        print('Wprowadziłeś nie poprawne dane. Wprowadzone dane powinny być liczbą.')


from _datetime import datetime

date_format="%d-%m-%Y"
CATEGORIES={"I": "Income",
            "E": "Expense"}
def get_data(prompt, allow_default=False):
    """
    Primi data de la utilizator ,
    Daca vrem data de azi apasam enter
    De asta folosim allow_default = False

    """
    date_string=input(prompt)
    if allow_default and not date_string:
        return datetime.today().strftime(date_format)
    try:#validam data ca sa fie d-m-y
        Valid_date=datetime.strptime(date_string, date_format)
        return Valid_date.strftime(date_format)
    except ValueError:
        print("Date invalide. Enter dd/mm/yyyy")
        return get_data(prompt, allow_default)

def get_amout():
    """
    Cerem utilizatorului sa dea detalii despre suma de bani
    Cerinte sunt ca sa fie positiv
    :return: amount
    """
    try:
        amount=float(input('enter the amount :'))
        if amount <= 0:
            raise ValueError('amount must be positive')
        return amount
    except ValueError as e:
        print(e)
        return get_amout()

def get_category():
    """
    Cerem categoria I sau E
    Folosim un dictionary pentru a accesa datele cand selectam I sau E

    :return: I -> Income
            E-> Expense
    """
    category=input("enter the category ('I' for income or 'E' for expense ) : ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Category invalide. Enter 'I' for income or 'E' for expense")
    return get_category()


def get_description():
    return input("enter the description : ")
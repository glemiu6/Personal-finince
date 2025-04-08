from _datetime import datetime

date_format="%d-%m-%Y"
CATEGORIES={"I": "Income",
            "E": "Expense"}
def get_data(prompt, allow_default=False):
    """
    Get date from user ,
    If we want today's date we press enter
    That's why we use allow_default = False

    """
    date_string=input(prompt)
    if allow_default and not date_string:
        return datetime.today().strftime(date_format)
    try:#we validate the date to be d-m-y
        Valid_date=datetime.strptime(date_string, date_format)
        return Valid_date.strftime(date_format)
    except ValueError:
        print("Date invalide. Enter dd/mm/yyyy")
        return get_data(prompt, allow_default)

def get_amout():
    """
    We ask the user to provide details about the amount of money
    Requirements are to be positive
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
    We are asking for category I or E
    We use a dictionary to access the data when we select I or E
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
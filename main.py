
import pandas as pd
import csv
from datetime import datetime
from data_entry import get_data, get_amout,get_category,get_description
from matplotlib import pyplot as plt
class CSV:
    CSV_FILE= "finance_data.csv"
    COLOMNS=['Date','Amount','Category','Descriptions']
    FORMAT='%d-%m-%Y'
    @classmethod #trebuie sa mai revad asta ce face
    def initiere_csv(cls):
        """
        initializam csv_file pentru a fi pregatit
        citim fisierul daca exista sau creem fisierul daca nu exista

        """
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.COLOMNS)
            #DataFrame ne ajuta sa accesam mai usor coloane si randuri din csv
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls,Data,Amount,Category,Descriptions):
        """
        adaugam datele necesare in csv_file
        :param Data:
        :param Amount:
        :param Category:
        :param Descriptions:
        :return:
        """
        new_entry={
            'Date':Data,
            'Amount':Amount,
            'Category':Category,
            'Descriptions':Descriptions
        }
        with open(cls.CSV_FILE, 'a',newline="") as csvfile:
            writer=csv.DictWriter(csvfile, fieldnames=cls.COLOMNS)
            writer.writerow(new_entry)
        print('Added successfully')


    @classmethod
    def get_transactions(cls,start_date,end_date):
        df=pd.read_csv(cls.CSV_FILE)
        df['Date']=pd.to_datetime(df['Date'],format=CSV.FORMAT)#facem din formatul string in formatul date time object
        start_date=datetime.strptime(start_date,CSV.FORMAT)
        end_date=datetime.strptime(end_date,CSV.FORMAT)
        #Creem o masca pentru a vedea daca trebuie sa luam sau nu in considerare
        mask=(df['Date']>=start_date) & (df['Date']<=end_date)
        filtered_df=df.loc[mask]

        if filtered_df.empty:
            print('No transactions found')

        else:
            print(f'Transactions found {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}')
            print(filtered_df.to_string(index=False,formatters={'Date':lambda x:x.strftime(CSV.FORMAT) }))

            total_income=filtered_df[filtered_df['Category']=='Income']['Amount'].sum()
            total_expense=filtered_df[filtered_df['Category']=='Expense']['Amount'].sum()
            print("\nSummary:")
            print(f'Total Income: {total_income:.2f}')
            print(f'Total Expense: {total_expense:.2f}')
            print(f'\nSavings:{(total_income-total_expense):.2f}')
        return filtered_df

def add():
    """
    Acesta functioe initializeaza csv
    Apoi ia datele necesare de la utilizator si le stocheaza in file

    """
    CSV.initiere_csv()
    date=get_data("enter the date of the transaction dd-mm-yyyy or for today press enter ", allow_default=True)
    amount=get_amout()
    category=get_category()
    description=get_description()
    CSV.add_entry(date,amount,category,description)

def plot_trans(df):
    df.set_index('Date',inplace=True)
    income =df[df["Category"]=='Income'].resample('D').sum().reindex(df.index,fill_value=0)
    expance=df[df["Category"]=='Expense'].resample('D').sum().reindex(df.index,fill_value=0)
    plt.figure(figsize=(10,5))
    plt.plot(income.index,income['Amount'],label='Income',color='blue')
    plt.plot(expance.index,expance['Amount'],label='Expense',color='red')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Income and Expense over time')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    while True:
        print('\n1. ADD TRANSACTIONS')
        print('2. View transactions and sumerry with date range')
        print('3. Exit')
        choise=int(input('Enter a choise :'))

        if choise==1:
            add()
        elif choise==2:
            start=get_data("Enter the start date (dd-mm-yyyy)")
            end=get_data("Enter the end date (dd-mm-yyyy)")
            df=CSV.get_transactions(start,end)
            if input('Do you want to see the graph (y/n)?').lower()=='y':
                plot_trans(df)
        elif choise==3:
            print('Exit')
            break
        else:
            print('Invalid input')

if __name__ == '__main__':
    main()
# Personal Finance Tracker

---
### Objectives : Keeping track of your finances  
### Author: Vlad Digori
## Summary
 
 - [Environment](#setting-up-the-environment)
 - [About the code](#about-the-code)
 
---
##  Setting up the Environment:
Install [Python](https://www.python.org/downloads/) IDLE.  

Now we create a virtual environment so we can run the code.  

### 1. Creating the environment:
```bash
python -m venv venv
```
### 2. Activating the environment:
#### For Mac/Linux:

```bash
source venv/bin/activate
```
#### For Windows:
```bash
.\venv\Scripts\activate
```
### 3. Installing all the necessary libraries to run the project:
```bash
pip install -r requirements.txt
```
### 4. Go to the program directory:
```bash
cd Code
```
### 5. Running the program
```bash
python main.py
```
or
```bash
python3 main.py
```
### 6. Closing the environment:
```bash
deactivate
```

---

## About the code

We created a python file named [data_entry.py](https://github.com/glemiu6/Personal-finance/blob/master/Code/data_entry.py).  
We create a `date_format` , this is how the date will look. After that we initiate a dictionary with the keys `I`(income) and `E`(expense).   
We have a function called `get_data` with a parameter prompt(the date ) and a default parameter = `False`(use this is we want to get today's date).   
The function `get_amount` is used to get the amount spent or gain.  
The function `get_caegory` asks the user to indicate the category `I/E` where we can access it from the dictionary.  
And a final function called `get_description` where we can enter a description about the money spent or gain.

We also created a file named [main.py]() where the main program runs. 

- The CSV Class

This class handles everything related to the CSV file: creating it, writing data, reading/filtering data.

`CSV.initiere_csv()`  
	•	Checks if the CSV file (finance_data.csv) exists.  
	•	If not, it creates a new one with columns: Date, Amount, Category, Descriptions.  

`CSV.add_entry(date, amount, category, description)`  
	•	Takes a transaction and appends it to the CSV.  
	•	Uses csv.DictWriter to write a new row in the file.  

`CSV.get_transactions(start_date, end_date)`  
	•	Reads the CSV file using pandas.  
	•	Converts the “Date” column to actual date objects.  
	•	Filters transactions between start_date and end_date.  
	•	Prints the filtered data in a nice format.  
	•	Calculates and prints:  
	•	Total Income  
	•	Total Expense  
	•	Savings = Income - Expense  
	•	Returns the filtered data (used later for plotting).  

- add() Function

This is the entry point to add a new transaction. It:
	•	Ensures the CSV is initialized  
	•	Gets user input (via functions from data_entry.py)  
	•	Adds the entry to the file using CSV.add_entry(...)  

- plot_trans(df) Function  
	•	Takes the filtered transactions (df)  
	•	Resamples the data per day  
	•	Plots two lines:  
	•	Blue = Income   
	•	Red = Expense  
	•	Uses matplotlib to show trends over time  


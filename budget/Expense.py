
from datetime import datetime
from dataclasses import dataclass
from collections import Counter

import csv

@dataclass(unsafe_hash=True)
class Expense:

    date_time:datetime
    vendor:str
    category:str
    amount:float

class Expenses:
    def __init__(self):
        self.list = []
        self.sum = 0

    def read_expenses(self, filename):

        with open(filename, "r") as file:
            csv_reader = csv.reader(file, delimiter="," )
            for row in csv_reader:
                amount = float(row[3][2:].replace(",", ""))
                converted_date = datetime.strptime(row[0], "%m/%d/%Y %H:%M:%S")
                self.list.append(Expense(converted_date, row[1], row[2], amount))
                self.sum += amount

    def categorize_for_loop(self):

        necessary_expenses_list = ["Phone", "Auto and Gas", "Classes", "Utilities", "Mortgage"]
        food_expenses_list = ["Groceries", "Eating Out"]
        necessary_expenses = set()
        food_expenses = set()
        unnecessary_expenses = set()

        for i in self.list:
           
            if i.category in necessary_expenses_list:
                necessary_expenses.add(i)
            elif i.category in food_expenses_list:
                food_expenses.add(i)
            else:
                unnecessary_expenses.add(i)
       
        return [necessary_expenses, unnecessary_expenses, food_expenses]


  
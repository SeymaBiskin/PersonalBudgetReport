import Expense
from collections import Counter

def main():

    category_list = []

    expenses = Expense.Expenses()
    expenses.read_expenses("../data/spending_data.csv")
    divided_for_loop = expenses.categorize_for_loop()
    

    for expense_set in divided_for_loop:
        for expense in expense_set:
            category_list.append(expense.category)
    
    spending_categories = Counter(category_list)
    print(spending_categories)
   




if __name__ == "__main__":
    main()
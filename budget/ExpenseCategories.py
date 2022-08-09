import Expense
from collections import Counter
import matplotlib.pyplot as plt

category_list = []
top_five_list = {}

def main():

    def plot_data_as_bar(*args):
        fig, ax = plt.subplots()
        ax.bar(*args)
        ax.set_title("# of Purchases by Category")
        plt.show()


    expenses = Expense.Expenses()
    expenses.read_expenses("../data/spending_data.csv")
    divided_for_loop = expenses.categorize_for_loop()
    

    for expense_set in divided_for_loop:
        for expense in expense_set:
            category_list.append(expense.category)
    
    spending_counter = Counter(category_list)
    top5 = spending_counter.most_common(5)
    categories, count = zip(*top5)

    plot_data_as_bar(categories, count)

   

if __name__ == "__main__":
    main()
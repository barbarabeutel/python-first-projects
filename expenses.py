
total=0
expenses =[]
num_expenses = int(input("Enter the number of expenses:\n"))
for expense in range(num_expenses):
    expenses.append(float(input("Please, type your expenses pressing enter each time:")))

total = sum(expenses)
print("This month you've spent $", total," so far.", sep='')
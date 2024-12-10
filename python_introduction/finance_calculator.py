# personal finance calculator program
# designed to calculate the annual saving money with statis interes 5%

# ask user for his monthly income
monthly_income = input ("Enter your monthly income: ")

# ask user for his monthly expenses
monthly_expenses = input ("Enter your total monthly expenses: ")

# substract the incom from the expenses
monthly_savings =float ( monthly_income) - float (monthly_expenses)

monthly_savings = int (monthly_savings)

# display monthly saving
print ("Your monthly savings are $" +str ( monthly_savings)+".")

# annual saving with interest 5%
projected_saving = int (( monthly_savings * 12 + (monthly_savings * 12 * 0.05)))

# display the annual saving with interest
print (f"Projected savings after one year, with interest, is: ${projected_saving}.")

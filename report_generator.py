import csv
import calendar
from transaction import Transaction, Income, Savings, Expense
monthDict = {'01':'January', '02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}

def groupByMonth(listOfTransactions):
    monthYearDict = {}
    for transaction in listOfTransactions:
            month = monthDict[transaction.date[3:5]]
            year = transaction.date[6:10]
            if month+year in monthYearDict.keys():
                monthYearDict[month+year].append(transaction)
            else:
                monthYearDict[month+year] = [transaction]
    
    def sort_key(key):
        # Extract month name and year from the key
        month_name = key[:-4]  # Everything except the last 4 characters
        year = int(key[-4:])  # Last 4 characters as the year

        # Convert month name to numeric value
        month_num = list(calendar.month_name).index(month_name)
        return (year, month_num)  # Sort by year first, then month

    # Sort the dictionary keys
    sorted_keys = sorted(monthYearDict.keys(), key=sort_key)

    # Create a new dictionary with sorted keys
    sorted_dict = {key: monthYearDict[key] for key in sorted_keys}
    return sorted_dict

def generateReport(monthYearDict):
    report = {}
    for monthYear, transactions in monthYearDict.items():
        totalIncome = 0
        totalExpenses = 0
        totalSavings = 0
        for transaction in transactions:
            if isinstance(transaction, Income):
                totalIncome += transaction.amount
            if isinstance(transaction, Expense):
                totalExpenses += transaction.amount
            if isinstance(transaction, Savings):
                totalSavings += transaction.amount
        report[monthYear] = [totalIncome, totalExpenses, totalSavings]
    
    return report

def goalGenerator(listOfTransactions):
    goals = {}
    for transaction in listOfTransactions:
        if isinstance(transaction, Savings):
            if transaction.goal in goals.keys():
                goals[transaction.goal][1] += transaction.amount
            else:
                goals[transaction.goal] = [transaction.target_amount, transaction.amount]
    return goals

def categorize(listofTransactions):
    categoryTotal = {}
    for transaction in listofTransactions:
        if isinstance(transaction, Expense):
            if transaction.category in categoryTotal:
                categoryTotal[transaction.category] += transaction.amount
            else:
                categoryTotal[transaction.category] = transaction.amount
    return categoryTotal

def saveToCSV(username, listOfTransactions):
    monthYearDict = groupByMonth(listOfTransactions)
    report = generateReport(monthYearDict)
    categoryExpenses = {}
    goalDict = goalGenerator(listOfTransactions)
    for monthYear, transactions in monthYearDict.items():
        categoryExpenses[monthYear] = categorize(transactions)

    with open(f"{username}/monthlyreport.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        categories = list(set(cat for month in categoryExpenses.values() for cat in month))
        #goals = list(set(goal for month in goalDict.values() for goal in month))
        header = ["Month-Year", "Total Income", "Total Expenses", "Balance", "Total Savings", "Expenses:"] + categories
        writer.writerows([header,[]])

        for monthYear, totals in report.items():
            row = [monthYear,
                   totals[0],
                   totals[1],
                   totals[0]-totals[1]-totals[2],
                   totals[2],
                   ''
                   ]
            for category in categories:
                row.append(categoryExpenses.get(monthYear, {}).get(category, 0))
            writer.writerow(row)
        writer.writerows([[],[],["Savings","Target Amount","Amount Saved","Progress"],[]])
        for goal in goalDict:
            row = [goal,goalDict[goal][0],goalDict[goal][1], str(round(goalDict[goal][1]/goalDict[goal][0]*100,2))+'%']
            writer.writerow(row)

# pcost.py
#
# Exercise 1.27
import sys
def portfolio_cost(filename):
    import csv
    f = open(filename)
    rows = csv.reader(f)
    totalCost = 0
    header = next(rows)
    for row in rows:
        try:
            rowCost = int(row[1]) * float(row[2])
            totalCost = totalCost + rowCost
        except ValueError:
            print('Data error', row)
    return totalCost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename='Data/portfolio.csv'

cost = portfolio_cost(filename)
print('The total cost is: ', cost)

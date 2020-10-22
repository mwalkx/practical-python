# sears tower problem
# tower 1450 ft
# dollar bill 0.004
towerHtFt = 1450.0
towerHtIn = towerHtFt * 12
print("Height in In", towerHtIn)
billHt = .004
pileHt = billHt
billCount = 1
day = 1
while pileHt < towerHtIn :
    pileHt = pileHt * 2
    day = day + 1
    print(day, pileHt)

print("bills required", pileHt/.004)
print("total days", day)

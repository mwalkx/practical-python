# bounce.py
#
# Exercise 1.5
initHeight = 100
returnBounce = 3/5
bounces = 10
for i in range(10):
    initHeight = round(initHeight * returnBounce, 4)
    print(i+1, initHeight)

print("done")

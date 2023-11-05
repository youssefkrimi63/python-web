for num in range(151):
    print(num)


for num in range(5, 1001, 5):
    print(num)


for num in range(1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)


sum_of_odds = 0
for num in range(1, 500001, 2):
    sum_of_odds += num
print(sum_of_odds)


for num in range(2018, 0, -4):
    print(num)


lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)

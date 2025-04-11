numbers = [2,2,3,4,5,7,8]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
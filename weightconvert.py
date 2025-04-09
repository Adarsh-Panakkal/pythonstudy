data = input("Select weight unit(kg or lbs):")
if data =="kg":
   kg1 =float(input("Enter your Weight in kg:"))
   weight = kg1*2.20462
   print("Your weight in lbs =",weight)
elif data =="lbs":
    lbs1 = float(input("Enter your Weight in lbs:"))
    weight =  lbs1* 0.453592
    print("Your weight in kg =", weight)
else:
    print("unit is wrong")
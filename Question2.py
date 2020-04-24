s =int(input("Enter sales amount :"))
if s <= 5000:
    d = (5/100)*s
    print("Discount is :", d)
elif s <= 10000:
    d = (10/100)*s
    print("Discount is :", d)
elif s <= 15000:
    d = (15/100)*s
    print("Discount is :", d)
elif s > 15000:
    d = (30/100)*s
    print("Discount is :", d)
print("Net Pay :", s-d)

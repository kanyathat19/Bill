print("Bill Split Calculator")
bill = float(input("Enter the bill: "))
tip = float(input("Enter how much tip you want to give: "))
tip_amount = (tip/100)*bill
total = tip_amount+bill
print(f"Total (including tip): {total}")
people = int(input("Enter people:"))
split = total/people
print(f"Each person pays: {split}")
print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ")
while size not in ("S", "M", "L"):
    print("Sorry, please enter S, M, or L")
    size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
while pepperoni not in ("Y", "N"):
    print("Sorry, please enter Y or N")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill += 0
extra_cheese = input("Do you want extra cheese? Y or N: ")
while extra_cheese not in ("Y", "N"):
    print("Sorry, please enter Y or N")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
        bill += 1
else:
    bill += 0
print(f"Your total bill is: ${bill}")
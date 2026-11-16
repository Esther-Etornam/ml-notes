bill = float(input("Enter the total bill amount: "))

friends = int(input("Enter the number of friends: "))
each_person = bill/friends
print(f" Each person pays GHS {each_person:.2f}")
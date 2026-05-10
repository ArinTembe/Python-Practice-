#personal finance tracker 
Expenselist = []
print('Welcome to your expense tracker, let’s see where your money actually goes!')

while True:
    print("==== MENU ====")
    print("1. Add Expenses")
    print("2. View all Expenses")
    print("3. View Total Expenses")
    print("Exit")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        date = input("What date did you spend? :  ")
        category = input("On what did you spend your money? : ")
        description = input("Any more details which you want to remember?: ")
        amount = float(input("Enter your amount: "))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        Expenselist.append(expense)
        print("Expenses added successfully!")

    elif choice == 2:
        if (len(Expenselist) == 0):
                print("No expenses added yet.")
        else: 
             print("==== These are all of your expenses. ====")
             count = 1
             for  expense in Expenselist:
                  print(f'expense number{count} -> {expense["date"]}, {expense["category"]}, {expense["description"]}, {expense["amount"]}')
                  count = count+1

    elif choice == 3:
         total = 0 
         for eachexpense in Expenselist:
              total = total + eachexpense["amount"]

              print("Total expenses = ", total)

    elif choice == 4:
         print("Thank You! Visit us when there is a new expense.")
         break

    else:
         print("INVALID CHOICE.")

    

 
    
                 
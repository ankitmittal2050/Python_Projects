# Expense tracker Report
expense_list =[] # list of expense in form of dictionary
print("Welcome to Expense tracker: ")
while True:
    print("====Menu====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Exit")
    choice = int(input("Please enter your choice : "))
#  1. Add Expense   
    if(choice==1):
        date=input("Enter the expense date (YYYY/MM/DD) : ")
        category=input("Enter the expense category (food/travel/bill/shopping etc) : ")
        description=input("Enter the expense category's description : ")
        amount=float(input("Enter the expense amount : "))

        expense_dict={
            'date':date,
            'category':category,
            'description':description,
            'amount':amount
        }

        expense_list.append(expense_dict)
        print(" \n Expense is added successfully")
#  2. View All Expense
    elif(choice==2):
        if(len(expense_list)==0):
            print("No Expenses Added. Kindly add the expense detail")
        else:
            print("====Below is your expense details====")
            count=1
            print("Expense Count   Date   Category   Amount")
            for i in expense_list:
                print(f"{count}   {i['date']}   {i['category']}   {i['description']}   {i['amount']}")
                count+=1
#  3. View Total Expense
    elif(choice==3):
        total=0
        for i in expense_list:
            total+=i['amount']
        
        print("\n Total expense is : ",total)

#  4. Exit
    elif(choice==4):
        print("Thanks for using the tool!")
        break
    else:
        print("Invalid choice! Try Again")

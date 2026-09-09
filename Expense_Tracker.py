import json

class Expense:
    def __init__(self,amount,category,describtion,date):
        self.amount = amount
        self.category = category
        self.describtion = describtion
        self.date = date

    def to_dict(self):
        return {
            "Amount": self.amount,
            "Category":self.category,
            "Description":self.describtion,
            "Date": self.date
        }

    def __str__(self):
        return f"category: {self.category}  Rs. {self.amount}  {self.describtion}  Date: {self.date}"

class ExpenseTracker:
    def __init__(self):
        self.expense = []

    def add_expense(self,amount,category,description,date):
        new = Expense(amount,category,description,date)
        self.expense.append(new)
        print("Added Successfully")


    def view_expense(self):
        if(len(self.expense) < 1):
            print("list is empty")
        else:
            for i in self.expense:
                print(i)




    def delete_expense(self,index):
        if(len(self.expense) < 1):
            print("list is empty")

        if(index>= 0 and index< len(self.expense)):
            del self.expense[index]
            print("Deleted Successfully")
        else:
            print("Invalid index")


    def total_by_category(self):
        total = {}
        for i in self.expense:
            if(i.category in total):
                total[i.category] = total[i.category] + i.amount
            else:
                total[i.category] = i.amount

        print(total)

    def save_to_file(self):
        data = []
        for i in self.expense:
            data.append(i.to_dict())
        with open("data.json","w") as f:
            json.dump(data,f)
        print("Saved data succesfully")

    def load_from_file(self):
        try: 
            with open("data.json","r")as f:
                data = json.load(f)

            for i in data:
                new = Expense(i["Amount"],i["Category"],i["Description"],i["Date"])
                self.expense.append(new)
        except FileNotFoundError:
            print("No, save file found")




tracker = ExpenseTracker()
tracker.load_from_file()
while True:
    print("1. Add Expensive")
    print("2. View Expensive")
    print("3. Delete Expense")
    print("4. Total By category")
    print("5. Save & Exit")

    choice = input("Enter your Choice: ")
    if(choice == "1"):
        amount=int(input("Enter amount: "))
        category = input("Enter Category: ")
        description = input("Enter descripion of category: ")
        date= input("Enter Date (DD-MM-YYYY): ")
        tracker.add_expense(amount,category,description,date)
    elif(choice == "2"):
        tracker.view_expense()

    elif(choice == "3"):
        index =int(input("Enter a deletion expense index: "))
        tracker.delete_expense(index)
    elif(choice == "4"):
        tracker.total_by_category()
    elif(choice == "5"):
        tracker.save_to_file()
        print("good Bye")
        break
    else:
        print("invalid Choice")

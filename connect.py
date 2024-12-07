import csv 

import pandas as pd
import os

# List of CSV files to merge
csv_files = ["income.csv", "expense.csv", "savings.csv"]  # Replace with your filenames

# Read and merge all CSV files
merged_data = pd.concat([pd.read_csv(file) for file in csv_files])

# Save the merged file
merged_data.to_csv("merged_output.csv", index=False)

print("CSV files merged successfully!")

################################################################################
#& list transactions
################################################################################

def readall():
    csv_files = ["income.csv", "expense.csv", "savings.csv"]
    merged_data = pd.concat([pd.read_csv(file) for file in csv_files])
    merged_data.to_csv("merged_output.csv", index=False)
    
    with open("merged_output.csv", "r") as file:
        reader = csv.reader(file)
        k=[]
        for row in reader:
            print(row)
            k.append(row)
    return  k

################################################################################
#6 track savings progress
################################################################################

def readsav():
    with open("savings.csv", "r") as file:
        reader = csv.reader(file)
        k=[]
        for row in reader:

            k.append(row)
    return k

def readinc():
    with open("income.csv", "r") as file:
        reader = csv.reader(file)
        k=[]
        for row in reader:

            k.append(row)
    return k

def readexp():
    with open("expense.csv", "r") as file:
        reader = csv.reader(file)
        k=[]
        for row in reader:
            k.append(row)
    return k



def readbydate(date):
    csv_files = ["income.csv", "expense.csv", "savings.csv"]
    merged_data = pd.concat([pd.read_csv(file) for file in csv_files])
    merged_data.to_csv("merged_output.csv", index=False)

    with open("merged_output.csv", "r") as file:
        reader = csv.reader(file)
        k=[]
        for row in reader:
            if row[1]==date:
                print(row)
                k.append(row)
    
    return k 


def readbycat(cat):
    with open("expense.csv", "r") as file:
        reader = csv.reader(file)
        k=[]
        for row in reader:
            if row[2]==cat:
                k.append(row)

    return k


def edit(sno):

    
    print("Enter 1 for Income")
    print("Enter 2 for Saving")
    print("Enter 3 for Expense")

    cat=int(input("Please input the catergory no - "))

    if cat==1:
        choice = int(input("Enter the attribute you want to edit:\n1. Amount\n2. Date\n3.Source\n"))
        if choice == 1:
            u = float(input("Enter the updated amount: "))

        elif choice == 2:
            u = input("Enter the updated date in DD-MM-YYYY format: ")

        elif choice == 3:
            u = input("Enter updated source of income: ")


        with open("income.csv", "r+") as file:
            reader = csv.reader(file)
            k=[]
            m=[]
            for row in reader:
                m=row[:]
                if row[0]==sno:
                    m[choice]=u
                k.append(m)
            
            writer=csv.writer()
            writer.writerows(k)

    elif cat==2:
        choice = int(input("Enter the attribute you want to edit:\n1. Amount\n2. Date\n3.Goal\n4. Target Amount\n"))
        if choice == 1:
            u = float(input("Enter the updated amount: "))

        elif choice == 2:
            u = input("Enter the updated date in DD-MM-YYYY format: ")

        elif choice == 3:
            u = input("Enter the updated goal of the saving: ")

        elif choice == 4:
            u = float(input("Enter the updated target amount: "))



        with open("savings.csv", "r+") as file:
            reader = csv.reader(file)
            k=[]
            m=[]
            for row in reader:
                m=row[:]
                if row[0]==sno:
                    m[choice]=u
                k.append(m)
            
            writer=csv.writer()
            writer.writerows(k)

    elif cat==3:

        choice = int(input("Enter the attribute you want to edit:\n1. Amount\n2. Date\n3. Category\n4. Expense Type\n"))
        if choice == 1:
            u = float(input("Enter the updated amount: "))
          
        elif choice == 2:
            u = input("Enter the updated date in DD-MM-YYYY format: ")

        elif choice == 3:
            u = input("Enter the updated category of expense: ")

        elif choice == 4:
            u = input("Enter the updated type of expense: ")

        with open("expense.csv", "r+") as file:
            reader = csv.reader(file)
            k=[]
            m=[]
            for row in reader:
                m=row[:]
                if row[0]==sno:
                    m[choice]=u
                k.append(m)
            
            writer=csv.writer()
            writer.writerows(k)
    
def deltrans(sno):
    
    print("Enter 1 for Income")
    print("Enter 2 for Saving")
    print("Enter 3 for Expense")

    cat=int(input("Please input the catergory no - "))

    if cat==1:

        with open("income.csv", "r+") as file:
            reader = csv.reader(file)
            k=[]
            m=[]
            for row in reader:
                m=row[:]
                if row[0]!=sno:
                    k.append(m)
            
            writer=csv.writer()
            writer.writerows(k)

    elif cat==2:


        with open("savings.csv", "r+") as file:
            reader = csv.reader(file)
            k=[]
            m=[]
            for row in reader:
                m=row[:]
                if row[0]!=sno:
                    k.append(m)
            
            writer=csv.writer()
            writer.writerows(k)

    elif cat==3:


        with open("expense.csv", "r+") as file:
            reader = csv.reader(file)
            k=[]
            m=[]
            for row in reader:
                m=row[:]
                if row[0]!=sno:
                    k.append(m)
            
            writer=csv.writer()
            writer.writerows(k)


def addtran():
    csv_files = ["income.csv", "expense.csv", "savings.csv"]
    merged_data = pd.concat([pd.read_csv(file) for file in csv_files])
    merged_data.to_csv("merged_output.csv", index=False)
    m=0
    with open("merged_output.csv", "r") as file:
        reader = csv.reader(file)
        m=len(reader)+1

    print("Enter 1 for Income")
    print("Enter 2 for Saving")
    print("Enter 3 for Expense")

    cat=int(input("Please input the catergory no - "))

    if cat==1:
        choice = int(input("Enter the attribute you want to edit:\n1. Amount\n2. Date\n3.Source\n"))
        k=[]
        k.append(m)
        am = float(input("Enter the updated amount: "))
        k.append(am)
        dat = input("Enter the updated date in DD-MM-YYYY format: ")
        k.append(dat)
        sou = input("Enter updated source of income: ")
        k.append(sou)


        with open("income.csv", "a") as file:

            writer=csv.writer()
            writer.writerow(k)

    elif cat==2:
        choice = int(input("Enter the attribute you want to edit:\n1. Amount\n2. Date\n3.Goal\n4. Target Amount\n"))
        k[]
        k.append(m)
        am = float(input("Enter the updated amount: "))
        k.append(am)
        dat = input("Enter the updated date in DD-MM-YYYY format: ")
        k.append(dat)
        goal = input("Enter the updated goal of the saving: ")
        k.append(goal)
        targ = float(input("Enter the updated target amount: "))
        k.append(targ)



        with open("savings.csv", "a") as file:
           
            writer=csv.writer()
            writer.writerow(k)

    elif cat==3:

        choice = int(input("Enter the attributes:\n1. Amount\n2. Date\n3. Category\n4. Expense Type\n"))
        k=[]
        k.append(m)
        am = float(input("Enter the updated amount: "))
        k.append(am)
        dat= input("Enter the updated date in DD-MM-YYYY format: ")
        k.append(dat)
        cat= input("Enter the updated category of expense: ")
        k.append(cat)
        typ= input("Enter the updated type of expense: ")
        k.append(typ)

        with open("expense.csv", "a") as file:

            writer=csv.writer()
            writer.writerow(k)

    




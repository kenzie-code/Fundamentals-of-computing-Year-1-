import Return
import ListSplit
import Datetime
import Borrow

def start():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("Enter 1. To Display")
        print("Enter 2. To Borrow a book")
        print("Enter 3. To return a book")
        print("Enter 4. To exit")
        try:
            q = int(input("Select a choice from 1 to 4: "))
            if(q == 1):
                with open("Stock.txt","r") as z:
                    lines = z.read()
                    print(lines)
                    print()
   
            elif(q == 2):
                ListSplit.listSplit()
                Borrow.borrowbook()
                
            elif(q == 3):
                ListSplit.listSplit()
                Return.returnbook()
                
            elif(q == 4):
                print("Much thanks for utilizing Library Management framework")
                break
            
            else:
                print("Please enter a valid number from 1 to 4")
                
        except ValueError:
            print("Please input as suggested.")
            print("")
            print("a")
start()

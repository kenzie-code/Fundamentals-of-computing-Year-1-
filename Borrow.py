import Datetime
import ListSplit

def borrowbook():
    success = False
    while(True):
        Firstname = input("Please, Enter the first name of the borrower: ")
        if Firstname.isalpha():
            break
        
        print("please enter a valid input")
    while(True):
        Lastname = input("Please, Enter the last name of the borrower: ")
        if Lastname.isalpha():
            break
        
        print("please enter a valid input")
            
    t = "Borrow-"+Firstname+".txt"
    with open(t,"w+") as z:
        z.write("               Library Management System  \n")
        z.write("                   Borrowed By: "+ Firstname+" "+Lastname+"\n")
        z.write("    Date: " + Datetime.getDate()+"    Time:"+ Datetime.getTime()+"\n\n")
        z.write("S.N. \t\t Bookname \t      Authorname \n" )
     
    
    while success == False:
        print("Please select a alternatives below:")
        for i in range(len(ListSplit.bookname)):
            print("Enter", i, "to borrow book", ListSplit.bookname[i])
    
        try:   
            a = int(input())
            try:
                if(int(ListSplit.quantity[a]) > 0):
                    print("Book is accessible")
                    with open(t,"a") as z:
                        z.write("1. \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                    ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                    with open("Stock.txt","w+") as z:
                        for i in range(7):
                            z.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.price[i]+"\n")


                    #multiple book borrowing code
                    loop = True
                    count = 1
                    while loop == True:
                        choice = str(input("Do you wish to acquire more books? Anyway you cannot acquire same book twice. Press Y for Yes and N for No."))
                        if(choice.upper() == "Y"):
                            count = count + 1
                            print("Please select an alternatives below:")
                            
                            for i in range(len(ListSplit.bookname)):
                                print("Enter", i, "to borrow book", ListSplit.bookname[i])
                                
                            a = int(input())
                            if(int(ListSplit.quantity[a]) > 0):
                                print("Book is accessible in our store")
                                with open(t,"a") as z:
                                    z.write(str(count) +". \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                                ListSplit.quantity[a] = int(ListSplit.quantity[a])-1
                                with open("Stock.txt","w+") as z:
                                    for i in range(7):
                                        z.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.price[i]+"\n")
                                        success = False
                                        success = False
                            else:
                                loop = False
                                break
                            
                        elif (choice.upper() == "N"):
                            print ("Thank you for getting books from us. ")
                            print("")
                            loop = False
                            success = True
                        else:
                            print("Please enter a valid input.")
                        
                else:
                    print("Book is not accessible in our store")
                    borrowBook()
                    success = False
                    
            except IndexError:
                print("")
                print("Please choose book according to their number.")
                
        except ValueError:
            print("")
            print("Please pick as proposed.")

import ListSplit
import Datetime

def returnbook():
    Name = input("Please, Enter name of borrower: ")
    a = "Borrow-"+Name+".txt"
    try:
        with open(a ,"r") as z:
            lines = z.readlines()
            lines = [a.strip("$") for a in lines]
    
        with open(a ,"r") as z:
            data = z.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnbook()

    b = "Return-"+Name+".txt"
    with open(b ,"w+")as z:
        z.write("                Library Management System \n")
        z.write("                    Returned By: "+ Name+"\n")
        z.write("    Date: " + Datetime.getDate()+"    Time:"+ Datetime.getTime()+"\n\n")
        z.write("S.N.     Bookname       price\n")


    total = 0.0
    for i in range(7):
        if ListSplit.bookname[i] in data:
            with open(b,"a") as z:
                z.write(str(i+1)+"\t\t"+ListSplit.bookname[i]+"\t\t"+ListSplit.price[i]+"\n")
                ListSplit.quantity[i] = int(ListSplit.quantity[i])+1
            total += float(ListSplit.price[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date terminated already? Press Y for Yes and N for No")
    
    stat = input()
    if(stat.upper() == "Y"):
        print("How long was the book returned late?")
        day = int(input())
        fine = 3 * day
        with open(b,"a")as z:
            z.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
            total = total + fine
            
    print("Final Total: "+ "$"+str(total))
    with open(b ,"a")as z:
        z.write("\t\t\t\t\tTotal: $"+ str(total))
        
    with open("Stock.txt","w+") as z:
        for i in range(7):
            z.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.price[i]+"\n")
  

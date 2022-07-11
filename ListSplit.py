def listSplit():
    global bookname
    global authorname
    global quantity
    global price
    bookname = []
    authorname = []
    quantity = []
    price = []
    with open("Stock.txt","r") as z:
        
        lines = z.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            count=0
            for a in lines[i].split(','):
                if(count==0):
                    bookname.append(a)
                    
                elif(count==1):
                    authorname.append(a)
                    
                elif(count==2):
                    quantity.append(a)
                    
                elif(count==3):
                    price.append(a.strip("$"))
                count+=1

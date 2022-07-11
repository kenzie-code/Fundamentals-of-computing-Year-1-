#Write a program that takes input from the user a string of numbers (eg.“24453”),
#then all the numbers from the string must be put in a list.
#The program then computes the sum, maximum and minimum from the list of numbers.

number = input("Enter a string of numbers:")


n = list(number)
sum_ = 0
max_ = n[0]
min_ = n[0]

for i in range(len(n)):
    m = n[i]
    sum_ = sum_+int(m)

    if(max_ < m):
        max_ = m

    if(min_ > m):
        min_ = m
       

print("The sum of numbers is:", sum_)
print("The maximum from the list is:", max_)
print("The minimum from the list is:", min_)

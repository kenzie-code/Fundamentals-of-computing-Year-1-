 #Write a program that takes 2 words as input from the user and prints out a list
#containing the letters which the 2 words have in common. For example,
#if word1 is “english”  and word2 is “nepali”, the output should be [“l”, “e”, “i”, “n”]. 

word1 = input("Enter First word:")
word2 = input("Enter another word:")
x1 = set(word1)
x2 = set(word2)
Y = list(x1 & x2)

print("Common letters:" , Y)

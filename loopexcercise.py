#1
#i=1
#while i < 11:
#    print(i)
#    i += 1

#2
#rows = 5
#columns = 5
#for r in range (1,6):
#    for c in range (1, r+1):
#        print(c, end = " ")
#    print()

#3
num = int(input("Enter a number: "))
sum = 0
for i in range (1, num+1):
    sum = sum + i
    i+=1
print(sum)
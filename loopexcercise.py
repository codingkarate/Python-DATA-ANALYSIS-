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
#num = int(input("Enter a number: "))
#sum = 0
#for i in range (1, num+1):
#    sum = sum + i
#    i+=1
#print(sum)

#4
#count = 0
#number = int(input("Enter a number: "))
#while number != 0:
#    number = number // 10
#    count += 1
#print(count)

#5
#rows = 5
#columns = 5
#for r in range (0,rows+1):
#    for c in range (columns - r, 0, -1):
#        print(c, end = " ")
#    print()


#6
#start = int(input("Enter start number: "))
#end = int(input("Enter end number: "))
#for num in range (start, end + 1):
#    if num > 1:
#        for i in range (2, num):
#            if (num%i) == 0:
#                break
#        else:
#            print(num)

#7
#t1, t2 = 0, 1
#for i in range (10):
#    print(t1)
#    t3 = t1 + t2
#    t1 = t2
#    t2 = t3


#8
#n = 5
#f = 1
#for i in range (1, n+1):
#    f = f*i
#print(f)

#9
#num = int(input("Enter a number: "))
#rev_num = 0
#while num > 0:
#    rem = num%10
#    rev_num = (10*rev_num) + rem
#    num = num//10
#print(rev_num)

#10
#n = 5
#start = 2
#sum_seq = 0
#for i in range (1, n+1):
#    print(start, end="+")
#    sum_seq += start
#    start = 10*start + 2
#print ("\n Sum of squence =", sum_seq)


#11
rows=5
columns=5
for r in range(1,6):
    for c in range (1, r+1):
        print("*", end = " ")
    print()
for r in range(1, rows):
    for c in range(columns-r, 0, -1):
        print("*", end = " ")
    print()
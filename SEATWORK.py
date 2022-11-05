print ("Array: [8, 12, 50, 25, 30, 29, 60, 52, 33, 99]")
print ("5 options available, please choose:")
print ("(1) Adding number in Array")
print ("(2) Insert a new number in Array")
print ("(3) Removing number in Array")
print ("(4) Arranging Array in ascending order")
print ("(5) Arranging Array in descending order")
Ans = float(input("What do you want to do?(1-6): "))

if Ans == 1:
    num1 = int(input("Give number to add: "))
    print("The element has been added")
    list1 = [8, 12, 50, 25, 30, 29, 60, 52, 33, 99]
    list1.append(num1)
    print(F"This is the new Array:{list1}")
elif Ans == 2:
    num21 = int((input("Give number for row : ")))
    num22 = int(9(input("Give number to insert : ")))
    print("The element has been inserted")
    list2 = [8, 12, 50, 25, 30, 29, 60, 52, 33, 99]
    list2.insert(num21,num22)
    print(F"This is the new Array:{list2}")
elif Ans == 3:
    num3 = int((input("Give number in the array you want to remove : ")))     
    print("The element has been removed")
    list3 = [8, 12, 50, 25, 30, 29, 60, 52, 33, 99]
    list3.remove(num3)
    print(F"This is the new Array:{list3}")
elif Ans == 4:
    print("The array is now processing") 
    print("The element has been arranged to Ascending") 
    list4 = [8, 12, 50, 25, 30, 29, 60, 52, 33, 99]
    list4.sort()
    print(F"This is the new Array:{list4}")
elif Ans == 5:
    print("The array is now processing") 
    print("The element has been arranged to Descending") 
    list5 = [8, 12, 50, 25, 30, 29, 60, 52, 33, 99]
    list5.sort(reverse=True)
    print(F"This is the new Array:{list5}")


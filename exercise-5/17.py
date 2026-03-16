''' Write a function that performs the following operations on a list:
• Print the fourth item
• Print all items except the first two
• Print the list in reverse
• Print the sum of elements
• Print maximum and minimum elements
• Print index of first zero (or -1 if none)
• Print list in ascending and descending order '''
def list_operations(l):
    length = len(l)
    num = 1
    while num == 1:
        print("\nEnter your choice from below options")
        print("1. Print the fourth item")
        print("2. Print all items except the first two")
        print("3. Print the list in reverse")
        print("4. Print the sum of elements")
        print("5. Print maximum and minimum elements")
        print("6. Print index of first zero (or -1 if none)")
        print("7. Print list in ascending and descending order")
        choice = int(input("Enter choice (1-7): "))
        match choice:
            case 1:
                print("fourth item =", l[3])
            case 2:
                e = []
                print("items except first two : ", end = "")
                for i in range(2, length):
                    e.append(l[i])
                print(e)
            case 3:
                m = []
                print("list in reverse : ",end = "")
                for i in range(length-1, -1, -1):
                    m.append(l[i])
                print(m)
            case 4:
                s = 0
                for i in range(length):
                    s += l[i]
                print("Sum =", s)
            case 5:
                minimum = l[0]
                maximum = l[0]
                for i in range(length):
                    if l[i] < minimum:
                        minimum = l[i]
                    if l[i] > maximum:
                        maximum = l[i]
                print("minimum = ", minimum)
                print("maximum = ", maximum)
            case 6:
                index = -1
                for i in range(length):
                    if l[i] == 0:
                        index = i
                        break
                print("index of first zero =", index)
            case 7:
                asc = l.copy()
                for i in range(length):
                    for j in range(i+1, length):
                        if asc[i] > asc[j]:
                            asc[i], asc[j] = asc[j], asc[i]
                print("ascending order: ", asc)
                desc = asc[::-1]
                print("descending order: ", desc)
            case _:
                print("Invalid choice")
        num = int(input("enter 1 to continue and 0 to exit : "))
        if num != 1:
            print("program ended successfully.")
l = []
length = int(input("enter length of list: "))
if length >= 4:
    for i in range(length):
        x = int(input(f"enter element {i+1}: "))
        l.append(x)
    list_operations(l)
else:
    print("please enter minimum four elements.")
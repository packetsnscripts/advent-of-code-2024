
list1 = []
list2 = []
with open('src/day01/input_1.txt', "r") as file:
    for line in file:
        print(line)
        num1, num2 = file.readline().split("   ")
        print(f"{num1} {num2}")
        list1.append(num1)
        list2.append(num2)
    
# print(list1)
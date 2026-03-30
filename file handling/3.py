with open("text2.txt","r") as f:
    data = f.read()
count = 0
for char in data:
    count+=1
print(count)
with open("text2.txt","r") as f:
    data1 = f.readlines()
length = len(data1)
print(f"total no of lines = {length}")
count1 = 0
for char in data:
    if char == " ":
        count1+=1
print(f"total no of words = {count1 + length}")
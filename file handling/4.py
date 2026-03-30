with open("text2.txt","r") as f:
    data = f.read()
word_list = data.split()
for i in range(len(word_list)):
    if word_list[i].lower() == 'anything':
        word_list[i] = 'something'
count = []
count1 = 0
for i in data:
    count1+=1
    if i == "\n":
        count1 = 0
print(count)
with open("text2.txt","a") as f:
    for i in range(len(word_list)):
        data = f.write(f"{word_list[i]} ")
        print("\n")
# def kmax(lst,k):
#     for i in range(len(lst)):
#         for j in range(i+1,len(lst)):
#             if lst[i] <= lst[j]:
#                 temp = lst[i]
#                 lst[i] = lst[j]
#                 lst[j] = temp
#     new_l = []
#     for i in lst:
#         if i not in new_l:
#             new_l.append(i)
#     print(new_l)
#     maximum = new_l[k-1]
#     return f"{k} largest element = {maximum}"
# print(kmax([1,6,2,9,10,6,9,3,7],1))

import pyttsx3
engine = pyttsx3.init()
text = input("enter something :")
engine.say(text)
engine.runAndWait()
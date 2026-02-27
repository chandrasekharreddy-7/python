''' Q17 : Write a program that takes two 5-letter words as input and finds the sum of the distance
between the respective characters of these words. '''
''' process - 1 '''
def worddistance(word1,word2):
    if len(word1) == 5 and len(word2) == 5 and word1.isalpha() and word2.isalpha():
        sum = 0
        for i in range(len(word1)):
            distance = abs(ord(word1[i]) - ord(word2[i]))
            sum = sum + distance
        print(sum)
    else:
        print("please enter a 5 letter words with upper case or lower case letter.")
word1 = input("enter a 5 letter word :")
word2 = input("enter a five letter word :")
worddistance(word1,word2)


''' process - 2 '''
word1 = input("enter a 5 - letter word :")
word2 = input("enter another 5 - letter word :")
if len(word1) == 5 and len(word2) == 5 and word1.isalpha() and word2.isalpha():
    sum = 0
    distance = abs(ord(word1[0]) - ord(word2[0])) + abs(ord(word1[1]) - ord(word2[1])) + abs(ord(word1[2]) - ord(word2[2])) + abs(ord(word1[3]) - ord(word2[3])) + abs(ord(word1[4]) - ord(word2[4]))
    sum = sum + distance
    print(f"sum of distance between respective words = {sum}")
else:
    print("enter a 5 - letter word")
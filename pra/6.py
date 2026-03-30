''' Manual String Counting:
    Write a program to count the number of vowels, consonants, digits, and special characters 
    in a string using loops (without built-in library functions). '''
def string_counting(string):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    d_count = 0
    s_count = 0
    for i in string:
        if i in vowels:
            v_count += 1
        elif 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            c_count += 1
        elif '1' <= i <= '9':
            d_count += 1
        else:
            s_count += 1
    return f"vowels = {v_count} : consonant count = {c_count} : digit count = {d_count} : special charcater count = {s_count}"
string = input("enter a string :")
print(string_counting(string))
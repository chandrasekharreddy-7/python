# n = 5
# for i in range(n):
#     print(" " * (n-i-1) + "* " * (i+1))
# for i in range(n-1, 0, -1):
#     print(" " * (n-i) + "* " * i)

# n = 5
# num = 1
# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()
    
# n = 5
# for i in range(n):
#     num = 1
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i+1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if j == 0 or j == i or i == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = 5

# # Upper
# for i in range(1, n+1):
#     print("*" * i + " " * (2*(n-i)) + "*" * i)

# # Lower
# for i in range(n, 0, -1):
#     print("*" * i + " " * (2*(n-i)) + "*" * i)


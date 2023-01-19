
# --- O(n) ---
# def print_items(n):
#     for i in range(n):
#         print(i)

# print_items(10)


## --- Drop Contants ---
# def print_items(n):
#     for i in range(n):
#         print(i)
        
#     for j in range(n):
#         print(j)

# print_items(10)


## --- Squared ---
# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             # print(i,j) # n*n = n^2
#             for k in range(n):
#                 print(i,j,k) # O(n^2)

# print_items(10)


## --- Drop-Non Dominants ---
# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j) # n*n = n^2
            
#     for k in range(n):
#         print(k) # O(n^2)

# print_items(10) # O(n^2 + n)
# Take user input for the list
n = int(input("Enter the number of strings in the list: "))
L1 = []
for i in range(n):
    L1.append(input(f"Enter string {i+1}: "))

# Sort the list based on the number of characters in each string
for i in range(len(L1)):
    for j in range(i + 1, len(L1)):
        if len(L1[i]) > len(L1[j]):
            # Swap the elements
            temp = L1[i]
            L1[i] = L1[j]
            L1[j] = temp

# Print the sorted list
print("Sorted list based on string lengths:", L1)

# Sorting Strings by Length in Python

## Aim

To write a Python program that accepts a list of strings from the user and sorts them in ascending order based on the number of characters in each string.

## Description

This program takes the number of strings as input and stores them in a list. It then sorts the strings based on their lengths using **nested loops and swapping**. Strings with fewer characters appear first, followed by strings with more characters.

## Algorithm

1. Start the program.
2. Accept the number of strings from the user.
3. Create an empty list named `L1`.
4. Read the strings from the user and append them to the list.
5. Use two nested loops to compare the lengths of the strings.
6. If the length of the current string is greater than the length of the next string, swap their positions.
7. Repeat the process until the list is sorted.
8. Display the sorted list.
9. Stop the program.

## Python Code

```python
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
```

## Sample Output

```text
Enter the number of strings in the list: 4
Enter string 1: Apple
Enter string 2: Hi
Enter string 3: Banana
Enter string 4: Cat
Sorted list based on string lengths: ['Hi', 'Cat', 'Apple', 'Banana']
```

## Concepts Used

* **List:** Stores multiple strings.
* **User Input:** Accepts strings from the user.
* **Nested Loops:** Compare the lengths of strings.
* **`len()` Function:** Returns the number of characters in a string.
* **Swapping:** Exchanges the positions of two strings.
* **Conditional Statement:** Checks whether one string is longer than another.

## Time Complexity

* **Time Complexity:** O(n²), because the program uses nested loops to compare strings.
* **Space Complexity:** O(n), for storing the list of strings.

## Result

The program successfully sorts a list of strings in ascending order based on their lengths using nested loops and swapping.

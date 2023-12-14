sides_A = 6
sides_B = 6

# By using math formula directly
total_combinations = sides_A * sides_B
print("Total combinations by direct formula:", total_combinations)

dice_A = [1, 2, 3, 4, 5, 6]
dice_B = [1, 2, 3, 4, 5, 6]

count = 0
combinations_matrix = []

for i in dice_A:
    combinations = []
    for j in dice_B:
        count += 1
        combinations.append((i, j))  # Storing combinations as tuples
    combinations_matrix.append(combinations)

print("Total combinations calculated:", count)

# Displaying the combinations matrix
for row in combinations_matrix:
    print(row)

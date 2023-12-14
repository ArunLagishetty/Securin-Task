def undoom_dice(die_A, die_B):
    new_die_A = []
    new_die_B = []
    count = 0

    for i in range(len(die_A)):
        for j in range(len(die_B)):
            if die_A[i] <= 4 and die_A[i] + die_B[j] <= 6:
                new_die_A.append(die_A[i])
                new_die_B.append(die_B[j])
                count += 1
    
    return new_die_A, new_die_B

# Initial dice
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

# Function to undoom the dice
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)

# Displaying the new dice configurations
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)

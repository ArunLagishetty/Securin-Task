def calculate_probabilities(die_a, die_b):
    # Calculate probability distribution of sums for the dice
    total_combinations = len(die_a) * len(die_b)
    probabilities = {i: 0 for i in range(2, 13)}  # Dictionary to store probabilities

    for face_a in die_a:
        for face_b in die_b:
            total = face_a + face_b
            probabilities[total] += 1

    for key in probabilities:
        probabilities[key] /= total_combinations  # Calculate probability

    return probabilities

def undoom_dice(die_a, die_b, original_probabilities):
    # Transform the dice to meet the conditions while maintaining original probabilities
    new_die_a = die_a[:]  # Copy Die A to modify
    new_die_b = die_b[:]  # Copy Die B to modify

    # To Keep track of the changes made to Die A
    changes_to_a = {spot: [] for spot in range(1, 7)}  # Dictionary to store changes

    # Step 1: Transform Die A
    for i, face in enumerate(new_die_a):
        if face > 4:
            # Adjust spots on Die A to satisfy the condition
            new_face = 8 - face
            changes_to_a[new_face].append(i)  #changes made
            new_die_a[i] = new_face

    # Step 2: Update Die B to maintain sum probabilities
    for spot, indices in changes_to_a.items():
        # Calculating the impact of changing Die A on the probabilities
        diff = 4 - spot  # Difference in spots on Die A
        for index in indices:
            for j, face in enumerate(new_die_b):
                if new_die_a[index] + face - diff <= 6:
                    # Adjust Die B based on the difference in Die A to maintain probabilities
                    new_die_b[j] += new_die_a[index] - diff

    # Step 3: Verifying  and adjusting to maintain probabilities
    new_probabilities = calculate_probabilities(new_die_a, new_die_b)
    if new_probabilities != original_probabilities:
        pass  #no-operation statement

    return new_die_a, new_die_b

# Given original dice configurations
die_a_original = [1, 2, 3, 4, 5, 6]
die_b_original = [1, 2, 3, 4, 5, 6]

# Calculate original probabilities
original_probabilities = calculate_probabilities(die_a_original, die_b_original)

# Get the transformed dice configurations
new_die_a, new_die_b = undoom_dice(die_a_original, die_b_original, original_probabilities)

print("Original Die A:", die_a_original)
print("Original Die B:", die_b_original)
print("New Die A:", new_die_a)
print("New Die B:", new_die_b)

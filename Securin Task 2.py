dice_A = dice_B = [1, 2, 3, 4, 5, 6]

combinations_matrix = []
total_combinations = 0

for i in dice_A:
    combinations = []
    for j in dice_B:
        total_combinations += 1
        combinations.append([i, j])
    combinations_matrix.append(combinations)

for target_sum in range(2, 13):
    count = 0
    for dice_combinations in combinations_matrix:
        for dice_pair in dice_combinations:
            if sum(dice_pair) == target_sum:
                count += 1
    probability = round((count / total_combinations), 3)
    print("Probability of sum", target_sum, "is", probability)

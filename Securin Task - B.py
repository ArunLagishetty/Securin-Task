target = [ 0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1 ]
dieA = [1, 2, 3, 4, 0, 0]
dieB = [1, 3, 4, 5, 6, 0]
def validate_current_combination():
    cur = [0] * 13
    for i in range(6):
        for j in range(6):
            sum_val = dieA[i] + dieB[j]
            if 2 <= sum_val <= 12:
                cur[sum_val] += 1

    for i in range(2, 13):
        if cur[i] != target[i]:
            return False

    return True

def print_dice_values():
    print("Die A is:", dieA)
    print("Die B is:", dieB)
    exit(1)

def explore_dice_combinations(posA, posB):
    if posA < 6 and posB < 6:
        for valA in range(4):
            new_valA = valA + 1
            for valB in range(11):
                new_valB = valB + 1
                dieA[posA] = new_valA
                dieB[posB] = new_valB
                explore_dice_combinations(posA + 1, posB + 1)
    else:
        if validate_current_combination():
            print_dice_values()

explore_dice_combinations(4, 4)

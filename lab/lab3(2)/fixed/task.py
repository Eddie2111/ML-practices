import math
import random

brac_id = input()
ini_hp_string = [brac_id[len(brac_id) - 1], brac_id[len(brac_id) - 2]]
initial_hp = int("".join(map(str, ini_hp_string)))
#print(type(initial_hp));

def input_handler():
    turns = brac_id[0]
    depth = 2 * int(turns)
    bulletCount = int(brac_id[2])
    branchingFactor = bulletCount ** depth
    min_range, max_range = map(int, input().split(' '))

    updated = []  # We can put test array here and comment the 'for loop' to see the result are coming accordingly or not
    for i in range(branchingFactor):
        updated.append(random.randint(min_range, max_range))

    return depth, bulletCount, branchingFactor, updated


def mini_max(pos, depth, alpha, beta, maxim, flagCount):
    if depth == 0:
        flagCount += 1
        return updated[pos], flagCount

    if maxim:
        i_max = -math.inf
        for child_node in range(bulletCount):
            i, flagCount = mini_max((pos * bulletCount) + child_node, depth - 1, alpha, beta, False, flagCount)
            i_max = max(i_max, i)
            alpha = max(alpha, i)
            if alpha >= beta:
                flagCount - 1
                break
        return i_max, flagCount

    else:
        i_min = math.inf
        for child_node in range(bulletCount):
            i, flagCount = mini_max((pos * bulletCount) + child_node, depth - 1, alpha, beta, True, flagCount)

            i_min = min(i_min, i)
            beta = min(beta, i)
            if alpha >= beta:
                flagCount - 1
                break
        return i_min, flagCount


depth, bulletCount, branchingFactor, updated = input_handler()
#print(depth, bulletCount, branchingFactor, updated);
max_amount, flagCount = mini_max(0, depth, -math.inf, math.inf, True, 0)

print('Depth and Branches ratio is ', depth, ":", bulletCount)
print('Terminal States (leaf node values) are ', *updated)
print('Left life (HP) of the defender after maximum damage caused by the attacker is ', initial_hp - max_amount)
print('After Alpha-Beta Pruning Leaf Node Comparisons ', flagCount)


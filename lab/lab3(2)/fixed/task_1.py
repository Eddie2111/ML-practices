import random as rd;
import math as mt;
iteration = 0

def minimax(leaf_nodes, deep, alpha, beta, branch, playermax): #control part of the program
    global iteration              
    if deep == 0:
        value = leaf_nodes[iteration]
        iteration+=1
        return value
    # checks if there are still branches to be explored
    
    if not (playermax):
        min_val = mt.inf
        for ind in range(branch):
            val = minimax(leaf_nodes, deep-1, alpha, beta, branch, True)
            min_val = min(min_val, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return min_val
    # if playermax is false, then it is the minimizing player
    
    if (playermax):
        max_val = -mt.inf
        for ind in range(branch):
            val = minimax(leaf_nodes, deep-1, alpha, beta, branch, False)
            max_val = max(max_val, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return max_val
    # if playermax is true, then it is the maximizing player

def run(): #model part of the program, recieves the input and shows output to the user
    student_id  = input("student id: ")
    turn        = int(student_id[0])*2
    totalBranch = int(student_id[2])
    starting_hp = int(student_id[len(student_id)-1] + student_id[len(student_id)-2])

    range = input("range of HP [like, ''1 30'' for 17301106]:")
    range = range.split(' ')
    minimum,maximum = int(range[0]), int(range[1])
    count,leaf_nodes = 1, []

    while totalBranch ** turn >= count:
        leaf_nodes.append(rd.randrange(minimum,maximum))
        count += 1
    damage = minimax(leaf_nodes,turn,-mt.inf,mt.inf,totalBranch, True)

    print("Depth and Branches ratio is {}:{}".format(turn,totalBranch))
    print("Terminal States (leaf node values) are {}".format(leaf_nodes))

    print("Left life(HP) of the defender after maximum damage caused by the attacker is", starting_hp - damage)
    print("After Alpha-Beta Pruning Leaf Node Comparisons", iteration)
    
if "__main__" == __name__:  #view part of the program
    run()
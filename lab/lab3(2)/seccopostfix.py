import random
import math
infinity = math.inf

def MiniMax(nodes, branch, depth, alpha, beta, maximize=True):
    global iter_count
    if depth == 0:
        leafNode = nodes[iter_count]
        iter_count+=1
        return leafNode
    if maximize == False:
        maxvalue = infinity
        for ind in range(branch):
            value = MiniMax(nodes, branch, depth-1, alpha, beta, True)
            maxvalue = min(maxvalue, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return maxvalue
    if maximize == True:
        minvalue = -infinity
        for ind in range(branch):
            value = MiniMax(nodes, branch, depth-1, alpha, beta, False)
            minvalue = max(minvalue, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return minvalue
iter_count = 0


def main():
    studentid = input("Enter your student id: ")
    turns = int(studentid[0])*2
    initial_HP = int(studentid[-2:][::-1])
    branch = int(studentid[2])

    hpmin,hpmax = [int(x) for x in input("Minimum and Maximum value for the range of negative HP: ").split()]
    x = 1
    nodes = []
    while x <= branch**turns:
        nodes.append(random.randint(hpmin,hpmax))
        x+=1
    print(nodes)
    iter_count = 0
    damage = MiniMax(nodes,branch,turns,-math.inf,math.inf)

    print("Depth and Branches ratio is", turns,":",branch)
    print("Terminal States (leaf node values) are ",nodes)
    print("Left life(HP) of the defender after maximum damage caused by the attacker is", initial_HP - damage)
    print("After Alpha-Beta Pruning Leaf Node Comparisons", iter_count)
    
if __name__ == "__main__":
    main()
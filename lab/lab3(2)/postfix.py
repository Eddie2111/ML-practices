import random
import math

global studentID
studentID = '20101073'  # PUT YOUR ID HERE

def main(studentID): #qc passed
    hp = (studentID[len(studentID) - 1], studentID[len(studentID)-2] );
    initial_hp = int(studentID[len(studentID)-1])*10 + int(studentID[len(studentID)-2])
    return initial_hp, hp

def control(): #qc passed
    step = int(studentID[0])
    bulletDamage = int(studentID[2])
    depth = 2*step
    branches = bulletDamage**depth
    iterateCount = input('').split(' ')
    range_min = int(iterateCount[0])
    range_max= int(iterateCount[1])
    count= []
    iterate = branches
    while count:
        count.append(random.randint(range_min,range_max))
        iterate-=1;
    output = [depth, bulletDamage, branches, count]
    return output

    #print(iterate,count,iterateCount,range_max,range_min)
    
def minimax(node,depth,alpha,beta,itr_max,flagCount):
    if depth == 0:
        flagCount += 1;
        return count[node],flagCount;
    
    if not itr_max:
        minimum     = math.inf;
        for leaf in range(bulletDamage):
            count,flagCount = minimax((node*bulletDamage)+leaf,depth-1,alpha,beta,True,flagCount);
            minimum = min(minimum,count);
            beta    = min(beta,count);
            if alpha >= beta:
                flagCount -= 1;
                break;
        return minimum,flagCount;    
    
    if itr_max:
        maximum     = -math.inf;
        for leaf in range(bulletDamage):
            count,flagCount = minimax((node*bulletDamage)+leaf,depth-1,alpha,beta,False,flagCount);
            maximum = max(maximum,count);
            alpha   = max(alpha,count);
            if alpha >= beta:
                flagCount -= 1;
                break;
        return maximum,flagCount;
    
    
print(main(studentID))

IOelements = control();

depth = IOelements[0];
bulletDamage = IOelements[1];
branches = IOelements[2];
count = IOelements[3];

#maxsteps,flagcount = algo(0,level,float('-inf'),float('inf'),True,0);        
maxsteps, flagcount = minimax(0, depth, -math.inf, math.inf, True, 0)
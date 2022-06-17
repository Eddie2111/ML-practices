import numpy as np;


a,polo =[1,0,1,1,0],[1,1,0,1,0];
for i in range(len(a)):
    print(np.random.choice(a, 2, replace=True, p=None));
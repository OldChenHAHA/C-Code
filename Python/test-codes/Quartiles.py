import numpy as np
n = int(raw_input())
x = map(int, list(raw_input().split()))
x = sorted(x)
q1 = np.median( np.array(x[:len(x)//2]) )
q2 = np.median( np.array(x) )
if n%2 is 0:
    q3 = np.median( np.array(x[len(x)//2+1:]) )
else :
    q3 = q3 = np.median( np.array(x[len(x)//2:]) )
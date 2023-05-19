ALPHA = 0.85

import numpy as np

def PageRank(TransitionMat, InitVector, NumbOfIt, M):
    ti = InitVector
    J = np.full((M,M),1)
    aJ = np.multiply((1-ALPHA)/M,J)
    aTransitionMat = np.multiply(ALPHA,TransitionMat)
    G = np.add(aTransitionMat,aJ) # Google transition matrix.
    for _ in range(NumbOfIt):
        ti = np.matmul(ti,G)
    return ti

P = np.matrix([[0, 1/2, 0, 1/2], [1/2, 0, 1/2, 0], [0, 0, 0, 1], [1/4, 1/4, 1/4, 1/4]])
t0 = np.matrix([1/4,1/4,1/4,1/4])

t10000 = PageRank(P, t0, 10000, 4)
t10001 = PageRank(P, t0, 10001, 4)
t10002 = PageRank(P, t0, 10002, 4)
t10003 = PageRank(P, t0, 10003, 4)
t10004 = PageRank(P, t0, 10004, 4)

print(f' t_10000 = {t10000}')
print(f' t_10001 = {t10001}')
print(f' t_10002 = {t10002}')
print(f' t_10003 = {t10003}')
print(f' t_10004 = {t10004}')

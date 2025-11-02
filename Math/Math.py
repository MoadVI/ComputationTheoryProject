# function to calculate the product
def PI(L):
    p = 1

    for i in range(len(L)):
        p *= L[i]

    return p

def vec_add(u, v):
    return [u[i] + v[i] for i in range(len(u))]

def vec_sub(u, v):
    return [u[i] - v[i] for i in range(len(u))]

def vec_mul_scalar(u, s):
    return [u[i] * s for i in range(len(u))]

def mat_vec_mul(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

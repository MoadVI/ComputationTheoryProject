# function to calculate the product
def PI(L):
    p = 1

    for i in range(len(L)):
        p *= L[i]

    return p

def vec_add(self, u, v):
    return [u[i] + v[i] for i in range(len(u))]

def vec_sub(self, u, v):
    return [u[i] - v[i] for i in range(len(u))]

def vec_mul_scalar(self, u, s):
    return [u[i] * s for i in range(len(u))]

def mat_vec_mul(self, M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]

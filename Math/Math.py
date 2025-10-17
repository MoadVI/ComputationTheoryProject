# function to calculate the product
def PI(L):
    p = 1

    for i in range(len(L)):
        p *= L[i]

    return p

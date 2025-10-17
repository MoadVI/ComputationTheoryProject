from Discretization.KSI import KSI
from Discretization.SIGMA import SIGMA

class Discretizator:
    def __init__(self, x_min, x_max, u_min, u_max, w_min, w_max, Nx, Nu):
        self.KSI = KSI(x_min, x_max, Nx)
        self.SIGMA = SIGMA(u_min, u_max, Nu)
        self.w_min = w_min
        self.w_max = w_max

    # abstraction interface
    def q(self, x):
        try:
            return self.KSI.q(x)
        except:
            raise

    # concretisation interface
    def p(self, sigma):
        try:
            return self.SIGMA.p(sigma)
        except:
            raise
from Exceptions.Exceptions import DimensionError

class KSI:
    def __init__(self, x_min, x_max, Nx):
        self.x_min = x_min
        self.dim_x = self.getDimX()
        self.setX_max(x_max)
        self.setNx(Nx)

    # getters
    def getDimX(self):
        return len(self.x_min)

    def getX_min(self):
        return self.x_min

    def getX_max(self):
        return self.x_max

    def getNx(self):
        return self.Nx

    #setters
    def setDimX(self, dim_x):
        if dim_x == self.dim_x:
            return
        elif dim_x < self.dim_x:
            del self.x_min[dim_x:]
            del self.x_max[dim_x:]
            del self.Nx[dim_x:]
        elif dim_x > self.dim_x:
            self.x_min.extend([0] * (self.dim_x - dim_x))
            self.x_max.extend([0] * (self.dim_x - dim_x))
            self.Nx.extend([0] * (self.dim_x - dim_x))

        self.dim_x = dim_x

    def setX_min(self, x_min):
        if len(x_min) != self.dim_x:
            raise DimensionError("Err1")

        self.x_min = x_min

    def setX_max(self, x_max):
        if len(x_max) != self.dim_x:
            raise DimensionError("Err1")

        self.x_max = x_max

    def setNx(self, Nx):
        if len(Nx) != self.dim_x:
            raise DimensionError("Err1")

        self.Nx = Nx

    # Check dimension
    def check_dimension(self, x):
        if len(x) != self.dim_x:
            raise DimensionError("Err2")

    # method to check if x belong to X0
    def in_grid(self, x: list):
        for i in range(len(x)):
            if x[i] < self.x_min[i] or x[i] > self.x_max[i]:
                return False
        return True

    # abstraction interface
    def q(self, x):
        try:
            # Check the dimension
            self.check_dimension(x)

            if not self.in_grid(x): return 0

            # Calculating the interpolation ratio vector
            r = []
            for i in range(len(x)):
                ri = (x[i] - self.x_min[i]) / (self.x_max[i] - self.x_min[i])
                r.append(ri)

            # Multiplying by the division and casting
            for i in range(len(x)):
                r[i] = int(self.Nx[i] * r[i]) + 1

            # Calculating ksi
            ksi = 1  # To shift the indexation by 1
            multiplyer = 1
            for i in range(len(x)):
                ksi += multiplyer * (r[i] - 1)
                multiplyer *= self.Nx[i]

            return ksi
        except:
            raise
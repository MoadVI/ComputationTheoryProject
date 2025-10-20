class Reachability:
    def __init__(self, tau, D_x=None, D_w=None):
        self.tau = tau
        self.D_x = D_x
        self.D_w = D_w
        

    def vec_add(self, u, v):
        return [u[i] + v[i] for i in range(len(u))]

    def vec_sub(self, u, v):
        return [u[i] - v[i] for i in range(len(u))]

    def vec_mul_scalar(self, u, s):
        return [u[i] * s for i in range(len(u))]
    
    def mat_vec_mul(self, M, v):
        return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


    def f(self, x, u, w):
        """
        x(t+1) = x + tau * (u + w)
        """
        return self.vec_add(x, self.vec_mul_scalar(self.vec_add(u, w), self.tau))

    # monotone approximation method 
    def reachable_interval_Monotone(self, x_lower, x_upper, u, w_lower, w_upper):
        f_min = self.f(x_lower, u, w_lower)
        f_max = self.f(x_upper, u, w_upper)
        return f_min, f_max
    



    # approximation with Bounds 
    def reachable_interval_Bounds(self, x_lower, x_upper, u, w_lower, w_upper):
        if self.D_x is None or self.D_w is None:
            raise ValueError("D_x and D_w must be defined")
        x_star = self.vec_mul_scalar(self.vec_add(x_lower, x_upper), 0.5)
        w_star = self.vec_mul_scalar(self.vec_add(w_lower, w_upper), 0.5)

        delta_x = self.vec_mul_scalar(self.vec_sub(x_upper, x_lower), 0.5)
        delta_w = self.vec_mul_scalar(self.vec_sub(w_upper, w_lower), 0.5)

        f_star = self.f(x_star, u, w_star)

        Dx_delta_x = self.mat_vec_mul(self.D_x, delta_x)
        Dw_delta_w = self.mat_vec_mul(self.D_w, delta_w)

        abs_margin = self.vec_add(self.vec_abs(Dx_delta_x), self.vec_abs(Dw_delta_w)) # Dx delta(x) + Dw delta(w)

        f_lower = self.vec_sub(f_star, abs_margin)
        f_upper = self.vec_add(f_star, abs_margin)

        return f_lower, f_upper
    




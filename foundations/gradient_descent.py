class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x=float(init)
        lr = learning_rate
        i = iterations
        if i==0 :
            return int(x)

        while i>0 :
            i=i-1
            x=x-(lr)*(2*x)
        return round(x,5)





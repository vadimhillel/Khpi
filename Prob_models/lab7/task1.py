import numpy as np

class Task1:
    
    def __init__(self, lambda_values: np.array, states: list[str]) -> None:
        self._lambda_values = lambda_values
        self._states = states
        
    def function(self):
        """Equations"""
        
        # Construct the system of the Kolmogorov equations
        A = self._lambda_values.T - np.diag(np.sum(self._lambda_values, axis=1))
        A[-1] = np.ones(A.shape[0])  # Enforce the sum of probabilities to be 1

        # Set up the equations for the stationary distribution (pi * A = 0)
        pi = np.zeros(len(A))
        pi[-1] = 1 # Setting the last element of pi to 1 to make the equations sum to 1

        # Solve the system of equations using np.linalg.solve
        p = np.linalg.solve(A, pi)

        # Normalize the probability vector
        p /= np.sum(p)

        return p
    
    def display_p(self):
        """The marginal probabilities of the states"""
        
        print("Stationary distribution:")
        for i, state in enumerate(self._states):
            print(f"{state}: {Task1.function(self)[i]}")

def main():
    lambda_values = np.array([
        [0, 3, 0, 0],
        [4, 0, 4, 0],
        [0, 3, 0, 4],
        [0, 0, 5, 0]
    ])

    states = ["S1", "S2", "S3", "S4"]
    
    t: Task1 = Task1(lambda_values, states)
    t.display_p()
    
if __name__ == "__main__":
    main()



import numpy as np


class Markov_process:
    
    def __init__(self, transition_matrix: np.array, initial_state: np.array) -> None:
        self._transition_matrix = transition_matrix
        self._initial_state = initial_state

    def func(self):
        
        # Perform matrix multiplication for three steps
        state_after_3_steps1 = np.linalg.matrix_power(self._transition_matrix, 3) @ self._initial_state
        state_after_3_steps2 = np.matmul(np.linalg.matrix_power(self._transition_matrix, 3),
                                         self._initial_state)
        state_after_3_steps3 = (self._transition_matrix @ self._transition_matrix 
                                @ self._transition_matrix @ self._initial_state)
        return [state_after_3_steps1, state_after_3_steps2, state_after_3_steps3]

def main():
    
    # Define the transition matrix
    transition_matrix = np.array([
        [0.3, 0.13, 0.08, 0.28, 0.21],
        [0.12, 0.44, 0.16, 0.25, 0.03],
        [0.05, 0.06, 0.34, 0.49, 0.06],
        [0.52, 0.06, 0.05, 0.31, 0.06],
        [0.13, 0.05, 0.29, 0.04, 0.49]
    ])
    
    # Define the initial state
    initial_state = np.array([0, 0, 1, 0, 0])
    
    m: Markov_process = Markov_process(transition_matrix, initial_state)
    for _, state in enumerate(m.func()):
        print(f"Method {_ + 1}: State after 3 steps {state}")
        
if __name__ == "__main__":
    main()
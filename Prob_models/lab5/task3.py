import numpy as np


class Markov_process:
    
    def __init__(self, transition_matrix: np.array, 
                 state_after_3_steps: np.array) -> None:
        self._transition_matrix = transition_matrix
        self._state_after_3_steps = state_after_3_steps
        
    def find_initial_state(self):
        inverse_transition_matrix = np.linalg.inv(self._transition_matrix)
        initial_state = np.linalg.matrix_power(inverse_transition_matrix, 3) @ self._state_after_3_steps
        return initial_state
    
    def test_initial_state(self):
        return np.matmul(np.linalg.matrix_power(self._transition_matrix, 3), Markov_process.find_initial_state(self))

def main():
    # Define the transition matrix
    transition_matrix = np.array([[0.2, 0.3, 0.5],
                                [0.4, 0.2, 0.4],
                                [0.1, 0.2, 0.7]])

    # Define system's distribution of states after 3 steps
    state_after_3_steps = np.array([0.187, 0.221, 0.592])
    
    m: Markov_process = Markov_process(transition_matrix, state_after_3_steps)
    print("\nThe initial state is:", m.find_initial_state())
    
    # flake8: noqa
    print("\nBy testing the code according to task1.py it's" + 
        f" being got {m.test_initial_state()} as the initial {state_after_3_steps}")

if __name__ == "__main__":
    main()


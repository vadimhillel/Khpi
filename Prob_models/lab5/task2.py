import numpy as np


class Markov_process:
    def __init__(self, transition_matrix: np.array, initial_state: list[np.array],
                 steps: int, stationary_step: int) -> None:
        self._transition_matrix = transition_matrix
        self._initial_state = initial_state
        self._steps = steps
        self._stationary_step = stationary_step

    def stationary_step(self):
        for i in range(self._steps):
            state = np.matmul(self._initial_state[-1], self._transition_matrix)
            self._initial_state.append(state)
            if np.allclose(self._initial_state[-1], self._initial_state[-2]):
                self._stationary_step = i + 1
                return
            
    def steps_func(self):
        for _, state in enumerate(self._initial_state):
            print(f"Step {_ + 1} - Probability Distribution: {state}")
    
    def get_convergence_step(self):
        if self._stationary_step:
            print("\nThe probability distribution of system states" +
                f" becomes stationary after {self._stationary_step} steps.")
        else:
            print("\nThe probability distribution does not reach a stationary" +
                " state within the provided number of steps.")
            
    def actual_convergence_step(self, initial_steps: int):
        if self._stationary_step:
            return self._stationary_step
        else: 
            self._steps += 1000
            Markov_process.stationary_step(self)
            return self._stationary_step + initial_steps
        
def main():
    # Define the transition matrix
    transition_matrix = np.array([[0.7, 0.1, 0.1, 0.1],
                             [0.2, 0.6, 0, 0.2],
                             [0.2, 0, 0.5, 0.3],
                             [0, 0, 0, 1]])

    # Define the initial state
    initial_state = [np.array([1, 0, 0, 0])]
    
    # Define steps
    steps = 10
    
    m: Markov_process = Markov_process(transition_matrix, initial_state, steps, None)
    m.stationary_step()
    m.steps_func()
    m.get_convergence_step()

    print(f"\nActual amount of steps needed is: {m.actual_convergence_step(steps)}")
            
if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class Task3:
    
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
            print(f"{state}: {Task3.function(self)[i]}")
            
    def display_plt(self):
        """Construct a labeled state graph"""
        
        G = nx.DiGraph()
        G.add_nodes_from(self._states)

        edges = [
            (self._states[i], self._states[j], self._lambda_values[i][j])
            for i in range(len(self._states))
            for j in range(len(self._states))
            if self._lambda_values[i][j] != 0
        ]
        G.add_weighted_edges_from(edges)

        pos = nx.planar_layout(G)
        nx.draw_networkx(G,pos)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, pos, label_pos=0.5, 
                                     edge_labels=labels)
        plt.show()


def main():
    lambda_values = np.array([[0, 1/2, 0, 0],
              [0, 0, 6, 0],
              [0, 0, 0, 1],
              [12, 0, 0, 0]])

    states = ["S1", "S2", "S3", "S4"]
    
    t: Task3 = Task3(lambda_values, states)
    t.display_p()
    t.display_plt()
    
if __name__ == "__main__":
    main()

import numpy as np


class MyApplicants:
    # Generate rankings for the 1,000 princes
    def __init__(self, rankings: list) -> None:
        self._rankings = rankings

    # Strategy 1: Select the First Prince
    def strategy_1(self):
        return self._rankings[0]

    # Strategy 2: Select the Last Prince
    def strategy_2(self):
        return self._rankings[-1]

    # Strategy 3: Select a Random Prince
    def strategy_3(self):
        return np.random.choice(self._rankings)

    # Strategy 4: Select the first prince who is better than a certain threshold
    def strategy_4(self):
        threshold = len(self._rankings)/1.4
        for prince in self._rankings:
            if prince >= threshold:
                return prince
        return self._rankings[-1]

    # Strategy 5: Select the Median Prince
    def strategy_5(self):
        return np.median(self._rankings)

    # Strategy 6: Look at the first 90% of Princes and select the best one,
    # then at the final 10%, select a prince that is +- 10% 
    # the rank of the best one from first 90%
    def strategy_6(self):
        top_90_threshold = self._rankings[:900]
        max_one = max(top_90_threshold)
        for prince in self._rankings[:900]:
            if prince >= max_one - np.ceil(0.1 * max_one):
                return np.max(prince)

    # Strategy 7: Select the Prince Better Than the Previous
    def strategy_7(self):
        previous_applicant = self._rankings[0]
        for rank in self._rankings[1:]:
            if rank > previous_applicant:
                return rank

    # Strategy 8: Accept the first prince better than the average so far
    def strategy_8(self):
        average_prince = np.mean(self._rankings)
        for princes in self._rankings:
            if princes > average_prince:
                return princes

    # Strategy 9: Select the first prince who is better than a moving threshold
    def strategy_9(self):
        threshold = 0
        for i in range(len(self._rankings)):
            threshold += 1.0 / (i+1)
            if self._rankings[i] >= threshold:
                return self._rankings[i]
        return self._rankings[-1]

    # Strategy 10: Among first 100 of princes, choose 3% of the best ones, 
    # then, among other 900, choose first who is better than any from this 3%
    def strategy_10(self):
        top_3_percent_qualities = self._rankings[np.argsort(self._rankings[:100])[-3:]]
        index_of_better_prince = np.argmax(self._rankings[100:] > np.min(top_3_percent_qualities))
        return self._rankings[100 + index_of_better_prince]

    # Strategy 11: Select the Best Prince with Test and Reject
    def strategy_11(self):
        test_princes = np.random.choice(self._rankings, size=100, replace=False)
        best_test_prince = np.max(test_princes)
        better_than_best_test = [rank for rank in self._rankings if rank > best_test_prince]
        while True:
            if better_than_best_test:
                return np.min(better_than_best_test)
            else:
                test_princes = np.random.choice(self._rankings, size=100, replace=False)
                best_test_prince = np.max(test_princes)
                better_than_best_test = [rank for rank in self._rankings if rank > best_test_prince]

    # Strategy 12: Select the First Prince Better Than Half Rank
    def strategy_12(self):
        half_rank = len(self._rankings) // 2
        better_than_half_rank = [rank for rank in self._rankings if rank > half_rank]
        return np.min(better_than_half_rank)

class Main:
    
    def __init__(self, func_list: list, best_strategy: int) -> None:
        self._func_list = func_list
        self._best_strategy = best_strategy
    
    # Evaluate the average quality of each strategy
    def main_func(self):
        r = MyApplicants(np.random.permutation(1000) + 1)
        
        strat_list = [r.strategy_1, r.strategy_2, r.strategy_3, r.strategy_4, 
                    r.strategy_5, r.strategy_6, r.strategy_7, r.strategy_8, 
                    r.strategy_9, r.strategy_10, r.strategy_11, r.strategy_12]
        
        for strat in strat_list:
            self._func_list.append(np.mean(strat()))
            
        print("\nAverage Quality of Applicants:")
        for i, strat in enumerate(self._func_list, start=1):
            print(f"Strategy {i}: {strat}")    
        
        self._best_strategy = np.argmax(self._func_list) + 1  
        return self._best_strategy
    
def main(best_strategy_list: list):
    for _ in range(10):
        m: Main = Main([], [])
        m.main_func()
        best_strategy_list.append(m._best_strategy)
        
    print(f"\nThe best strategy is: {np.argmax(np.bincount(best_strategy_list))}")
    
    
if __name__ == "__main__":
    main([])

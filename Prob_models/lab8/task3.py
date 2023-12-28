def absense_of_queue(arrival_rate: int, t: int) -> float:
    """Customers per hour and average service time per customer in minutes"""
    return 1 - (1 / (1 + (arrival_rate / (60 /t))))

print(f"\nThe probability of no waiting for customers in the system: {absense_of_queue(8, 9):.4f}")
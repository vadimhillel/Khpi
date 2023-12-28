def relative_throughput(arrival_rate: int, t: int) -> float:
    """Customers per hour and average service time per customer in minutes"""
    return 1 / (1 + (arrival_rate / (60 /t)))

print(f"\nThe relative throughput is: {relative_throughput(6, 10):.2f}")
def downtime_probability(arrival_rate: int, t: int) -> float:
    """Customers per hour and average service time per customer in minutes"""
    return 1 / (1 + (arrival_rate / (60 /t)))

print(f"\nThe probability of system downtime is approximately: {downtime_probability(4, 12):.4f}")

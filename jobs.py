def job_scheduling(jobs, n):
    # Step 1: sort jobs by profit (highest first)
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Step 2: create slots (empty initially)
    slots = [-1] * n
    total_profit = 0

    # Step 3: place jobs
    for job in jobs:
        job_id, deadline, profit = job
        # try to put job in latest free slot before deadline
        for slot in range(min(n, deadline) - 1, -1,-1):
            if slots[slot] == -1:
                slots[slot] = job_id
                total_profit += profit
                break

    # Print result
    print("Scheduled Jobs:",slots)
    print("Total Profit:", total_profit)


# --- Main Program ---
# n = int(input("Enter number of jobs: "))
n=5
jobs = [
    ("J1", 2, 20),
    ("J2", 2, 60),
    ("J3", 1, 40),
    ("J4", 3, 100),
    ("J5", 4, 80)
]

print("Enter job_id deadline profit:")

# for _ in range(n):
#     job_id, deadline, profit = input().split()
#     jobs.append((job_id, int(deadline), int(profit)))

job_scheduling(jobs, n)

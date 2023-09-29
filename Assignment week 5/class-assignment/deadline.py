def deadline_driven_greedy(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: (x['profit'], -x['deadline']), reverse=True)
    
    max_deadline = max(job['deadline'] for job in sorted_jobs)
    
    schedule = [-1] * max_deadline
    
    total_profit = 0
    for job in sorted_jobs:
        for i in range(job['deadline'] - 1, -1, -1):
            if schedule[i] == -1:
                schedule[i] = job['id']
                total_profit += job['profit']
                break
    
    return schedule, total_profit

jobs = [
    {'id': 'Job1', 'profit': 50, 'deadline': 2},
    {'id': 'Job2', 'profit': 60, 'deadline': 1},
    {'id': 'Job3', 'profit': 20, 'deadline': 3},
    {'id': 'Job4', 'profit': 70, 'deadline': 2},
    {'id': 'Job5', 'profit': 30, 'deadline': 1}
]

schedule, profit = deadline_driven_greedy(jobs)
print("Scheduled Jobs:", schedule)
print("Total Profit:", profit)

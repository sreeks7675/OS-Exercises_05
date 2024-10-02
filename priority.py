#Priority Scheduling
'''
Key Characteristics:
-->Non preemptive approach that selects the process with higher priority first.
--> Lower the numerical value --> higher is the priority (Considered)
'''

def compute_times(n,processes,arrival_time,burst_time,priority):
    completion_time=[0]*n
    turnaround_time=[0]*n
    waiting_time=[0]*n
    completed=0
    is_completed=[False]*n
    time=0

    while completed<n:
        idx=-1
        highest_prior=float('inf')

        for i in range(n):
            if arrival_time[i]<=time and not is_completed[i]:
                if priority[i]<highest_prior:
                    highest_prior=priority[i]
                    idx=i
                elif priority[i]==highest_prior and arrival_time[i]<arrival_time[idx]:
                    idx=i
        if idx!=-1:
            completion_time[idx]=time+burst_time[idx]
            turnaround_time[idx]=completion_time[idx]-arrival_time[idx]
            waiting_time[idx]=turnaround_time[idx]-burst_time[idx]
            time+=burst_time[idx]
            completed+=1
            is_completed[idx]=True
            
        else:
            time+=1
    return completion_time,turnaround_time,waiting_time

def priority_scheduling(processes,arrival_time,burst_time,priority):
    n=len(processes)
    completion_time,turnaround_time, waiting_time=compute_times(n,processes,arrival_time,burst_time,priority)
    print('Processes\tArrival Time\tBurst Time\tPriority\tCompletion Time\tTurnaround Time\tWaiting Time')
    for i in range(n):
        print(f'{processes[i]} \t\t{arrival_time[i]} \t\t{burst_time[i]} \t\t{priority[i]} \t\t{completion_time[i]} \t\t{turnaround_time[i]} \t\t{waiting_time[i]}')
    print("Average Turnaround Time:",sum(turnaround_time)/n)
    print("Average Waiting Time:",sum(waiting_time)/n)

#main
processes = [1, 2, 3, 4]
arrival_time = [0, 1, 2, 3]
burst_time = [10, 1, 2, 1]
priority = [3, 1, 4, 2] 
priority_scheduling(processes, arrival_time, burst_time, priority)
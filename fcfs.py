def compute_completion_time(n,proceses,arrival_time,burst_time):
    completion_time=[0]*n
    start_time=0

    for  i in range(n):
        if start_time<arrival_time[i]:
            start_time=arrival_time[i]
        completion_time[i]=start_time+burst_time[i]
        start_time=completion_time[i]
    return completion_time

def compute_turnaround_time(n,arrival_time,completion_time):
    turnaround_time=[0]*n
    for i in range(n):
        turnaround_time[i]=completion_time[i]-arrival_time[i]
    return turnaround_time

def compute_waiting_time(n,turnaround_time,burst_time):
    waiting_time=[0]*n
    for i in range(n):
        waiting_time[i]=turnaround_time[i]-burst_time[i]
    return waiting_time

def fcfs_func(processes,arrival_time,burst_time):
    n=len(processes)
    processes_sorted=sorted(range(n),key=lambda i:arrival_time[i])
    sorted_arrival=[arrival_time[i] for i in processes_sorted]
    sorted_burst=[burst_time[i] for i in processes_sorted]

    completion_time=compute_completion_time(n,processes_sorted,sorted_arrival,sorted_burst)
    turnaround_time=compute_turnaround_time(n,sorted_arrival,completion_time)
    waiting_time=compute_waiting_time(n,turnaround_time,sorted_burst)


    print("Process \tArrival Time \tBurst Time \tCompletion Time \tTurnaround Time \tWaiting Time")
    for i in range(n):
        print(f'P{processes_sorted[i]+1} \t\t{sorted_arrival[i]} \t\t{sorted_burst[i]} \t\t{completion_time[i]} \t\t{turnaround_time[i]} \t\t{waiting_time[i]}')

    print("Average Waiting Time:",sum(waiting_time)/n)
    print("Average Turnaround Time:",sum(turnaround_time)/n)


processes=[1,2,3,4]
arrival_time=[0,1,2,3]
burst_time=[5,2,6,3]
fcfs_func(processes,arrival_time,burst_time)
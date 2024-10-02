#Non-preemptive SJF 
'''
Key Characteristics
-->Minimum average Waiting Time across all scheduling algorithms.
-->Schedules processes based on shortest burst times.
-->Can reduce starving effect caused when a number a short processes are pushed into the ready queue by ageing.
'''

def compute_completion_time(n,processes,arrival_time,burst_time):
    completion_time=[0]*n
    start_time=0
    remain_processes=list(range(n))
    while remain_processes:
        available_processes=[process for process in remain_processes if arrival_time[process]<=start_time]
        if available_processes:
            next_process=min(available_processes,key=lambda process:burst_time[process])
        else:
            next_process=min(remain_processes,lambda process:arrival_time[process])
            start_time=arrival_time[next_process]

        completion_time[next_process]=start_time+burst_time[next_process]
        start_time=completion_time[next_process]

        remain_processes.remove(next_process)
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

def sjf_func(processes,arrival_time,burst_time):
    n=len(processes)

    completion_time=compute_completion_time(n,processes,arrival_time,burst_time)
    turnaround_time=compute_turnaround_time(n,arrival_time,completion_time)
    waiting_time=compute_waiting_time(n,turnaround_time,burst_time)

    print("Processes\tArrival time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting time")
    for i in range(n):
        print(f"P{processes[i]}\t\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

    print("Average Waiting Time:",sum(waiting_time)/n)
    print("Average Turnaround Time:",sum(turnaround_time)/n)

#main
processes=[1,2,3,4,5]
arrival=[2,5,1,0,4]
burst=[6,2,8,3,4]
sjf_func(processes,arrival,burst)
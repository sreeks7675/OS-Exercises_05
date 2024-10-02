#SRTF Scheduling algorithm
'''
Key Characteristics:
-->Preemptive method of scheduling (Preemptive SJF)
-->'''
import heapq
def compute_times(n,processes,arrival_time,burst_time):
    remaining_time=burst_time[:]
    time=0
    completion_time=[0]*n
    waiting_time=[0]*n
    turnaround_time=[0]*n
    completed=0
    min_heap=[]

    while completed<n:
        for i in range(n):
            if arrival_time[i]<=time and remaining_time[i]>0 and (i not in [p[1] for p in min_heap]):
                heapq.heappush(min_heap,(remaining_time[i],i))
            
        if min_heap:
            current_burst,current_process=heapq.heappop(min_heap)

            time+=1#incrementing the time for each passing ms
            remaining_time[current_process]-=1

            if remaining_time[current_process]==0:
                completion_time[current_process]=time
                turnaround_time[current_process]=completion_time[current_process]-arrival_time[current_process]
                waiting_time[current_process]=turnaround_time[current_process]-burst_time[current_process]
                completed+=1
        else:
            time+=1

    return completion_time,turnaround_time,waiting_time
    
def srtf_func(processes,arrival_time,burst_time):
    n=len(processes)
    completion_time,turnaround_time, waiting_time=compute_times(n,processes,arrival_time,burst_time)
    print('Processes\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time')
    for i in range(n):
        print(f'{processes[i]} \t\t{arrival_time[i]} \t\t{burst_time[i]} \t\t{completion_time[i]} \t\t{turnaround_time[i]} \t\t{waiting_time[i]}')
    print("Average Turnaround Time:",sum(turnaround_time)/n)
    print("Average Waiting Time:",sum(waiting_time)/n)

#main
processes=[1,2,3,4]
arrival_time=[0,1,2,3]
burst_time=[7,4,1,4]
srtf_func(processes,arrival_time,burst_time)

            



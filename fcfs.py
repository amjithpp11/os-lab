#AMJITH PP 20219016
#FCFS

class FCFS:
    def __init__(self):
        self.burst = []
        self.arrival = []

        self.n = int(input("Enter the number of processes: "))
        for i in range(self.n):
            self.burst.append(int(input(f"Enter the burst time of process {i+1}: ")))
            self.arrival.append(int(input(f"Enter the arrival time of process {i+1}: ")))

    def findWaitingTime(self):
        self.waiting = [0] * self.n
        total_waiting = self.arrival[0]
        for i in range(self.n):
            self.waiting[i] = total_waiting - self.arrival[i]
            total_waiting += self.burst[i]

    def findTurnAround(self):
        self.turn_around = [0] * self.n
        for i in range(self.n):
            self.turn_around[i] = self.waiting[i] + self.burst[i]

    def findCompletionTime(self):
        self.completion = [0] * self.n
        completion_time = self.arrival[0]
        for i in range(self.n):
            completion_time += self.burst[i]
            self.completion[i] = completion_time

    def printTable(self):
        average_waiting = 0
        average_turn_around = 0
        print("Processes\tBurst Time\tArrival Time\tWaiting Time\tTurn-Around Time\tCompletion Time")
        for i in range(self.n):
            print(f"{i+1}\t\t{self.burst[i]}\t\t{self.arrival[i]}\t\t{self.waiting[i]}\t\t{self.turn_around[i]}\t\t\t{self.completion[i]}")
            average_waiting += self.waiting[i]
            average_turn_around += self.turn_around[i]
        print(f"Average waiting time = {average_waiting/self.n:.5f}")
        print(f"Average turn around time = {average_turn_around/self.n}")

def main():
    fcfs = FCFS()

    fcfs.findWaitingTime()
    fcfs.findTurnAround()
    fcfs.findCompletionTime()
    fcfs.printTable()

if __name__ == "__main__":
    main()
    
#OUTPUT
"""
Enter the number of processes: 5 
Enter the burst time of process 1: 2
Enter the arrival time of process 1: 0
Enter the burst time of process 2: 3
Enter the arrival time of process 2: 1
Enter the burst time of process 3: 5
Enter the arrival time of process 3: 2
Enter the burst time of process 4: 4
Enter the arrival time of process 4: 3
Enter the burst time of process 5: 6
Enter the arrival time of process 5: 4
Processes	Burst Time	Arrival Time	Waiting Time	Turn-Around TimeCompletion Time
1		2		0		0		2		2
2		3		1		1		4		5
3		5		2		3		8		10
4		4		3		7		11		14
5		6		4		10		16		20
Average waiting time = 4.20000
Average turn around time = 8.2
"""    
    
    

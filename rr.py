#AMJITH PP 20219016
# ROUND ROBIN

import copy


class RR:
    def __init__(self):
        self.ready_queue = []
        self.processes = []
        self.quantum = 2

        print("Round Robin Scheduling with Quantum 2ns")
        self.n = int(input("Enter the number of processes: "))
        for i in range(self.n):
            arrival = int(input(f"Enter the arrival time for process {i+1}: "))
            burst = int(input(f"Enter the burst time for process {i+1}: "))
            self.processes.append([i, arrival, burst, False])

    def sort(self, index):
        for i in range(len(self.processes)):
            for j in range(0, len(self.processes) - i - 1):
                if self.processes[j][index] > self.processes[j+1][index]:
                    temp = self.processes[j]
                    self.processes[j] = self.processes[j+1]
                    self.processes[j+1] = temp

    def roundRobinScheduling(self):
        self.time_elapsed = self.processes[0][1]
        self.processes_copy = copy.deepcopy(self.processes)
        self.display_data = []
        self.order = []
        while True:
            all_done = True
            for process in self.processes_copy:
                if process[2] > 0:
                    all_done = False
            if all_done:
                break
            self.setProcessArrival()
            current_process = self.ready_queue.pop(0)
            for i in range(len(self.processes)):
                if self.processes[i][0] == current_process[0]:
                    index = i
            if self.processes_copy[index][2] < self.quantum:
                self.time_elapsed += self.processes_copy[index][2]
                self.processes_copy[index][2] = 0
            else:
                self.processes_copy[index][2] -= self.quantum
                self.time_elapsed += self.quantum
            if self.processes_copy[index][2] > 0:
                self.setProcessArrival()
                self.order.append(f"P[{index+1}]")
                self.ready_queue.append(self.processes_copy[index])
            else:
                self.display_data.append([index+1, self.processes[index][1], self.processes[index][2], self.time_elapsed -
                                         self.processes[index][2] - current_process[1], self.time_elapsed - current_process[1], self.time_elapsed])

    def setProcessArrival(self):
        for process in self.processes_copy:
            if process[1] <= self.time_elapsed and process[2] > 0 and process[3] == False:
                self.order.append(f"P[{process[0]+1}]")
                process[3] = True
                self.ready_queue.append(process)

    def displayTable(self):
        average_waiting = 0
        average_turn_around = 0
        # Sort display data
        for i in range(len(self.display_data)):
            for j in range(0, len(self.display_data) - i - 1):
                if self.display_data[j][0] > self.display_data[j+1][0]:
                    temp = self.display_data[j]
                    self.display_data[j] = self.display_data[j+1]
                    self.display_data[j+1] = temp
                    #print("Sorting")
        print("Processes\tArrival Time\tBurst Time\tWaiting Time\tTurn-Around Time\tCompletion Time")
        for data in self.display_data:
            average_waiting += data[3]
            average_turn_around += data[4]
            print(f"P{data[0]}\t\t{data[1]}\t\t{data[2]}\t\t{data[3]}\t\t{data[4]}\t\t\t{data[5]}")
        print(f"Average waiting time = {average_waiting/self.n:.5f}")
        print(f"Average turn around time = {average_turn_around/self.n}")


def main():
    rr = RR()
    rr.sort(1)
    rr.roundRobinScheduling()
    rr.displayTable()


if __name__ == "__main__":
    main()

#OUTPUT
"""
Round Robin Scheduling with Quantum 2ns
Enter the number of processes: 4
Enter the arrival time for process 1: 0
Enter the burst time for process 1: 21
Enter the arrival time for process 2: 0
Enter the burst time for process 2: 3
Enter the arrival time for process 3: 0
Enter the burst time for process 3: 6
Enter the arrival time for process 4: 0
Enter the burst time for process 4: 2
Processes	Arrival Time	Burst Time	Waiting Time	Turn-Around Time	Completion Time
P1		0		21		11		32			32
P2		0		3		8		11			11
P3		0		6		11		17			17
P4		0		2		6		8			8
Average waiting time = 9.00000
Average turn around time = 17.0
"""

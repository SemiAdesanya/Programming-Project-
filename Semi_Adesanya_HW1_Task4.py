# Task 4: Implement a round robin cpu scheduling using a circular
# linked list.  Each process is represneted as a node in the list


class Node:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time  # the time the process needs on the cpu or remaining time
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):   # if there is no head then there are no processes left
        return self.head is None

    def append(self, pid, burst_time):
        new_node = Node(pid, burst_time)
        if self.head is None:              # if it is the first process it will point back to itself
            new_node.next = new_node
            self.head = new_node
            return
        curr = self.head
        while curr.next != self.head:  # to find the last node so we can add the new process at the end 
            curr = curr.next
        curr.next= new_node  # to connect the last node to the new node then make the new node point back to 
        new_node.next = self.head   # the head to keep the list circular
        

    def remove(self, node):
        if self.head is None: # there would be nothing to remove if the list is already empty
            return
        if node.next is node: # to check if the node is the only process left in the list
            self.head = None
            return  
        if node is self.head: # if we are removing the first node then we need to update the head
            curr = self.head

            while curr.next != self.head: # to find the last node so it can point to the new head
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
            return

        prev = self.head
        while prev.next is not node:  # so that for any other node we find the node that comes before it
            prev = prev.next
            if prev is self.head: # if we get back to the head and the node was not found
                return
        prev.next = node.next # to skip over the node being removed and connect to the next one

                

    def display(self):
        if self.head is None: # to display a message if there are no processes in the list
            print("No processes in the list.")
            return
        curr = self.head # to start at the head and go through each process once
        while True:
            print(f"Process {curr.pid}: Remaining Burst Time = {curr.burst_time}")
            curr = curr.next
            if curr is self.head: # to stop when we reach the head again
                break


def units(n):
    return f"{n} unit" if n == 1 else f"{n} units"


def round_robin(processes, quantum_time):
    if not (1 <= len(processes) <= 50) or not (1 <= quantum_time <= 10): # the constraints
        raise ValueError("Need 1-50 processes and a quantum between 1 and 10")
    if any(not (1 <= b <= 100) for _, b in processes):
        raise ValueError("Burst times must be between 1 and 100")

    cll = CircularLinkedList() # to create the circular linked list and add all the processes
    for pid, burst in processes:
        cll.append(pid, burst)

    print("Processes in the list:") # to show the processes and their starting burst times
    cll.display()
    print("\nStarting Round Robin Scheduling:")

    time = 0 # it keeps track of the total time used by the CPU
    current = cll.head # to start with the first process in the circular linked list
    while not cll.is_empty():  # so that it keeps going until every process has finished
        nxt = current.next    # to save the next process before making any changes and also becuase the current node
        print(f"Time: {time}, Processing PID: {current.pid}") # might be removed

        
        run = min(quantum_time, current.burst_time) # a process can only use the time quantum or the time it has left
        current.burst_time -= run  # subtract the time used from the processs remaining burst time
        time += run  # add the time used to the total CPU time

        if current.burst_time <= 0: # if the burst time reaches zero then the process is done
            print(f"Process {current.pid} completed.")
            cll.remove(current) # to remove the completed process from the circular linked list
        else:   # if the process is not finished then it will display how much time it has left
            print(f"Process {current.pid} now has {units(current.burst_time)} remaining.")
        current = nxt # so that it can move on to the next process in the list

    print("All processes completed.")
    print(f"Total time taken: {time}")
    return time


# to test...the total CPU time should equal the sum of all the original burst times
# because the CPU isnt idle here
def run_test(title, processes, quantum):
    print(f"\n=== {title} ===")
    total = round_robin(processes, quantum)
    expected = sum(b for _, b in processes)
    assert total == expected, f"Expected {expected}, got {total}"   

# driver code
if __name__ == "__main__":
    print("\n=== Circular Linked List Test ===") # testing the circular linked list

    lst = CircularLinkedList()

    print("Empty before adding:", lst.is_empty())

    lst.append(1, 5)
    lst.append(2, 6)
    lst.append(3, 7)

    print("\nProcesses after adding:")
    lst.display()

    lst.remove(lst.head) # remove the first process and check that the list still works

    print("\nProcesses after removing the head:")
    lst.display()

    print("Empty now:", lst.is_empty())
    

    run_test("Example", [(1, 10), (2, 5), (3, 8)], 4) # test 1: the example provided in the assignment 

    run_test("Single Process", [(1, 7)], 3) # test 2: only one process in the list

    run_test("Quantum Bigger Than Burst Times", [(1, 2), (2, 3)], 10) # test 3: time quantum is bigger than the burst times

    run_test("Minimum Values", [(1, 1), (2, 1)], 1) # test 4: minimum burst time and minimum quantum

    run_test("Maximum Values", [(1, 100)], 10) # test 5: maximum burst time and maximum quantum

    run_test("Burst Time Equals Quantum", [(1, 4), (2, 4), (3, 4)], 4) # test 6: to check what happens when the burst time equals the quantum

    run_test("Head Finishes First", [(1, 1), (2, 9), (3, 9)], 3) # test 7: to check when removing the head, middle, and last nodes first
    run_test("Middle Finishes First", [(1, 9), (2, 1), (3, 9)], 3)
    run_test("Last Process Finishes First", [(1, 9), (2, 9), (3, 1)], 3)

    many = [(i, (i * 7) % 100 + 1) for i in range(1, 51)] # test 8: to check the maximum number of processes allowed
    run_test("Maximum Number of Processes", many, 10)


